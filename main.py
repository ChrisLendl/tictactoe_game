"""a simple tic tac toe game"""

#hi, I modified this file through a simple comment

def char_to_printable(cell):
    """if field state is like initialisation: " ", if not return X or O"""

    if cell == 0:
        return " "

    if cell == 1:
        return "X"
    return "O"


class GameBoard:
    """Gameboard state definition, turn checks and Gameboard graphical output"""
    def __init__(self):
        self.state = [0] * 9

    def make_turn(self, cell, player):
        """check if player has made valid turn"""
        if self.is_valid_turn(field):
            self.state[cell] = player.symbol
            return True
        return False

    def is_valid_turn(self, cell):
        """turn is valid if a player filled out the field """
        x_test = bool(self.state[cell] == 0)
        return x_test

    def check_win(self, player):
        """what combinations does it take to win game?"""
        p_s = player.symbol
        if self.state[0] == p_s and self.state[1] == p_s and self.state[2] == p_s:
            return True
        if self.state[3] == p_s and self.state[4] == p_s and self.state[5] == p_s:
            return True
        if self.state[6] == p_s and self.state[7] == p_s and self.state[8] == p_s:
            return True

        if self.state[0] == p_s and self.state[3] == p_s and self.state[6] == p_s:
            return True
        if self.state[1] == p_s and self.state[4] == p_s and self.state[7] == p_s:
            return True
        if self.state[2] == p_s and self.state[5] == p_s and self.state[8] == p_s:
            return True

        if self.state[0] == p_s and self.state[4] == p_s and self.state[8] == p_s:
            return True
        if self.state[2] == p_s and self.state[4] == p_s and self.state[6] == p_s:
            return True
        return False

    def is_full(self):
        """check if is already full"""
        for i in self.state:
            if i == 0:
                return False
        return True

    def print_game_board(self):
        """print 9 separate fields"""
        print(" " + char_to_printable(self.state[0]) + " | " +
              char_to_printable(self.state[1]) + " | " +
              char_to_printable(self.state[2]) + " \n" +
              " " + char_to_printable(self.state[3]) + " | " +
              char_to_printable(self.state[4]) + " | " +
              char_to_printable(self.state[5]) + " \n" +
              " " + char_to_printable(self.state[6]) + " | " +
              char_to_printable(self.state[7]) + " | " +
              char_to_printable(self.state[8]) + " \n")


class Player:
    """initialising players"""
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(2)
    board = GameBoard()
    act_player = player_a
    while not board.is_full():
        board.print_game_board()
        try:
            field = int(input("Where do you want to place your sign? [1-9]"))
        except ValueError:
            continue
        field = field - 1
        if field < 0 or field > 8:
            print("Please enter a number between 1 and 9")
            continue
        if not board.make_turn(field, act_player):
            print("Invalid Move")
            continue
        if board.check_win(act_player):
            print("You won!")
            break

        if act_player == player_a:
            act_player = player_b
        else:
            act_player = player_a
