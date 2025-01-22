import secrets

from fair_random_generator import FairRandomGenerator
from get_input import GetInput
from config import SystemInputOptions,DICE_FACES


class GameAbstraction:
    user_first = False

    def __init__(self, dices):
        self.dices = dices

    @staticmethod
    def computer_dice_choice(dices):
        random_index = secrets.randbelow(len(dices))
        return random_index

    def determine_first_move(self):
        limit = 2  # Only 0 and 1 is enough, like heads / tails in coin.
        # Computer generates "fair random number and hashes it"
        print("Let's determine who makes the first move.")
        fair_random_generator = FairRandomGenerator(limit)
        credentials = fair_random_generator.generate()
        print("Try guess my selection.")

        inputer = GetInput(self.dices, limit, baned_options=[SystemInputOptions.HELP])
        user_choice = inputer.get_command()
        print(user_choice, "CHOICE")
        print('Your selection is:', user_choice)
        print('My selection is:', credentials['value'])
        print(f"(KEY={credentials['key']}).")

        # If user guesses correctly, he/she starts the first move.
        if credentials['value'] == user_choice:
            self.user_first = True

    @staticmethod
    def print_result(cp_num, user_num):
        if cp_num > user_num:
            print(f"I win {cp_num} > {user_num}!")
        elif cp_num < user_num:
            print(f"You win {cp_num} < {user_num}!")
        else:
            print(f"Draw {cp_num} = {user_num}!")

    def user_chooses_dice(self, dices):
        print("Choose your dice:")
        inputer = GetInput(self.dices, dices, is_number=False)
        user_choice = inputer.get_command()
        print(f"You chose the {dices[user_choice]} dice.")
        return user_choice

    def computer_chooses_dice(self, dices):
        cp_choice = self.computer_dice_choice(dices)
        print(f"I chose {self.dices[cp_choice]} dice.")
        return cp_choice

    def computer_rolls(self, limit):
        # Computer chooses a random number
        print("It is time for my throw")
        fair_random_generator = FairRandomGenerator(limit)
        credentials = fair_random_generator.generate()

        # User choose a number
        print('Add your number modulo 6.')
        inputer = GetInput(self.dices, limit, baned_options=[SystemInputOptions.HELP])
        user_choice = inputer.get_command()

        # Summarize choices
        print(f"Your selection is:", user_choice)
        print("My selection is:", credentials['value'])
        print(f"(KEY={credentials['key']}).")
        # Find mod for "fair choice"
        [_, mod] = divmod(credentials['value'] + user_choice, limit)
        print(f"The result is {credentials['value']} + {user_choice} = {credentials['value'] + user_choice} mod(6)")
        return mod

    def user_rolls(self, limit):
        # Computer choose random number
        print("It is time for your throw.")
        fair_random_generator = FairRandomGenerator(limit)
        credentials = fair_random_generator.generate()

        # User choose a number
        print('Add your number modulo 6.')
        inputer = GetInput(self.dices, limit, baned_options=[SystemInputOptions.HELP])
        user_choice = inputer.get_command()

        # Summarize choices
        print(f"Your selection is:", user_choice)
        print("My selection is:", credentials['value'])
        print(f"(KEY={credentials['key']}).")
        # Find mod to make "a fair choice"
        [_, mod] = divmod(credentials['value'] + user_choice, limit)
        print(f"The result is {credentials['value']} + {user_choice} = {credentials['value'] + user_choice} mod(6)")
        return mod

    def start_game(self):
        limit = DICE_FACES
        if self.user_first:
            # User chooses a dice
            print(f"You make the first move and choose.")
            user_dice_choice = self.user_chooses_dice(self.dices)

            # Computer chooses a dice from reminded dices
            reminded_dices = [self.dices[i] for i in range(len(self.dices)) if i != user_dice_choice]
            cp_dice_choice = self.computer_chooses_dice(reminded_dices)

            # User's turn: He/she rolls his/her dice
            mod = self.user_rolls(limit)
            user_num = self.dices[user_dice_choice][mod]
            print("Your throw is", user_num)

            # Computer's turn: Computer rolls its dice
            mod = self.computer_rolls(limit)
            cp_num = reminded_dices[cp_dice_choice][mod]
            print("My throw is", cp_num)

            # Print result
            self.print_result(int(cp_num), int(user_num))

        else:
            # Computer chooses a dice
            print(f"I make the first move ")
            cp_dice_choice = self.computer_chooses_dice(self.dices)

            # User chooses a dice
            reminded_dices = [self.dices[i] for i in range(len(self.dices)) if i != cp_dice_choice]
            user_dice_choice = self.user_chooses_dice(reminded_dices)

            # Computer rolls its dice
            mod = self.computer_rolls(limit)
            cp_num = self.dices[cp_dice_choice][mod]
            print("My throw is", cp_num)

            # User rolls his/her dice
            mod = self.user_rolls(limit)
            user_num = reminded_dices[user_dice_choice][mod]
            print("Your throw is", user_num)

            # Print Result
            self.print_result(int(cp_num), int(user_num))