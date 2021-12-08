from collections import namedtuple

# Command (e.g. "forward 9")
Command = namedtuple('Command', 'command_type value')


class Submarine:
    """ Submarine with position, depth and the functions for its movement. """

    def __init__(self):
        self.position = 0
        self.depth = 0

    def forward(self, value: int):
        self.position += value

    def up(self, value: int):
        self.depth -= value

    def down(self, value: int):
        self.depth += value

    def do_command(self, command: Command):
        getattr(self, command.command_type)(command.value)

    def multiply_position_depth(self):
        return self.position * self.depth

    def calculate_final_position(self, course: list):
        for command in course:
            self.do_command(command)


class SubmarineUpdate(Submarine):
    """
    Added new aim attribute to the Submarine and update moving functions.
    """

    def __init__(self):
        super(SubmarineUpdate, self).__init__()
        self.aim = 0

    def forward(self, value: int):
        self.position += value
        self.depth += self.aim * value

    def up(self, value: int):
        self.aim -= value

    def down(self, value: int):
        self.aim += value


def calculate_multiply_position(course: list) -> int:
    """ Part 1. Return multiply position by depth. """
    submarine = Submarine()
    submarine.calculate_final_position(course)
    return submarine.multiply_position_depth()


def update_calculate_multiply_position(course: list) -> int:
    """ Part 2. Return multiply position by depth. """
    submarine = SubmarineUpdate()
    submarine.calculate_final_position(course)
    return submarine.multiply_position_depth()


if __name__ == '__main__':
    input_course = []
    # Create new course for submarine like this:
    # input_course = [Command(command_type='forward', value=9), ...]
    with open('input.txt', 'r') as file:
        for input_command in file.read().split('\n'):
            x, y = input_command.split(' ')
            input_course.append(Command(command_type=x, value=int(y)))

    print('Part 1:', calculate_multiply_position(input_course))
    print('Part 2:', update_calculate_multiply_position(input_course))
