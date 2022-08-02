import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #using a single list represent a 3x3 table
        self.current_winner = None #keep track of anyone who wins

    def print_board(self):
        #trying to get the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|' .join(row) + '|')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        # return[]
       return [i for i, spot in enumerate(self.board) if spot == '']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move(assign square to letters)
        #then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        #winner if 3 in a row at any where, they all need to be checked
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #checking diagonal
        #only if the squares are even numbers
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #from left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #from right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

            #if all this checks fail
            return False


def play(game, x_player, o_player, print_game=True):
    #return the winner of a game(the letter), or none as tie
    if print_game:
        game.print_board_nums()

    letter = 'x' #first game letter
    #keep iterating while game is still on
    while game.empty_squares():
        #get the moves from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move[square, letter]:
            if print_game:
                print(letter + f'make a move to square {square}')
                game.print_board()
                print('')  #an empty line

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!!')
                return letter

            #after making moves, we need to alternate letters
            letter = 'o' if letter == 'x' else 'x'

        #tiny pause to reduce the speed
        time.sleep(0.7)

    if print_game:
        print('It\'s a tie!!')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

