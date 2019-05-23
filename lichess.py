import berserk
import threading
from chess_engine import is_move, check_legal, commit_move
import chess
import serial

TOKEN = "YedQUsAhQ5I6OeOE"

incepe = 0

session = berserk.TokenSession(TOKEN)
client = berserk.Client(session)

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = 'COM3'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

def should_accept(event):
    if(event['challenge']['challenger']['id'] == "honestymx"):
        return True

class Game(threading.Thread):
    def __init__(self, client, game_id, tura, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.tura = tura
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        print(game_state)
        move = game_state['moves'][-4:]
        commit_move(board, move)
        self.tura = self.tura+1

        if((self.tura%2) == 1):
            game.read()

    def read(self):
        wait = True
        if (wait == True):
            reading = ser.readline().decode('utf-8')
            print(reading)
            move = reading.replace('m', '')
            move = move.replace(' ', '')
            if(is_move(move) == False):
                client.bots.post_message(self.game_id, move)
                wait = False

    def handle_chat_line(self, chat_line):
        if chat_line['text'] == "stop":
            client.bots.resign_game(self.game_id)

        if chat_line['text'] == "ajutor":
            client.bots.post_message(self.game_id, 'Acesta este botul pentru tabla de sah. Comanda pentru oprierea meciului este "stop"')

        if not (is_move(chat_line['text']) == False):
            if(check_legal(board, chat_line['text']) == True):
                client.bots.make_move(self.game_id, chat_line['text'])
            elif(check_legal(board, chat_line['text']) == False):
                client.bots.post_message(self.game_id, "Mutare ilegala")
                game.read()
        pass


for event in client.bots.stream_incoming_events():
    if event['type'] == 'challenge':
        if should_accept(event):
            #print(event['challenge']['id'])
            if (event['challenge']['color'] == 'black'):
                incepe = 1
            elif(event['challenge']['color'] == 'white'):
                incepe = 0
            client.bots.accept_challenge(event['challenge']['id'])
        else:
            client.bots.decline_challenge(event['challenge']['id'])
    elif event['type'] == 'gameStart':
        #print(event)
        if (incepe == 1):
            game = Game(client, event['game']['id'], tura = 1)
            game.start()
            board = chess.Board()
            game.read()
        elif(incepe == 0):
            game = Game(client, event['game']['id'], tura = 0)
            game.start()
            board = chess.Board()
