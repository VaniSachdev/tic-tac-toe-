
 
 How to Play:
 O. Uncomment menu() at the bottom of the file to begin playing 
 1. Always use CAPITAL LETTERS when asked for input 
 2. When deciding where to put your game pieece make sure to have it formatted CAPITAL LETTER + Number (ex: A1 NOT a1 or 1A). If you mess up it will prompt you to try again. 
 The goal is to win 3 rounds of tic tac toe; as you progress through the game you will be able to view how many games X and O have won as well as how many rounds it took for you to win! 


This is a functional game of tic tac toe in three seperate modes:
0. Person v Person 
1. Person v AI 
2. AI v AI (This is an easter egg! When asked to select A or B at the start of the game, type in 42!)

While it would have been easier to have a board labeled like the design below, I thought it would be hard for the user to decide where they wanted to place their next move since it is difficult to gain a holistic view of where the free (blank) spaces are. So, I implemeneted an alphanumeric board (kind of akin to a chess board) to provide an optimized experience for the user. It was a little difficult to implement until I remembered dictionaries existed! I needed to write more helper functions to "convert" my alphanumeric stirngs into integers, but all in all it wasn't too bad. 


1 | 2 | 3
----------
4 | 5 | 6
----------
7 | 8 | 9
----------

Between my milestone and final iteratoin, I made an AI that was "too smart"; it only won or tied games. So, I stuck with an AI that won/blocked when it could and made a random move otherwsie. At first I made the AI put its first piece in the middle of the board if free, but this also made it "too smart" when playing against each other/ if the computer got the first move. I wanted to make sure that regardless of the gameplay option selected the algorithms weren't too biased in selecting a winner. So, I stuck with the AI that was just the right amount of dumb. 

If I had more time I would try to make a 3 by 3 board; I think I have most of the base methods complete, and it would be more debugging than actual code writing. I also wanted to be able to save the outputs of each game to a text file so that users could have a "receipt" of their game. I tried to do this, but there were a lot of bugs. 

Notes:
 * MAKE SURE TO HAVE TERMCOLOR (TO INSTALLL TYPE PIP INSTALL TERMCOLOR IN TERMINAL)
 ** I rec the "Solarized Light" color palette on VS Code for the most aesthetic gameplay experience 

 final.py
 Download
#Name: Vani Sachdev 
# CS5 Gold Fall 

#make sure to pip install termcolor ! 


import random 
import time
from termcolor import colored

