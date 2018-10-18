#### COMMON DEPENDENCIES:
* python 3.6.5
* Appium v1.9.1

#### FOR SETUP PYTHON DEPENDENCIES:
For mac OS:
* Create and activate virtualenv
> pip3 install virtualenv
* Verify installation is successful
> virtualenv --version
* Create a virtual environment for a project (execute command from the project directory)
* Go to the project directory
> virtualenv venv
* For activation virtualenv (execute command from the project directory)
> source venv/bin/activate
* Setup python dependencies (execute command from the project directory)
> pip3 install -r requirements.txt

##### set env variables
Our "config.py" file gets data from ".env" file
* create ".env" file
* set the requirement variables (e.g. --> see "{project_path}/example.env")

##### FAQ (How to run the tests)
* For run all tests
> pytest
* For run one test - add path to the file
* e.g. for run test test_user_login
> pytest tests/acceptance/test_user_login.py