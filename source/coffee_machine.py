#! python3
class CoffeeMachine:
    """Represents a coffee machine."""

    _COFFEE_TYPES = {
        '1': {
            'name': 'espresso',
            'water': 250,
            'coffee': 16,
            'cost': 4,
        },
        '2': {
            'name': 'latte',
            'water': 350,
            'milk': 75,
            'coffee': 20,
            'cost': 7,
        },
        '3': {
            'name': 'cappuccino',
            'water': 200,
            'milk': 100,
            'coffee': 12,
            'cost': 6,
        }
    }

    VALID_ACTIONS = ('buy', 'fill', 'take', 'remaining', 'exit')

    def __init__(self, water=0, milk=0, coffee=0, cups=0, money=0):
        """Initialize a CoffeeMachine object empty by default."""
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.last_action = None
        self.last_option = None

    def __repr__(self):
        contents = [f'{key}={value}' for key, value in self.__dict__.items()]
        contents_str = ', '.join(contents)
        return f'CoffeeMachine({contents_str})'

    def show_content(self):
        """Display the coffee machine content."""
        print('\nThe coffee machine has:')
        print(f'{self.water} ml of water')
        print(f'{self.milk} ml of milk')
        print(f'{self.coffee} g of coffee beans')
        print(f'{self.cups} disposable cups')
        print(f'${self.money} of money')

    def can_prepare(self, selection):
        """Check that the selected beverage can be prepared."""
        coffee_type = CoffeeMachine._COFFEE_TYPES[selection]

        # Check if there is enough water
        if self.water // coffee_type['water'] == 0:
            return False, 'water'

        # Check if there is enough milk (excluding espresso selection)
        if selection != '1':
            if self.milk // coffee_type['milk'] == 0:
                return False, 'milk'

        # Check if there is enough coffee
        if self.coffee // coffee_type['coffee'] == 0:
            return False, 'coffee'

        # Check if there is enough cups
        if self.cups == 0:
            return False, 'cups'

        return True, None

    def sell(self, selection):
        """Update the machine content after selling selected coffee."""
        coffee_types = CoffeeMachine._COFFEE_TYPES

        # Check if the selected beverage can be prepared
        can_prepare, missing = self.can_prepare(selection)
        if not can_prepare:
            print(f'Sorry, not enough {missing}!')
            return None
        else:
            print('I have enough resources, making you a coffee!')

        # Update machine content
        self.water -= coffee_types[selection]['water']
        self.coffee -= coffee_types[selection]['coffee']
        self.cups -= 1
        self.money += coffee_types[selection]['cost']

        if selection != '1':
            self.milk -= coffee_types[selection]['milk']

        # Update last action and last selection
        self.last_action = 'buy'
        self.last_option = selection

    def fill(self, water=0, milk=0, coffee=0, cups=0):
        """Fill the coffee machine content with provided supplies."""
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups

        # Update last action and provided supplies
        self.last_action = 'fill'
        self.last_option = (water, milk, coffee, cups)

    def give(self, show=True):
        """Clear cash register."""
        if show:
            print('I gave you $', self.money, '\n')
        self.money = 0

        # Update last action
        self.last_action = 'take'
        self.last_option = None

    def get_buy_option(self):
        """Get a valid option for 'buy' action."""
        valid_options = list(self._COFFEE_TYPES.keys())
        valid_options.append('back')

        # Formulate a prompt
        options_prompt = \
            [f'{option} - {properties["name"]}'
             for option, properties in self._COFFEE_TYPES.items()]
        options_prompt.append('back - to main menu:\n')
        options_prompt = ', '.join(options_prompt)
        prompt = '\nWhat do you want to buy? ' + options_prompt

        # Get option
        while True:
            option = input(prompt)

            if option in valid_options:
                return self.get_action() if option == 'back' else option
            else:
                print("Invalid command. Try again.")

    @staticmethod
    def get_fill_option():
        """Get a valid option for 'fill' action."""
        # Get 'fill' option
        water = int(input('\nWrite how many ml of water you want to add:\n'))
        milk = int(input('Write how many ml of milk you want to add:\n'))
        coffee = int(input('Write how many grams of coffee you want to add:\n'))
        cups = int(input(
            'Write how many disposable cups of coffee you want to add:\n'))

        return water, milk, coffee, cups

    def get_action(self):
        """Get user action.

        The function gets a user input until it is valid or the user command
        is 'exit'. The user input determines the action that would be invoked
        (buy, fill, take, remaining, exit).
        The function returns False on 'exit' command, True otherwise.
        """
        # Get input until valid input is provided or 'exit' command
        while True:
            action = input(f'\nWrite action ({", ".join(self.VALID_ACTIONS)}):\n')
            if action in self.VALID_ACTIONS:
                if action == 'exit':
                    return False
                break
            else:
                print("Invalid command. Try again.")

        # Check if the last action is the same as the current one
        if self.last_action == action:
            option = self.last_option
            DO_GET_OPTION = False
        else:
            DO_GET_OPTION = True

        # Execute according to selected action
        if action == 'buy':
            if DO_GET_OPTION:
                option = self.get_buy_option()
            self.sell(option)
        elif action == 'fill':
            if DO_GET_OPTION:
                option = self.get_fill_option()
            self.fill(*option)
        elif action == 'take':
            self.give()
        elif action == 'remaining':
            self.show_content()

        return True


if __name__ == "__main__":
    # Initialize a coffee machine
    machine = CoffeeMachine(500, 250, 100, 10, 300)

    # Get user action
    DO_USE_MACHINE = True
    while DO_USE_MACHINE:
        DO_USE_MACHINE = machine.get_action()
