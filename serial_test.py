import serial
from chess_engine import is_move


# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = 'COM3'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600


def read():
    wait = True
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while (wait == True):
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        wait = False
        return(reading.replace('m', ''))

if __name__ == "__main__":
    print(read())