class Board:
    def __init__(self):
        """ input: n/a
            return: n/a 
            goal: initalizes the empty board """
        self.data = [[" "," ", " "],[" ", " ", " "],[" ", " ", " "]]
 
    def __repr__(self):
        """input: n/a
            return: a string (s) 
            goal:prints the board in the desired 3 by 3 format """ 
        data = self.data 
        s  = ''
        r_data = len(data)
        c_data = len(data[0])
        
        x_directions = ['A', 'B', 'C']
        y = 0
        
        for letter in range(0, len(x_directions)):
            x = x_directions[letter] 
            s +=  "  " + colored(x, "blue") + " "
        s += '\n' 
    
        for row in range(r_data):
            for col in range(c_data):
                if col == 0:
                    s += colored(str(y), "blue") + " "
                    y += 1 
                if col != 2:
                    s += data[row][col] + " | "
                else: 
                    s += data[row][col] 
          
            s += '\n'
            if row != 2:
                s += (4* c_data) * '-' 
                s += '\n'    
        return s 
 
    def row_and_col(self, move):
        """ input: move, alphanumeric string 
            return: row (int) & col (int)
            goal: converts the alphanumeric move inro its rows and columns """ 


        l_col = move[0]
        
        row = int(move[-1])
    
        col_dict = {
            "A": 0,
            "B": 1,
            "C": 2
            }

        col = col_dict.get(l_col, 4) # returns 4 if the col isnt in the range (so it does not error out)
        return row, col 

    def addMove(self, move, ox):
        """ input: move, an alphanumeric string and ox, a character 
            return: n/a
            goal: adds a given move of the desired character (as given by ox)) """ 
        
        row, col = self.row_and_col(move)
        if self.data[row][col] == " ":
            self.data[row][col] = ox 

    def valid_input(self, move):
        """ input: move, an alphanumeric string 
            return: n/a 
            goal: checks to see if the format of an input is valid """
        if len(move) != 2 or type(move[0]) or type(move[-1]):
            return False
        return True 

    def valid_move(self, move):
        """ input: move, an alphanumeric string 
            return: boolean (T if move is valid, F if it is not a valid move)
            goal: checks to see if a move is valid """ 
        data = self.data
        try:
            row, col = self.row_and_col(move)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if data[row][col] == " ":
                    return True
            return False
        except ValueError:
            return False

    def horizontal_win(self, ox, color = False):
        """ input: ox, a character, and an optional boolean (set to false) 
            return: boolean 
            checks for horizontal wins """

        #boolean is optional so that when the ai checks each win the color of the board doesn't become green 
        data = self.data 
        for row in range(3):
            if data[row][0] == ox and data[row][1] == ox and data[row][2] == ox:
                if color:
                    data[row][0] = colored(data[row][0], "green")
                    data[row][1] = colored(data[row][1], "green")
                    data[row][2] = colored(data[row][2], "green")  
                return True 
        return False 

    def vertical_win(self, ox, color = False):
        """ input: ox, a character, and an optional boolean (set to false) 
            return: boolean 
            checks for vertical wins """ 

        #boolean is optional so that when the ai checks each win the color of the board doesn't become green 

        data = self.data 
        for col in range(3):
            if data[0][col] == ox and data[1][col] == ox and data[2][col] == ox:
                if color:
                    data[0][col] = colored(data[0][col], "green")
                    data[1][col] = colored(data[1][col], "green")
                    data[2][col] = colored(data[2][col], "green")  
                return True 
        return False 
    
    def diagonal_win(self, ox, color = False):
        """ input: ox, a character, and an optional boolean (set to false) 
            return: boolean 
            checks for diagonal wins """ 

        #boolean is optional so that when the ai checks each win the color of the board doesn't become green 
        data = self.data 
        if data[0][0] == ox and data[1][1] == ox and data[2][2] == ox:
            if color:
                data[0][0] = colored(data[0][0], "green")
                data[1][1] = colored(data[1][1], "green")
                data[2][2] = colored(data[2][2], "green") 
            return True

        if data[0][2] == ox and data[1][1] == ox and data[2][0] == ox:
            if color:
                data[0][2] = colored(data[0][2], "green")
                data[1][1] = colored(data[1][1], "green")
                data[2][0] = colored(data[2][0], "green") 
            return True 
              

    def win(self, ox, color = False):
        """ input: ox, a character, and an optional boolean (set to false) 
            return: boolean 
            checks for wins in all directions """ 

        #boolean is optional so that when the ai checks each win the color of the board doesn't become gree
        if self.diagonal_win(ox, color) or self.horizontal_win(ox, color) or self.vertical_win(ox, color):
            return True
        return False

    def full_board(self):
        """ input: n/a
            output: boolean
            goal: checks to see if the board is full """
        full = 0 
        data = self.data
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == " ":
                    full = -1 
        if full == 0:
           return True
        else:
            return False  

    def set_board(self, string):
        """ input: string (a string)  
            return: n/a:
            goal: a series of moves are placed on the board (more for testing) """
        ox = "X"
        string = [move for moves in string for move in moves.split(",")] #basically splits the list of moves into an array consisting of its individual components 
        for i in range(len(string)): 
            if self.valid_move(string[i]): #if the move is valid 
                self.addMove(string[i], ox) #it is added to the board 
            if ox == "X": #so that the board switches move 
                ox = "O"
            elif ox == "O":
                ox = "X"
            
    def clear_board(self):
        """ input: n/a
            return: n/a 
            goal: clears the board (more for testing) """
        self.__init__() 

    def del_move(self, move):
        """ input: n/a
            return: n/a 
            goal: clears the board (more for testing) """
        data = self.data
        row, col = self.row_and_col(move)
        data[row][col] = " "


    def move_win(self, ox):
        """ input: ox, a character
            return: an array, win_pos
            goal: determines all the postions a player with chatacer ox can make to win"""
        win_pos = []
        free = self.free_moves()
        for x in free:
            self.addMove(x, ox) 
            if self.win(ox):
                win_pos.append(x)
            self.del_move(x)  
        return win_pos

    def free_moves(self):
        """ input: n/a 
            return: free_spaces, an array 
            goal: return an array that has all the moves for all the empty spaces left on the board"""


        data = self.data

        #converts each col to a character 
        
        rev_col_dict = {
            0 : "A",
            1: "B",
            2: "C"
            }

        free_spaces = [ ]

        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == " ": #if free space 
                    s_row = str(row)       
                    s_col = rev_col_dict[col]
                    move = s_col + s_row #convert into alphanumeric string 
                    free_spaces.append(move)  #and append it to the array 
        return free_spaces

    def ai_move(self, ox):
        """ input: ox, a character
            return: move, an alphanumeric string 
            goal: the ai makes a move depending on if it can win/its opponent will win in the next move 
            if neither, the ai makes a random move """

        if ox == "X":
            opp = "O"
        else:
            opp = "X"

        ai_win = self.move_win(ox)
        ai_protect = self.move_win(opp)

        # print(ai_win, ai_protect)

        if len(ai_win) > 0:
            move = random.choice(ai_win)  
            # print("win!")  
        else:
            if len(ai_protect) > 0:
                move = random.choice(ai_protect)
                # print("protec")
            else:
                move = random.choice(self.free_moves())
                # print ("idle")
        # print(move)
        return move


    # i implemented a minimax algorithm for the ai that was mostly woking but it was too smart :( and that was sad 
    # (it either won or tied and that is a boring user experience !)
    # life lesson: being fair > being smart (or fun game >>>> lol)

    # def change_player(self, player):
    #     """
    #     input: player (character)
    #     return player (characer)
    #     goal: returns the opposite player (if x return o, if o return x )
    #     """
    #     if player == "X":
    #         player = "O"
    #     else:
    #         player = "X"
    #     return player 
 
 
    # def minimax(self, board, depth, ox):
    #     """
    #     input: board (the board), depth (int), ox (character)
    #     return: best_value (int)
    #     goal: analyze every game state & pick the best one (when it is o's turn)
    #     (the ai in the 1v1 game is always only o)
    #     Recursively analyze every possible game state and choose
    #     the best move location.
    #     """

    

    #     if depth == 0 or board.full_board():
    #         if board.win(opp) == True:
    #             return 0
    #         elif board.win(player) == False:
    #             return 10
    #         else:
    #             return 5

    #     if player == "X":
    #         best_value = 0
    #         for move in board.free_moves():
    #             board.add_move(move, player)
    #             move_value = self.minimax(board, depth-1, self.change_player(player))
    #             board.add_move(move, " ")
    #             best_value = max(best_value, move_value)
    #         return best_value
        
    #     if player == "O":
    #         best_value = 100
    #         for move in board.free_moves():
    #             board.add_move(move, player)
    #             move_value = self.minimax(board, depth-1, self.change_player(player))
    #             board.add_move(move, " ")
    #             best_value = min(best_value, move_value)
    #         return best_value   

       

    def host_game(self):
        """ input: n/a 
            return: the character of the winner & the number of rounds it took to win 
            goal: hosts a 1v1 game """ 
        print(colored("welcome to tic tac toe, 2-player edition! may the best human win!", "green"))
        print("MOVES SHOULD BE LETTER NUMBER (EX: A1, B2, etc) ")
        print(self)
        game = 1 
        move = "Z1"
        turn = 0 
        x_win = 0
        o_win = 0 
        draw = 0 
        while game == 1:
            print(colored("--Round: " + str(x_win + o_win + draw) + "--", "magenta"))
            print(colored("X:"+ str(x_win) + "   O:" + str(o_win), "green"))
            
            while not self.valid_input(move) and not self.valid_move(move):
                if turn%2 == 0:
                    move = input("X\'s turn: ")
                    char = "X"
                else:
                    move = input("O\'s turn: ")
                    char = "O"

            self.addMove(move, char)

            if self.win("O", True):
                print(self)
                print (colored("O wins!", "green"))
                o_win += 1 
                if o_win < 3:
                    self.__init__()
                else:
                    game = 0 
                    total = draw+o_win+x_win 
                    return "O", total  
                
            elif self.win("X", True):
                print(self)
                print (colored("X wins!", "green"))
                x_win += 1
                if x_win < 3:
                    self.__init__()
                else:
                    game = 0  
                    total = draw+o_win+x_win 
                    return "X", total 

            elif self.full_board():
                print(self)
                print(colored("the board is full :(", "red"))
                self.__init__()
                draw += 1 
            if game == 1:    
                turn +=1
                move = "Z1"
                print (self)


    def host_game_ai(self):
        """input: n/a 
            return: the character of the winner & the number of rounds it took to win 
            goal: hosts a computer vs ai game """

        print(colored("welcome to tic tac toe, 1-player edition! may the best human/computer win!", "green"))
        print("MOVES SHOULD BE LETTER NUMBER (EX: A1, B2, etc) ")
        print(self)
        game = 1 
        move = "Z1"
        turn = 0 
        x_win = 0
        o_win = 0 
        draw = 0  
       
        while game == 1:
            print(colored("--Round: " + str(x_win + o_win + draw) + "--", "magenta"))
            print(colored("X:"+ str(x_win) + "   O:" + str(o_win), "green"))
            
            while not self.valid_input(move) and not self.valid_move(move):
                if turn%2 == 0:
                    move = input("X\'s turn: ")
                    char = "X"
                else:
                    char = "O"
                    move = self.ai_move(char)
                    print("O\'s turn: " + move)
                    time.sleep(1)
                 

            self.addMove(move, char)

            if self.win("O", True):
                print(self)
                print (colored("O wins!", "green"))
                o_win +=  1 
                if o_win < 3:
                    self.__init__()
                else:
                    game = 0 
                    total = draw+o_win+x_win 
                    return "O", total 
                
            elif self.win("X", True):
                print(self)
                print (colored("X wins!", "green"))
                x_win +=  1 
                if x_win < 3:
                    self.__init__()
                else:
                    game = 0  
                    total =  total = draw+o_win+x_win  
                    return "X", total 
           
            elif self.full_board():
                print(self)
                print(colored("the board is full :(", "red"))
                self.__init__()
                draw += 1 
              
             
            if game == 1:    
                turn +=1
                move = "Z1"
                print (self)


    def host_game_ai_ai(self):
        """ input: n/a 
            return: the character of the winner & the number of rounds it took to win 
            goal: hosts an ai vs ai game """ 


        print(colored("welcome to tic tac toe, 1-player edition! may the best human/computer win!", "green"))
        print(self)
        game = 1 
        move = "Z1"
        turn = 0 
        x_win = 0
        o_win = 0 
        draw = 0 



        while game == 1:
            print(colored("--Round: " + str(x_win + o_win + draw) + "--", "magenta"))
            print(colored("X:"+ str(x_win) + "   O:" + str(o_win), "green"))
            
            while not self.valid_input(move) and not self.valid_move(move):
            
                if turn%2 == 0:
                    char = "X"
                    move = self.ai_move(char)
                    print("X\'s turn: " + move)
                    time.sleep(1)
                else:
                    char = "O"
                    move = self.ai_move(char)
                    print("O\'s turn: " + move)
                    time.sleep(1)
                    
                 

            self.addMove(move, char)

            if self.win("O", True):
                print(self)
                print (colored("O wins!", "green")) 
                o_win +=  1 
                if o_win < 3:
                    time.sleep(1)
                    self.__init__()
                else:
                    game = 0
                    total = draw+o_win+x_win  
                    return "O", total 
                
            elif self.win("X", True):
                print(self)
                print (colored("X wins!", "green"))
                x_win +=  1 
                if x_win < 3:
                    time.sleep(1)
                    self.__init__()
                else:
                    game = 0 
                    total = draw+o_win+x_win   
                    return "X", total 

            elif self.full_board():
                print(self)
                print(colored("the board is full :(", "red"))
                self.__init__()
                draw += 1 
            if game  == 1:    
                turn +=1
                move = "Z1"
                print (self)





