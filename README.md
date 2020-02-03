# recommender

To run this app, you must have installed Flask

if you do not have flask installed on your system:
I am going to demostrate on how to get the application running on your local machine. After installing python interpreter on your machine, we will create a virtual environment to house our Recommendation application, this is done to seperate the framework environment from the core python environment.
To do this, we will be using a library called virtualenvironment wrapper. Below command demostrate how to install it on different machines.

#ON WINDOWS
pip install virtualenvwrapper-win

#ON LINUX machine
pip install virtualenvwrapper

After you have successful installed virtual environment, use the below command to create a virtual environment
mkvirtualenv [name_of_your_environment] e.g. mkvirtualenv recommendation

Afer your finished creating the environment, the interpreter activate the enivironment immediately. To deactivate the environment, use
deactivate
To activate the environment back, use

workon [name_of_your_environment] e.g workon recommendation

Now that you have successfully setup the virtualenvironment. The next thing to do is to install flask in the environment and other dependencies. Type the following command:

pip install flask --> This installs the latest version of flask in the environment
python install -r requirements.txt --> to install all the necessary dependencies

After the completion of above commands, Our application is ready to be launched; To open the app, 
run:
  python run.py  --> Note you must be in the folder you extrated the zip file or the clone of this project.

THANKShttps://github.com/bjboss007/recommender/edit/Branch/README.md
