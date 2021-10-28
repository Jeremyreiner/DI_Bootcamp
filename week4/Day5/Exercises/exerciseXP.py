
ttT_board = {
    '1': '', '2': '', '3': '',
    '4': '', '5': '', '6': '',
    '7': '', '8': '', '9': '',
}
board_key = []
for key in ttT_board:
    board_key.append(key)

def print_board(board):
    print("*"*13)
    print("|" + " " + board['1'] + (" |" + " ") + board['2'] + (" |" + " ")  + board['3'] + " " + "|")
    print("-"*13)
    print("|" + " " + board['4'] + (" |" + " ") + board['5'] + (" |" + " ")  + board['6'] + " " + "|")
    print("-"*13)
    print("|" + " " + board['7'] + (" |" + " ") + board['8'] + (" |" + " ")  + board['9'] + " " + "|")
    print("-"*13)

print('''Welcome to tic tac toe. Player 1 will be player X,
and player 2 will be player O. Please instruct which square you will place your 
player value. IE first row will be 1, 2, 3 and last row will be 7, 8, 9.
Good luck!
''')

def play_game():
    turn = "X"
    count = 0

    for i in range(10):
        print_board(ttT_board)
        print(f"Its your turn {turn}. Where would you like to move? ")
        move = input()

        if ttT_board[move] == '':
            ttT_board[move] = turn
            count += 1
        else: 
            print(f"Your move {move} has already been selected. Chose another spot")
            continue
        if count >= 5:
            if ttT_board['1'] == ttT_board['2'] == ttT_board['3'] != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Best row to win!")
                break

            
            elif ttT_board['4'] == ttT_board['5'] == ttT_board['6']  != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Well la di da, Great Win!")
                break
            
            elif ttT_board['7'] == ttT_board['8'] == ttT_board['9']  != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Like stealing candy from a baby.")
                break
            
            elif ttT_board['1'] == ttT_board['4'] == ttT_board['7']  != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Could've done better...")
                break
            
            elif ttT_board['2'] == ttT_board['5'] == ttT_board['8']  != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Horrible way to win...")
                break
            
            elif ttT_board['3'] == ttT_board['6'] == ttT_board['9']  != '':
                print_board(ttT_board)
                print(f"\n Game over..\n {turn} won!! Took you long enough...")
                break
            
            elif ttT_board['1'] == ttT_board['4'] == ttT_board['9']  != '':
                print_board(ttT_board)
                print("\n Game over..\n")
                print(f"{turn} won!! Bloody hell harry...")
                break
            elif count == 9:
                print_board(ttT_board)
                print("\nGAME OVER\n" + "Welp.. I guess nobody lost")
                break



        if turn == "X":
            turn = "O"
        else:
            turn = "X"

play_game()


