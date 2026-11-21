import unittest

from gameplay.resources import Resources


class TestResources(unittest.TestCase):

    # Cette fonction est exécutée avant chaque test
    def setUp(self):
        self.resources = Resources()

    def test_initial_values(self):
        self.assertEqual(self.resources.amounts["gold"], 500)
        self.assertEqual(self.resources.amounts["elixir"], 500)

    def test_add_resource(self):
        self.resources.add_resource("gold", 100)

        self.assertEqual(self.resources.amounts["gold"], 600)

    def test_maximum_storage(self):
        self.resources.add_resource("gold", 1000)

        self.assertEqual(self.resources.amounts["gold"], 1000)

    def test_spend_resource(self):
        self.resources.spend_resource("gold", 200)

        self.assertEqual(self.resources.amounts["gold"], 300)

    def test_insufficient_resources(self):
        result = self.resources.spend_resource("gold", 1000)

        self.assertFalse(result)
        self.assertEqual(self.resources.amounts["gold"], 500)


if __name__ == "__main__":
    unittest.main()
