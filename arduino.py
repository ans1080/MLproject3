# Arduino Test Program

# Imports
import pyfirmata
from time import sleep
import numpy as np

class Arduino:
    """
    Class for running the Arduino
    """
    def __init__(self):
        """
        Initializes the arduino class
        """

    # Create a function that grabs relevant data and returns the new row
    def output(self, score):
        """
        Sends output signals to the arduino
        Input: score: list, the 3-item percentage classification of the picture
        Ouput: none: buzzer and LED high/low output
        """
        import numpy as np

        # Initialize the board
        board = pyfirmata.Arduino('COM4')
        
        # Change score into a string
        label = {0: 'Defect 1', 1: 'Defect 2', 2: 'Normal'}
        score = label[np.argmax(score)]

        # Normal Output
        if score == 'Normal':
            board.digital[12].write(1)
            sleep(3)
            board.digital[12].write(0)

# board.digital[12].write(1)
# sleep(5)
# board.digital[12].write(0)
# board.digital[8].write(1)
# sleep(1)
# board.digital[8].write(0)

# for x in range(0, 25):
#     board.digital[13].write(1)
#     sleep(0.1)
#     board.digital[13].write(0)
#     sleep(0.1)
#     x = x + 1 
