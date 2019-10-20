# Test Project

This is a simple web project in Django created to make sure you have installed
all necessary tools and frameworks.

Here are instructions on how to get started:

1) Download the latest version of Python for your machine from here:
   https://www.python.org/downloads/

2) To install Django, open your command prompt (terminal) and type:

    ```pip install Django``` if you are on Windows,
    
    ```pip3 install Django``` if you are on Mac.
    
    If none of these worked, try using ```pip install Django==2.2.6```,
    where 2.2.6 is the latest release.

3) Navigate to your favourite folder for storing projects in git-bash or any
other tool you are using git with and execute this series of commands:

       git clone https://github.com/Mystery3051/request-to-pay.git
       git checkout django-sandbox

    This will create a project folder named **request-to-pay** and switch the
    development branch to django-sandbox so that you don't modify any files in
    production code.
    
4) Using command line (terminal) navigate *inside* **request-to-pay** folder and type:
    
    ```python manage.py runserver``` on Windows,
    
    ```python3 manage.py runserver``` on Mac.
    
5) Go to your browser and type ```localhost:8000``` and see a beautiful
debug page.

6) If something didn't work - see this thread on StackOverflow:
https://stackoverflow.com/questions/37094032/how-to-run-cloned-django-project

   and update this README.md file to include hacks you used to make it work!
