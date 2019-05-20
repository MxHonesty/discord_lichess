import chess
import serial

board = chess.Board()

#print (board.legal_moves)

def check_legal(board, move):
    if (chess.Move.from_uci(move) in board.legal_moves):
         return True

def commit_move(board, move):
    if(check_legal(board, move) == True):
        board.push(chess.Move.from_uci(move))

def serial_data(port, baudrate):
    s = serial.Serial(port, baudrate, timeout = 60)

    line = s.readline()
    s.close()
    return line
