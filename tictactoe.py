

reset_board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

class Game:
    def __init__(self):
        #initialize variables
        self.scores = {'P1': 0, 'P2': 0}
        self.board = [[1,2,3],
                      [4,5,6],
                      [7,8,9]]
        self.players = {'P1': 'X', 'P2': 'O'}

    def player_won(self, player):
        """
        Description:
            A player wins thus its score rises

        Args:
            player(str): "P1" or "P2" who wins

        Returns:
            none: Returns none
            
        """
        if player in self.players:    
            self.scores[player] += 1
            print('%s Wins!!!' % player)
            return 1
        return 0

    def check_won(self, player):
        """
        Description:
            Checks if a player wins the match

        Conditions:
            Return 1    Horizontal: If any row is all "X" or "O"
            Return 1    Vertical: If any column is all "X" or "O"
            Return 1    Diagonal: If any 3 places marked "X" or  "O" diagonally (ex: Top left corner to bottom right corner)
            Return 0    If none of this happens

        Args:
            player(str): "P1" or "P2" player variable
        
        Returns:
            Boolean(0 or 1): If statemant is true returns 1 otherwise returns 0

        """

        # Check diagonal win
        # top left to bottom right
        if self.board[0][0] == self.players[player] and self.board[1][1] == self.players[player] and self.board[2][2] == self.players[player]:
            return 1
        
        # top right to bottom left
        if self.board[0][2] == self.players[player] and self.board[1][1] == self.players[player] and self.board[2][0] == self.players[player]:
            return 1
        

        for i in range(3):
            # check horizontal win
            if self.board[i].count(self.players[player]) == 3:
                return 1
            
        # check vertical win
        for i in range(3):
            if self.board[0][i] == self.players[player] and self.board[1][i] == self.players[player] and self.board[2][i] == self.players[player]:
                return 1
            
            
        return 0

    def display_game(self):
        """
        Description: 
            Displays current game board in a command line
        
        Returns:
            none: Returns none.
        """
        for row in self.board:
            row_text = ''
            for column in row:
                row_text += str(column) +' '
            print(row_text)

    def display_coordinate(self, coordinate):
        """
        Description:
            Returns the mark from spesified coordinate

        Args:
            coordinate(dictionary): ex: {'x': 0, 'y': 0} is first column in first row

        Returns:
            str or int: If place is never touched it returns int ex: 1 First column in first row
                        If coordinate is marked returns str ex: "X" as P1's mark
        """
        if 'x' in coordinate and 'y' in coordinate:
            if -1 < coordinate['x'] < 3 and -1 < coordinate['y'] < 3:
                word = self.board[coordinate['y']][coordinate['x']]
                return word
        return 0

    def get_coordinate(self, place):
        """
        Description:
            Returns coordinate(dict) from clients' str input

        Args:
            place(str): place where to get coordinate from (1-9 str) (usually players' input)

        Returns:
            dict: coordinates got from the place where client requested ex:{'x': 0, 'y': 0}
        
        """
        try:
            place = int(place) - 1
        except ValueError:
            return 0
        if -1 < place < 9:
            x = place % 3
            y = place // 3
            coordinate = {'x': x, 'y': y}
            return coordinate
        
        return 0

    def place(self, player, place):
        '''
        Place player's mark (X or O) on the game board where player chooses

        Args:
            player(str): Player who makes the move (P1 or P2)
            place(str): Place where mark should be placed

        Returns:
            bool: True if successful False otherwise.
        '''

        # if player is in players and place is valid and free
        # then place the mark for spesified place
        # else return 0

        if player in self.players:
            coordinate = self.get_coordinate(place)
            if coordinate:
                mark = self.display_coordinate(coordinate)
                try:
                    mark = int(mark)
                except ValueError:
                    return 0
                if 0 < mark < 10:
                    self.board[coordinate['y']][coordinate['x']] = self.players[player]
                    return 1
        return 0
    
    def play_game(self, tour_limit = 1):
        """
        Description:
            play the game as long as tour variable
        
        Args:
            tour(int): default 1 as tours should be played
        
        Workflow Diagram:
            1- Start
            2- Display scores
            3- check if tour == tours then finish otherwise continue
            4- Display game situation
            5- ask player1 where to mark
            6- if place() returns False go to 3 if True continue
            7- if check_won returns True give P1 a point and go 3 otherwise continue
            8- display game sit.
            9- ask player2 where to mark
            10- if place() returns False go to 6 if True continue
            11- if check_won returns True give P2 a point and go 3 otherwise continue
            12- display game sit.
            13- go to 5
        
        """
        print(self.scores)
        
        for tour in range(tour_limit):
            print(f"\nRound {tour + 1}")
            self.display_game()

            next_game = 0
            
            while next_game == False:
                for player in self.players:
                    while True:
                        player_input = input(f"{player}, enter your move: ")
                        if self.place(player, player_input):
                            break
                        else:
                            print("Invalid move. Please try again.")
                    self.display_game()
                    if self.check_won(player):
                        self.player_won(player)
                        print(self.scores)
                        self.display_game()
                        next_game = True
                        self.board = reset_board
                        break  # If someone wins, end the round early
            
            # Check if the game is over
            if self.scores['P1'] + self.scores['P2'] == tour_limit:
                print("Game Over")
                break


if __name__ == '__main__':
    tours = input('Tour limit: ')
    gm = Game()
    gm.play_game(int(tours))