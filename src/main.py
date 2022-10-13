import Board
import random
import AI

gameBoard = Board.Board()
marks = ['X', 'O']
random.shuffle(marks)
current_player = marks[0]

print("Your mark is X \nThe board: \n")
gameBoard.print_board()
game_running = True
while game_running:
    if current_player == 'X':
        user_move = input("Enter a number: ")
        gameBoard.play_move(int(user_move) - 1, 'X')
        current_player = 'O'
    else:
        print("\nAI is thinking...")
        gameBoard.play_move(AI.best_move(board=gameBoard), 'O')
        print("AI move:")
        gameBoard.print_board()
        current_player = 'X'

    result = gameBoard.check_win()
    if result != "NO_END":
        # X only wins if an extraordinarily timed cosmic flare causes an untimely bit-flip
        print(f"Winner: {result} \nFinal board:")
        gameBoard.print_board()
        game_running = False
