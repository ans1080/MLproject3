### MLproject3 - Defective Part Extractor
#### Andy Snitgen and Jacob Henry

#### Purpose
<p>
  The purpose of the this program is to create and deploy a machine learning algorithm that can detect pictures of a specific machined part and correctly identify if they are defective or not.  Ideally, the input should come from a locally hosted flask app and the output will be displayed on the screen.  A stretch goal for the project is to use an arduino microcontroller in combination with the pyserial library to turn on a green led light if the part is normal, but sound a buzzer if it is defective. </p>

#### Instructions
* Load a terminal such as git bash
* Navigate to the directory where the project files are saved
* Use the command `flask run`
* The output should have a ip adress formatted as `http://127.0.0.1:5000/`
  * Copy this adress into a web browser and load the page
* Click on `Choose File` and select and image of a part
* Click submit
