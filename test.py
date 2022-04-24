import numpy as np
from arduino import Arduino
from time import sleep

# Shared Dictionary & Arduino initialize
label = {0: 'Defect 1', 1: 'Defect 2', 2: 'Normal'}
arduino = Arduino()

# Test with Normal Picture
score = [0.07632941, 0.07632941, 0.8473412]
arduino.output(score)
score_string = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(label[np.argmax(score)], 100 * np.max(score))
print(score_string)

sleep(1)

# Test with Defect 1
score = [0.88215196, 0.01742122, 0.10042677]
arduino.output(score)
score_string = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(label[np.argmax(score)], 100 * np.max(score))
print(score_string)

sleep(1)

# Test with Defect 2
score = [0.00758621, 0.98482764, 0.00758621]
arduino.output(score)
score_string = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(label[np.argmax(score)], 100 * np.max(score))
print(score_string)