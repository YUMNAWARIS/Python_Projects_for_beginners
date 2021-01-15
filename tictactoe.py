
board = ["-", "-", "-" ,
         "-", "-", "-" ,
         "-", "-", "-"]
turn = "x"
move = 0
winner = None
draw = False


def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])


def play_game():
    global turn
    global move

    display_board()
    
    while True:

        try:
            a = int(input("Enter number 1-9: "))
            while board[a-1]!= "-":
                print("Already occupied. ")
                a = int(input("Enter again: "))

            board[a-1] = turn

        except:
            print("try valid inputs...")
            continue
        
        check_if_win()
        check_tie()

        if winner != None:
            display_board()
            print(winner , "wins")
            break
        elif draw == True:
            display_board()
            print("Tie!")
            break
        else:
            display_board()
            
        flip_turn()
        move += 1


def check_if_win():
    global winner
    row1 = board[0]== board[1]==board[2] != "-"
    row2 = board[3]== board[4]==board[5] != "-"
    row3 = board[6]== board[7]==board[8] != "-"

    col1 = board[0]== board[3]==board[6] != "-"
    col2 = board[1]== board[4]==board[7] != "-"
    col3 = board[2]== board[5]==board[8] != "-"

    diag1 = board[0]== board[4]==board[8] != "-"
    diag2 = board[2]== board[4]==board[6] != "-"
  

    if row1:
        winner = board[0]
    elif row2:
        winner = board[3]
    elif row3:
        winner = board[6]
    elif col1:
        winner = board[0]
    elif col2:
        winner = board[1]
    elif col3:
        winner = board[2]
    elif diag1 or diag2:
        winner = board[4]
    

def check_tie():
    global draw
    if winner == None and move == 8:
        draw = True
    return draw

def flip_turn():
    global turn 
    if turn == "x":
        turn = "o"
    else:
        turn = "x"


while True:
    play_game()
    b = input("Press any key to exit. ")
    if b != '':
        exit()
    else:
        exit()
    