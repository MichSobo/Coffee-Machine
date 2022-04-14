import unittest

from coffee_machine import CoffeeMachine


class TestCoffeeMachine(unittest.TestCase):
    """Class for testing Coffee class."""

    def setUp(self):
        """Initialize a test with default parameters"""
        self.machine = CoffeeMachine(500, 250, 100, 10, 300)

    def test_can_prepare(self):
        """Test can_prepare method with sufficient ingredients."""
        answer = True, None

        output = self.machine.can_prepare('1')
        self.assertEqual(answer, output)

        output = self.machine.can_prepare('2')
        self.assertEqual(answer, output)

        output = self.machine.can_prepare('3')
        self.assertEqual(answer, output)

    def test_can_prepare_water(self):
        """Test can_prepare method with missing water."""
        self.machine.water = 249
        self.assertEqual((False, 'water'), self.machine.can_prepare('1'))

        self.machine.water = 349
        self.assertEqual((False, 'water'), self.machine.can_prepare('2'))

        self.machine.water = 199
        self.assertEqual((False, 'water'), self.machine.can_prepare('3'))

    def test_can_prepare_milk(self):
        """Test can_prepare method with missing milk."""
        self.machine.milk = 1
        self.assertEqual((True, None), self.machine.can_prepare('1'))

        self.machine.milk = 74
        self.assertEqual((False, 'milk'), self.machine.can_prepare('2'))

        self.machine.milk = 99
        self.assertEqual((False, 'milk'), self.machine.can_prepare('3'))

    def test_can_prepare_coffee(self):
        """Test can_prepare method with missing coffee."""
        self.machine.coffee = 15
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('1'))

        self.machine.coffee = 19
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('2'))

        self.machine.coffee = 11
        self.assertEqual((False, 'coffee'), self.machine.can_prepare('3'))

    def test_can_prepare_cups(self):
        """Test can_prepare method with missing cups."""
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