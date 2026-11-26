class Game:
    def __init__(self):
        self.current_player = "X"
        self.board = [
            "", " ", " ",
            " ", " ", " ",
            " ", " ", " "
        ]
        print(self.board)

    def next_turn(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
