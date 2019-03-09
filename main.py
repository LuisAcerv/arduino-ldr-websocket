# import serial
import pyfirmata

PORT = '/dev/cu.usbmodem141101'

PIN = 0  # Pin 2 is used
DEL = 3  # A 3 seconds delay

# Creates a new board
board = pyfirmata.Arduino(PORT)
it = pyfirmata.util.Iterator(board)
it.start()

# Loop for blinking the led
while True:
    board.analog[PIN].enable_reporting()
    print(board.analog[PIN].read())
    board.pass_time(DEL)
    print(board.analog[PIN].read())
    board.pass_time(DEL)
