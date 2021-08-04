# Game area / board

gamearea = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

gamearea_keys = []

for key in gamearea:
    gamearea_keys.append(key)

'''
function that prints the updated board after every move.
'''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# main function witch has the gameplay.


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(gamearea)
        print("your turn," + turn + ".Choose your move!")

        move = input()

        if gamearea[move] == ' ':
            gamearea[move] = turn
            count += 1
    # Checks if player choose allready occupied space
        else:
            print("Space allready occupied .\nChoose new move!")
            continue
        """
        checks if player X or O has won,for every move after 5 moves.
        checks row for row. verticaly and horizontaly
        """

        # Checks top row horizontal
        if count >= 5:
            if gamearea['7'] == gamearea['8'] == gamearea['9'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # Checks middle row horizontal
            elif gamearea['4'] == gamearea['5'] == gamearea['6'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # Checks bottom row horizontal.
            elif gamearea['1'] == gamearea['2'] == gamearea['3'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

            elif gamearea['1'] == gamearea['4'] == gamearea['7'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # Checks left row verticaly
            elif gamearea['1'] == gamearea['4'] == gamearea['7'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # checks middle row verticaly
            elif gamearea['2'] == gamearea['5'] == gamearea['8'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # checks right row verticaly
            elif gamearea['3'] == gamearea['6'] == gamearea['9'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # Checks diagonally
            elif gamearea['7'] == gamearea['5'] == gamearea['3'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        # checks other diagonal
            elif gamearea['1'] == gamearea['5'] == gamearea['9'] != ' ':
                printBoard(gamearea)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
    # Checks for a tie
        if count == 9:
            print("\nGame Over.\n")
            print("Tie")
            break
    # Changes player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
# After game over asks if players wants to play again or quit.
    restart = input("Another round?(y/n)")
    if restart == "y" or restart == "Y":
        for key in gamearea_keys:
            gamearea[key] = " "

        game()


if __name__ == "__main__":
    game()
