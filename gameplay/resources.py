

class Resources:
    def __init__(self):
        #dictionnaire contenant les ressources du joueur
        self.amounts = {
            "gold": 500,
            "elixir": 500,
        }
        #dictionnaire contenant les capacités maximales de stockage des ressources du joueur
        self.maximum = {
            "gold": 1000,
            "elixir": 1000,
        }




    

#fonction permettant au joueur de gagner des ressources: vérifie que la ressource existe, que la quantité est positive et que le joueur ne dépasse pas la capacité maximale de stockage

    def add_resource(self, resource, amount):
        if amount < 0:
            return False

        if resource not in self.amounts:
            return False

        #ajoute les ressources au joueur

        self.amounts[resource]+= amount

        #empeche le joueur de dépasser la capacité maximale de stockage

        self.amounts[resource] = min(self.amounts[resource], self.maximum[resource])
        return True

#fonction permettant au joueur de dépenser des ressources: la dépense est possible si le joueur possède assez de ressources

    def spend_resources(self, resource, amount):
        if amount < 0:
            return False

        if resource not in self.amounts:
            return False

         #vérifie que le joueur a assez de ressources pour dépenser amount demandé

        if self.amounts[resource] < amount:
            return False

        #dépense les ressources du joueur

        self.amounts[resource]-= amount
        return True