def menu():

    """ no input/retirn 
    goal: acts as the main function (starts the game) """

    x = Board()
    print (colored(" welcome to tic tac toe!", "green"))
    print("the goal of this game is to win 3 games!")
    print("how many players are with us today?")
    p_num = "invalid"

    option_a = colored("A for two players ", "green")
    option_b = colored("B for one player ", "green")

    start = False
    

    while p_num != 'A' or  p_num != 'B':
        if start:
            break
        p_num = input("please respond with " + option_a + "or " + option_b)
        if p_num == 'A':
            start = True 
            winner, total = x.host_game()
            print (colored("\n andddddd the winner after " + str(total) + " rounds is: "+ winner +"!", "blue"))
            
        elif p_num == 'B':
            start = True 
            winner, total = x.host_game_ai()
            print (colored("\n andddddd the winner after " + str(total) + " rounds is: "+ winner +"!", "blue"))
        elif p_num == "42":
            start = True 
            print(colored("you work too hard -- get yourself some tea, snuggle into your blankets, and watch two ai's batttle it out!", "blue"))
            time.sleep(3)
            winner, total = x.host_game_ai_ai()
            print (colored("\n andddddd the winner after " + str(total) + " rounds is: "+ winner +"!", "blue"))
        else:
            print(colored("that was not a valid entry :( please try again!", "red"))


#UNCOMMENT MENU() TO START GAME 
# menu()



# # tests 
# x = Board()
# # x.host_game()

# z = ["AO", "C0", "C0", "B0", "B1", "B2", "C1", "C2"]
# x.set_board(z)
# print(x)

# y = x.dumb_ai_move("O")
# print(y)


# x.del_move("B1")
# print(x)
# print(x.full_board())
