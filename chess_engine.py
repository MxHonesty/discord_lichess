import chess
import serial

#board = chess.Board()

#print (board.legal_moves)

def is_move(move):
    try:
        chess.Move.from_uci(move)
    except:
        return False

def check_legal(board, move):
    if (chess.Move.from_uci(move) in board.legal_moves):
         return True
    else:
        return False

def commit_move(board, move):
    if(check_legal(board, move) == True):
        board.push(chess.Move.from_uci(move))
        return "Move executed"
    elif(check_legal(board, move) == False):
        return "Move is not legal"


def serial_data(port, baudrate):
    s = serial.Serial(port, baudrate, timeout = 60)

    line = s.readline()
    s.close()
    return line
