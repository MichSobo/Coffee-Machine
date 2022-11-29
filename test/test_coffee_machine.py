import unittest

from source.coffee_machine import CoffeeMachine


class TestCoffeeMachine(unittest.TestCase):
    """Class for testing Coffee class."""

    def setUp(self):
        """Initialize a test with default parameters"""
        self.machine = CoffeeMachine(500, 250, 100, 10, 300)

    def test_can_prepare(self):
        """can_prepare() tests with sufficient ingredients"""
        machine = CoffeeMachine(1e6, 1e6, 1e6, 1e6, 1e6)

        self.assertTrue(machine.can_prepare('1')[0])
        self.assertTrue(machine.can_prepare('2')[0])
        self.assertTrue(machine.can_prepare('3')[0])

    def test_can_prepare_water(self):
        """can_prepare() tests with missing water"""
        required_water = {}
        for coffee_id, coffee_properties in CoffeeMachine._COFFEE_TYPES.items():
            required_water[coffee_id] = coffee_properties['water']

        self.machine.water = required_water['1'] - 1
        self.assertEqual((False, 'water'), self.machine.can_prepare('1'))

        self.machine.water = required_water['2'] - 1
        self.assertEqual((False, 'water'), self.machine.can_prepare('2'))

        self.machine.water = required_water['3'] - 1
        self.assertEqual((False, 'water'), self.machine.can_prepare('3'))

    def test_can_prepare_milk(self):
        """can_prepare() tests with missing milk"""
        required_milk = {}
        for coffee_id, coffee_properties in CoffeeMachine._COFFEE_TYPES.items():
            required_milk[coffee_id] = coffee_properties.get('milk', 1)

        self.machine.milk = required_milk['1'] - 1
        self.assertEqual((True, None), self.machine.can_prepare('1'))

        self.machine.milk = required_milk['2'] - 1
        self.assertEqual((False, 'milk'), self.machine.can_prepare('2'))

        self.machine.milk = required_milk['3'] - 1
        self.assertEqual((False, 'milk'), self.machine.can_prepare('3'))

    def test_can_prepare_coffee(self):
        """can_prepare() tests with missing coffee"""
        required_coffee = {}
        for coffee_id, coffee_properties in CoffeeMachine._COFFEE_TYPES.items():
            required_coffee[coffee_id] = coffee_properties['coffee']

        self.machine.coffee = required_coffee['1'] - 1
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('1'))

        self.machine.coffee = required_coffee['2'] - 1
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('2'))

        self.machine.coffee = required_coffee['3'] - 1
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('3'))

    def test_can_prepare_cups(self):
        """can_prepare() tests with missing cups"""
        self.machine.cups = 0
        self.assertEqual((False, 'cups'), self.machine.can_prepare('1'))
        self.assertEqual((False, 'cups'), self.machine.can_prepare('2'))
        self.assertEqual((False, 'cups'), self.machine.can_prepare('3'))

    def test_sell01(self):
        """Test sell method for coffee type 1."""
        answer = 'CoffeeMachine(water=250, milk=250, coffee=84, cups=9, ' \
                 'money=304, last_action=buy, last_option=1)'

        self.machine.sell('1')
        output = self.machine.__repr__()

        self.assertEqual(answer, output)

    def test_sell02(self):
        """Test sell method for coffee type 2."""
        answer = 'CoffeeMachine(water=150, milk=175, coffee=80, cups=9, ' \
                 'money=307, last_action=buy, last_option=2)'

        self.machine.sell('2')
        output = self.machine.__repr__()

        self.assertEqual(answer, output)

    def test_sell03(self):
        """Test sell method for coffee type 3."""
        answer = 'CoffeeMachine(water=300, milk=150, coffee=88, cups=9, ' \
                 'money=306, last_action=buy, last_option=3)'

        self.machine.sell('3')
        output = self.machine.__repr__()

        self.assertEqual(answer, output)

    def test_fill01(self):
        """Test fill method with all items."""
        answer = 'CoffeeMachine(water=1000, milk=500, coffee=200, cups=20, ' \
                 'money=300, last_action=fill, last_option=(500, 250, 100, 10))'

        self.machine.fill(500, 250, 100, 10)
        output = self.machine.__repr__()

        self.assertEqual(answer, output)

    def test_fill02(self):
        """Test fill method with selected item."""
        answer = 'CoffeeMachine(water=1000, milk=250, coffee=100, cups=10, ' \
                 'money=300, last_action=fill, last_option=(500, 0, 0, 0))'

        self.machine.fill(500,)
        output = self.machine.__repr__()

        self.assertEqual(answer, output)

    def test_give(self):
        """Test give method."""
        answer = 'CoffeeMachine(water=500, milk=250, coffee=100, cups=10, ' \
                 'money=0, last_action=take, last_option=None)'

        self.machine.give(show=False)
        output = self.machine.__repr__()

        self.assertEqual(answer, output)


if __name__ == "__main__":
    unittest.main(verbosity=2)