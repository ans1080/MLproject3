# Arduino Test Program
import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM4')

board.digital[12].write(1)
sleep(5)
board.digital[12].write(0)
board.digital[8].write(1)
sleep(1)
board.digital[8].write(0)

for x in range(0, 25):
    board.digital[13].write(1)
    sleep(0.1)
    board.digital[13].write(0)
    sleep(0.1)
    x = x + 1 
