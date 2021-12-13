class Board:
    def __init__(self, input_board: str):
        self.board = tuple(
            row for row in input_board.split()
        )
        self.rows = tuple(self.board[x * 5:(x + 1) * 5] for x in range(5))
        self.columns = tuple(self.board[x::5] for x in range(5))
        self.matched_numbers = []
        self.is_winner = False

    def check_board_for_victory(self):
        """
        Check board for marked numbers on rows and columns.
        If all numbers in row or column are marked -> board is win.
        """
        for row, column in zip(self.rows, self.columns):
            if (
                    all(x in self.matched_numbers for x in row) or
                    all(x in self.matched_numbers for x in column)):
                self.is_winner = True
                return self
        return False

    def match(self, number: str):
        """ Marking input number in board if it is here. """
        if number in self.board:
            self.matched_numbers.append(number)
        if len(self.matched_numbers) >= 5:
            return self.check_board_for_victory()

    def get_final_score(self):
        """ Return final score for winner board. """
        sum_unmatched_numbers = sum(
            int(x) for x in self.board if x not in self.matched_numbers
        )
        return sum_unmatched_numbers * int(self.matched_numbers[-1])


def play_bingo(numbers: tuple[str], boards: tuple[Board]):
    """ Part 1. Marking all input numbers in boards and search winner. """
    for number in numbers:
        for board in boards:
            winner = board.match(number)
            if winner:
                return winner.get_final_score()


def play_update_bingo(numbers: tuple[str], boards: tuple[Board]):
    """ Part 2. Search last winner board. """
    for number in numbers:
        winner_boards = []
        for board in boards:
            winner = board.match(number)
            if winner:
                if len(boards) != 1:
                    winner_boards.append(winner)
                else:
                    return winner.get_final_score()
        # Delete winner boards from list
        boards = tuple(x for x in boards if x not in winner_boards)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read().split('\n\n')
        input_numbers = tuple(x for x in data[0].split(','))
        input_boards = tuple(Board(x) for x in data[1:])

    print('Part 1:', play_bingo(input_numbers, input_boards))
    print('Part 2:', play_update_bingo(input_numbers, input_boards))
