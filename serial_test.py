import serial
from chess_engine import is_move


# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = 'COM4'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

def read():
    wait = True
    while (wait == True):
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        move = reading.replace('m', '')
        move = move.replace(' ', '')
        print(move)
        if(is_move(move) == False):
            print('da')
            wait = False

#def send(data):
    #ser.write(data)

def send(data):
    data = data.encode()
    ser.write(data)
    pass

if __name__ == "__main__":
    send("ma8h1")
