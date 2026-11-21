BUILDINGS_DATA = {

    "gold_mine": {

        "name": "Mine d'or",

        "build_cost": {
            "gold": 200
        },

        "production_resource": "gold",

        "production_by_level": {
            1: 10,
            2: 20,
            3: 35
        },

        "upgrade_costs": {
            1: 200,
            2: 400
        }
    },

    "elixir_collector": {

        "name": "Extracteur d'elixir",

        "build_cost": {
            "gold": 200
        },

        "production_resource": "elixir",

        "production_by_level": {
            1: 10,
            2: 20,
            3: 35
        },

        "upgrade_costs": {
            1: 200,
            2: 400
        }
    }
}

BUILDINGS_DATA["gold_mine"]["production_by_level"][2]