
from gameplay.resources import Resources
from gameplay.economy import Economy


# Création des ressources du joueur
player_resources = Resources()

# Création du système économique
economy = Economy(player_resources)


print("WELCOME TO PROJECT CLASH")

print("Gold:", player_resources.amounts["gold"])
print("Elixir:", player_resources.amounts["elixir"])


# Construction d'une mine d'or
economy.build("gold_mine", (3, 5))

# Simulation de 60 secondes de jeu
economy.update(60)


print("After 1 minute:")

print("Gold:", player_resources.amounts["gold"])
print("Elixir:", player_resources.amounts["elixir"])