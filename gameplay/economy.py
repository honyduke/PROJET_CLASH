from gameplay.building import Building


class Economy:

    def __init__(self, resources):

        # Référence vers les ressources du joueur
        self.resources = resources

        # Dictionnaire contenant tous les bâtiments construits
        self.buildings = {}

        # Accumulateurs permettant de conserver les fractions
        # de ressources produites
        self.production_remainders = {}

        # Identifiant du prochain bâtiment
        self.next_building_id = 1

    def build(self, building_type, position):

        """
        Construit un bâtiment si le joueur possède suffisamment
        de ressources.
        """

        # Création temporaire du bâtiment pour vérifier son type
        try:
            building = Building(building_type, position)
        except ValueError:
            return False

        # Récupération du prix de construction
        cost = building.data["build_cost"]

        # Vérification des ressources disponibles
        for resource, amount in cost.items():

            if self.resources.amounts[resource] < amount:
                return False

        # Paiement du bâtiment
        for resource, amount in cost.items():
            self.resources.spend_resource(resource, amount)

        # Attribution d'un identifiant unique
        building_id = f"building_{self.next_building_id}"

        self.buildings[building_id] = building

        self.production_remainders[building_id] = 0

        self.next_building_id += 1

        return True

    def upgrade_building(self, building_id):

        """
        Améliore un bâtiment après vérification du prix
        et des ressources disponibles.
        """

        # Vérifie que le bâtiment existe
        if building_id not in self.buildings:
            return False

        building = self.buildings[building_id]

        # Récupération du prix de l'amélioration
        cost = building.get_upgrade_cost()

        # Vérifie que le bâtiment peut encore être amélioré
        if cost is None:
            return False

        # Vérifie que le joueur possède suffisamment d'or
        if self.resources.amounts["gold"] < cost:
            return False

        # Paiement puis amélioration
        self.resources.spend_resource("gold", cost)

        return building.upgrade()

    def update(self, elapsed_time):

        """
        Calcule la production de ressources des bâtiments
        en fonction du temps écoulé, exprimé en secondes.
        """

        for building_id, building in self.buildings.items():

            resource = building.data["production_resource"]

            # Production par minute du bâtiment
            production_per_minute = building.get_production()

            # Calcul de la production pendant le temps écoulé
            production = production_per_minute * elapsed_time / 60

            # Ajout de la production précédente non entière
            production += self.production_remainders[building_id]

            # On ne récupère que la partie entière
            whole_production = int(production)

            # On conserve la partie décimale pour le prochain calcul
            self.production_remainders[building_id] = (
                production - whole_production
            )

            # Ajout des ressources au joueur
            self.resources.add_resource(resource, whole_production)