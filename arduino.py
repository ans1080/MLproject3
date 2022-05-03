# Arduino Test Program

# Imports
import pyfirmata
from time import sleep
import numpy as np
import serial

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
        # Initialize the board
        board = pyfirmata.Arduino('COM12')
        
        # Change score into a string
        label = {0: 'Defect 1', 1: 'Defect 2', 2: 'Normal'}
        score = label[np.argmax(score)]

        # Normal Output
        if score == 'Normal':
            board.digital[12].write(1) # 12 = Green
            sleep(3)
            board.digital[12].write(0)
            board.sp.close()

        # Defect 1 Output
        if score == 'Defect 1':
            board.digital[11].write(1) #11 = Red
            board.digital[8].write(1) # 8 = Buzzer
            sleep(3)
            board.digital[11].write(0)
            board.digital[8].write(0)
            board.sp.close()
        
        # Defect 2 Output
        if score == 'Defect 2':
            for x in range(15):
                board.digital[9].write(1) # = Blue
                sleep(0.1)
                board.digital[9].write(0)
                sleep(0.1)
            board.sp.close()
