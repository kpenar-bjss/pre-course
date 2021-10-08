import random

def print_board(board):
    #print('\n'*10)
    
    print( board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print( board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print( board[1] + '|' + board[2] + '|' + board[3])

def player_marker():
    
    marker = ''
    
#select the marker
    while marker != 'X' and marker != 'O':
        marker = input('choose X or O : ')
        
#define opposite side

    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1, player2)

#place marker on the bord
def place_move(board, marker, move):
    board[move] = marker

def win_check(board, mark):
     return ((board[1] == board[2] == board[3] == mark) or
     (board[4] == board[5] == board[6] == mark) or
     (board[7] == board[8] == board[9] == mark) or
     (board[7] == board[4] == board[1] == mark) or 
     (board[8] == board[5] == board[2] == mark) or 
     (board[9] == board[6] == board[3] == mark) or 
     (board[7] == board[5] == board[3] == mark) or 
     (board[9] == board[5] == board[1] == mark)) 

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, move):
    
    return board[move] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            False
#board is not full if False

#Board is full if true
    return True
    
def player_choice(board):
    move = 0
#ask player about the move
    while move not space_check(board, move) or not in range[1,10]:
        move = input('select move : ')

    return move

def replay():
    
    choice = input('play again? Enter Yes or No: ')

    return choice =='Yes'

#Game mechanics

print('Welcome to Tic Tac Toe!')

while True:
    #reset the board
    playBoard= [' ']*10
    player1_move, player2_move = player_input()
    # Set the game up here

    turn = 'Player 1'

    play_game = input('play? Enter y or n')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #show current board
            display_board(playBoard)
            #select move
            move= player_choice(playBoard)
            #place marker
            place_move(playBoard, player1_move, move)

            #check victory condition
            if win_check(playBoard, mark):
                print ('win player 1')
            else:
                if full_board_check(playBoard):
                    print('draw')
                    gameon=False
                else:
                    turn='Player 2'
        else:
            if turn == 'Player 2':
            #show current board
            display_board(playBoard)
            #select move
            move= player_choice(playBoard)
            #place marker
            place_move(playBoard, player1_move, move)

            #check victory condition
            if win_check(playBoard, mark):
                print ('win player 2')
            else:
                if full_board_check(playBoard):
                    print('draw')
                    gameon=False
                else:
                    turn='Player 1'

    if not replay():
        break

    
    