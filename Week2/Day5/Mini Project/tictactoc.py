won = False
is_player_x = True

def play():
    print("welcome to TIC TAC TOE")
    display_board()
    player_input('x')
    display_board()
    player_input('o')
    display_board()
    

board =[
    ["","",""],
    ["","",""],
    ["","",""]
    
]



def display_board():
    print("TIC TAC TOE")
    print("***************")
    print("* {}   | {}  | {}  *".format(board[0][0], board[0][1], board[0][2]))
    print("* ---|---|--- *")
    print("*  {}  | {}  | {}  *".format(board[1][0], board[1][1], board[1][2]))
    print("* ---|---|--- *")
    print("*  {}  | {}  | {}  *".format(board[2][0], board[2][1], board[2][2]))
    print("***************")




def player_input(player):
    print("player {}'s turn".format(player))
    input_row = input('Enter row: ')
    input_col = input('Enter col: ')
    
    row = int(input_row)
    col = int(input_col)
    
    if board[row][col] == "":
        board[int(row) - 1] [int(col) - 1] = player
    else:
        print("This have already been played")

    
    



def check_win():
    raise NotImplementedError()

play() 

