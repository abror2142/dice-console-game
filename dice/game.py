import sys

from error import ErrorHandling
from game_abstraction import GameAbstraction


class Game(ErrorHandling, GameAbstraction):

    def __init__(self, dices):
        super().__init__(dices)
        self.dices = [dice.split(',') for dice in dices]

    def play(self):
        self.handle_errors()
        self.determine_first_move()
        self.start_game()


game = Game(sys.argv[1:])
game.play()