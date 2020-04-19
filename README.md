# Django Blog Lesson Steps

## Venv
- python3 -m venv myvenv
- virtualenv venv
- virtualenv venv --system-site-packages
- source venv/bin/activate

## Deactivation a Virtual Environment
- deactivate

## Reactivating a Virtual Environment
- source venv/bin/activate

## Uninstall Packages
- sudo pip3 uninstall packagename

## Install Django (Upto 2022)
- pip install django==1.11.29

## requirements.txt
- pip3 freeze --local > requirements.txt

## Start a Django Project in the Directory
- django-admin startproject blog .

## Change Its Mode to Be Executable to Run It
- chmod +x manage.py

## Initialise the Database and Get the Tables Ready
- ./manage.py migrate

## Allowing Hosts
- In settings.py: 
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                os.environ.get('HOSTNAME')]
```

## Run It in the Server
- python3 ./manage.py runserver

## Initialise Git
- git init

## .gitignore
- echo -e "*.sqlite3\n*.pyc\n.vscode\n/myvenv\n/venv\n__pycache__/" > .gitignore

## Upload Onto Github
- git add .
- git status 
- git commit -m "Created simple Django project"
- git remote add origin < the repository url >
- git push -u origin master

## Travis CI
- Select the project repository
- Click on Unknown 
- Copy and paste the Markdown result to the README.md file 
[![Build Status](https://travis-ci.com/Rian1010/django-blog-lessons.svg?branch=master)](https://travis-ci.com/Rian1010/django-blog-lessons)