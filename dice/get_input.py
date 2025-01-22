from probability_table import ProbabilityTable
from config import SystemInputOptions
from rich.console import Console

class GetInput:
    console = Console()

    def __init__(self, dices, data, baned_options=(), is_number=True):
        self.command = ""
        self.data = data
        self.is_number = is_number
        self.dices = dices
        self.baned_options = baned_options
        self.options = [str(n) for n in range(self.data if is_number else len(self.data))]

    def __print_2d_array_options(self):
        for num in range(len(self.data)):
            print(num, '-', self.data[num])

    def __print_system_options(self):
        for sys_opt in self.system_options:
            self.console.print(
                sys_opt,
                '-',
                SystemInputOptions.INPUT_OPTIONS[sys_opt].capitalize(),
                style="blue")

    def __print_integer_options(self):
        for num in range(self.data):
            print(num, '-', num)

    def __print_options(self):
        if self.is_number:
            self.__print_integer_options()
        else:
            self.__print_2d_array_options()
        self.__print_system_options()

    @property
    def system_options(self):
        opt = filter(lambda x:x not in self.baned_options, SystemInputOptions.INPUT_OPTIONS.keys())
        return list(opt)

    def __validate(self):
        if not (self.command in self.options or self.command in self.system_options):
            self.console.print('Invalid command. Try again!', style="red bold")
            self.get_command()

    def __execute(self):
        if self.command in ['X', 'x']:
            print('Thank you! Bye :)')
            exit()
        elif self.command == '?':
            probability_table = ProbabilityTable(self.dices)
            probability_table.print()
            self.get_command()
        else:
            index = int(self.command)
            return index

    def get_command(self):
        self.__print_options()
        self.command = input()
        self.__validate()
        return self.__execute()