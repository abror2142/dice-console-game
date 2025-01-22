import re
from rich.console import Console

from config import DICE_FACES


class ErrorHandling:
    error = None
    tip = None

    def __int__(self, dices):
        self.dices = dices

    def print_error(self):
        console = Console()
        console.print(self.error, style="red")
        console.print(f">> {self.tip}", style="green italic")

    def has_valid_length(self):
        for dice in self.dices:
            if len(dice) != DICE_FACES:
                self.tip = f"Every dice should contain exactly {DICE_FACES} faces: {dice}"
                return False
        return True

    def is_int(self):
        for dice in self.dices:
            for face in dice:
                if re.search("\D", face):
                    self.tip = f"Only integer values are permitted in a dice: {",".join(dice)}"
                    return False
        return True

    def handle_errors(self):
        if not self.dices:
            self.error = "You did not pass dices as argument!"
            self.tip = "Pass at least 3 dice elements."
        elif len(self.dices) < 3:
            self.error = f"You passed {len(self.dices)} arguments!"
            self.tip = "Pass at least 3 dice elements."
        elif not self.has_valid_length():
            self.error = "Invalid number of faces in a dice!"
        elif not self.is_int():
            self.error = "Invalid type of value found in dice!"

        if self.error:
            self.print_error()
            exit()