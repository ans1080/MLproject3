### MLproject3 - Defective Part Extractor
#### Andy Snitgen and Jacob Henry

#### Purpose
<p>
  The purpose of the this program is to create and deploy a machine learning algorithm that can detect pictures of a specific machined part and correctly identify if they are defective or not.  Ideally, the input should come from a locally hosted flask app and the output will be displayed on the screen.  A stretch goal for the project is to use an arduino microcontroller in combination with the pyserial library to turn on a green led light if the part is normal.  The part can be defective in one of two ways.  The first way is a misaligned hole, and the part is a waste so a red led should light and a buzzer sound.  However, the second defect is not an entirely wasted part, just a dirty one that needs to be cleaned.  In that case the light should flash blue. </p>

#### Instructions for Local Arduino Use
* Load a terminal such as git bash
* Navigate to the directory where the project files are saved
* Use the command `flask run`
* The output should have a ip adress formatted as `http://127.0.0.1:5000/`
  * Copy this address into a web browser and load the page
* Click on `Choose File` and select an image of a part
* Click submit

#### Instructions for Heroku Cloud Web App
* Copy and paste the following link into a web browser: https://obscure-chamber-74940.herokuapp.com/
* Click on `Choose File` and select an image of a part
* Click submit
  * Note that even a plugged in Arduino will not function with the Online Version

#### Special Note
* The TensorFlow model saved in the `tensorflow` folder occasionally does not pull correctly from git hub
  * This causes a type error when the program is run
* If this error occurs, unpack the `tensorflow.zip` file and use it to overwrite the corrupted `tensorflow` folder

#### File Information
* data
  * This folder contains:
    * test_data folder with sub-folders containing test data in all 3 categories (normal, defect 1, defect 2)
    * train_data folder with sub-folders containing all training data seperated into each category
    * val_data folder with sub-folders containing organized copies of all the test data
    * defect_log, a csv containing a list of all the test and train data
* static
  * This folder contains all of the pictures run by the app in a temporary folder `tmp`
* templates
  * This folder contains two basic html web pages:
    * index, the homepage with options to load a picture and submit it
    * search_results, the results webpage that shows classification and confidence percentage
* tensorflow
  * This folder contains the files associated with a saved keras nueral model
* tensorflow 2
  * This folder contains the files associated with a second saved keras model
    * This is not used in the program, but proved useful in tuning the model
* app.py
  * This python file contains the code for the flask app used in local deployment
* arduino.py
  * This python file contains the code used to run the arduino
* model_creation.py
  * This file contains the code that creates the keras nueral network model
* requirements
  * This text file contains a list of packages necessary to run the application
* runtime
  * This text file contains a log of the python version needed to run the app
* test
  * This python file was used to test the arduino code without use of the app 
  * It is not currently used
