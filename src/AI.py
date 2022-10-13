import math
import Board


def minimax(board: Board.Board, is_maximizing: bool):
    result = board.check_win()
    if result == 'TIE':
        return 0
    elif result == 'O':
        return 100
    elif result == 'X':
        return -100

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            current_cell = board.get_cell(i)
            if current_cell not in ['X', 'O']:
                board.play_move(i, 'O')
                best_score = max(minimax(board, not is_maximizing), best_score)
                board.play_move(i, current_cell)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            current_cell = board.get_cell(i)
            if current_cell not in ['X', 'O']:
                board.play_move(i, 'X')
                best_score = min(minimax(board, not is_maximizing), best_score)
                board.play_move(i, current_cell)
        return best_score


def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        current_cell = board.get_cell(i)
        if current_cell not in ['X', 'O']:
            board.play_move(i, 'O')
            score = minimax(board, False)
            board.play_move(i, current_cell)
            if score > best_score:
                best_score = score
                move = i
    return move
