Attendance Management System

Create a virtual environment on Windows using command:
            virtualenv venv
Activate the environment names "venv":
            ./venv/Scripts/activate            

1. First install all the required modules given in the requirements.txt using the command:
            pip install -r requirements.txt

2. If there is a dlib error due to the installation of face recognition module use the following command in the terminal:
        pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl

3.  MYSQL database can be accessed using the mysql workbench installed on the device.
The required credentials are :
username: root
password: test@123 

4. Important:  Create a new folder named image and a folder named data in your main folder if it doesn't already exist. These will contain the data set of the registered students ,that is their pictures for face recognition purposes.
Also create a csv file named attendance.
 
4. After the installations, run the python file named loginform.py. In the new window that appears you can login through an already registered username or create a new user and fill the form with the required information and go back the login window.

5. Login with the correct credentials and the attendance management system is opened in a new window.
Click on the student details button and register a new candidate and also update the already registered students in the record. 

5. The data set can also be uploaded without using a live web cam by clicking the images button on the main screen. Make sure that the user is registered and the image are saved with a name in the standard format.

6. Close the student details window and then on the main screen click on the add attendance button which redirects to a new window. Click on the button and wait for the web cam to get started. It records your attendance and adds it to a csv file named attendance.

7. You can exit using the exit button.
