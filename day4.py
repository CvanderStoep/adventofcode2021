def read_input_file():
    # This is day4 part 1
    rows, cols = (5, 5)
    bingo_balls = []
    bingo_board_numbers = []
    filename = "input4test.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    for index, line in enumerate(content):
        if index == 0:
            bingo_balls = line.split(',')
            bingo_balls = list(map(int, bingo_balls))
            continue

        if line != "":
            bingo_board_numbers.append(list(map(int, line.split())))

    number_of_bingo_boards = int(len(bingo_board_numbers) / rows)
    bingo_boards = []

    for i in range(number_of_bingo_boards):
        card_numbers = bingo_board_numbers[rows * i:rows * i + cols]
        bingo_boards.append(Board(card_numbers))

    for board in bingo_boards:
        board.print_board()

    for bingo_ball in bingo_balls:
        for board in bingo_boards:
            board.check_number(bingo_ball)
            if not board.bingo:
                bingo = board.check_bingo()
                if bingo:
                    print(f'final score: {board.calculate_score()}')


class Board:
    def __init__(self, board, rows=5, cols=5):
        self.board = board
        self.rows = rows
        self.cols = cols
        self.bingo = False

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def check_number(self, number):
        self.number = number
        for i in range(self.rows):
            for j in range(self.cols):
                if self.number == self.board[i][j]:
                    self.board[i][j] = -1

    def check_bingo(self):
        for row in self.board:
            bingo = all(elem == -1 for elem in row)
            if bingo:
                print('bingo', self.number)
                self.bingo = True
                self.print_board()
                return True

        columns = [[], [], [], [], []]
        for i in range(self.cols):
            for j in range(self.rows):
                columns[i].append(self.board[j][i])

        for column in columns:
            bingo = all(elem == -1 for elem in column)
            if bingo:
                print('bingo', self.number)
                self.bingo = True
                self.print_board()
                return True

        return False

    def calculate_score(self):
        score = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1:
                    score += self.board[i][j]

        print(score, self.number)
        return score * self.number


if __name__ == '__main__':
    read_input_file()
