from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

motor1 = board.get_pin("d:9:o")
motor2 = board.get_pin("d:10:o")

def clockwise():
    motor1.write(1)
    motor2.write(0)
def counterclockwise():
    motor2.write(1)
    motor1.write(0)
while True:
    clockwise()
    time.sleep(1)
    counterclockwise()
    time.sleep(1)
board.exit()
