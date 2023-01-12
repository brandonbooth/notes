# Coding Notes
by [Brandon Booth](https://brandon-booth.com/index.php) - Fall 2020


## Table of Contents
- [Terminal](#Terminal)
- [Git Command Line](#git-command-line)
- [Python Resources](#python-resources)
- [Python](#Python)
- [Anaconda](#Anaconda)
- [Django](#Django)
- [Heroku](#Heroku)
- [HTML and CSS](#HTML-and-CSS)

**Helpful links:**
- https://guides.github.com/features/mastering-markdown/#syntax
- https://github.com/RichardLitt/standard-readme/edit/master/README.md
- https://education.github.com/git-cheat-sheet-education.pdf
- https://guides.github.com/introduction/flow/
- https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

> Note: TBD...

## Terminal
Show hidden files on Mac: ```Command+Shift+.```

### Environment Variables
To see environment variable enter the following into terminal:
```sh
printenv
```

Add .zshrc (or .bash) files using nano by entering the following into terminal:
```sh
nano .zshrc
```
or
```sh
nano ~/.zshrc
```

Add envrionment variable:
```sh
export db_user="username"
```
Save changes:
Enter ```Control+X```, then ```Y``` to save, then ```Enter``` to keep the same file name.

## Git Command Line
Check version of git installed on mac:
```sh
git -–version
```

Add GitHub username and email to git on Mac:
```sh
git config --global user.email "brandon.booth@yahoo.com"
```
```sh
git config --global user.name "brandonbooth"
```

Navigate to location of folder or project:
```sh
cd projects
```

Initialize the git repository within the project folder:
```sh
git init
```

Use terminal to view the hidden git repository that was created (this will make files visible in finder):
```sh
defaults write com.apple.find AppleShowAllFiles YES
```

Check status of git folder:
```sh
git status
```

Add a file to git (after adding file it is a good practice to check the status to validate):
```sh
git add test1.txt
```

Commit file to git repository with message:
```sh
git commit -m "Initial Commit - add test file"
```

Check git log:
```sh
git log
```

After a change is made add the file and then commit the changes (note: multiple files can be added at the same time - Use “*” as a wildcard):
```sh
git add *.txt
```

Add location of repository:
```sh
git remote add origin https://github.com/brandonbooth/projects.git
```
```sh
git remote add origin https://github.com/brandonbooth/python.git
```
```sh
git remote add origin https://github.com/brandonbooth/brandon-booth_com.git
```

Push to repository:
```sh
git push -u origin main
```

Pull from GitHub:
```sh
git pull https://github.com/brandonbooth/notes.git
```
```sh
git pull https://github.com/brandonbooth/python.git
```
```sh
git pull https://github.com/brandonbooth/brandon-booth_com.git
```

```sh
git pull origin main --allow-unrelated-histories
```

**Misc Commands:**
List git commands:
```sh
git --help
```
```sh
git status --help
```

List branch:
```sh
git branch
```

Checkout a branch:
```sh
git checkout main
```

Merge a branch:
```sh
git merge otherbranch
```

## python-resources
Additional Resources covered in CS511
- RegexOne (https://regexone.com/problem): Learn Regular Expressions with simple, interactive exercises.
- Jsonviewer (https://codebeautify.org/jsonviewer): Visualize JSON code.
- NumPy's main site (https://numpy.org/): Contains tutorials, documentation and instructions for installing it.
- matplotlib's main site (https://matplotlib.org/#): Contains a ton of documentation on this plotting library. The most important is the stuff in the pyplot module.
- Amazon AWS Free Tier (https://aws.amazon.com/free/): this has information on Amazon's AWS free tier of service. You can use limited services for free, but be careful, if you use more than the free limit you can get charged.
- Google App Engine  (https://cloud.google.com/appengine): this is a good place to start on making a web service or working with a cloud platform. It also has a free tier and unlike AWS if you go over the limit, it simply gets turned off until the quota resets.
- Arduino  (https://www.arduino.cc/): This may seem like an outlier but stay with me a second. Learning C/C++ can be helpful for optimizing things that Python does inefficiently. The main benefit is that you get 'closer' to the hardware and and do things like work with memory in a more efficient way. Arduino has a bunch of tutorials for beginners to teach them how to program it and how to learn C/C++. So that is a plus. You are literally working with I/O pins and limited memory, sot that will teach you some stuff. And it is really great for collecting environmental data over time. So you can hook it up to things like moisture sensors in the soil, temperature sensors, a switch in your door. Whatever it is, you can log data over time then do cool stuff with that data. And its fun.

## Python

### Creating virtual environments
Create a virtual environment by executing the following command in the project folder:
```sh
virtualenv venv
```
or:
```sh
python3 -m venv /path/to/new/virtual/environment
```
or with a specific version of python:
```sh
virtualenv -p /usr/bin/python2.7 my_project
```

> https://docs.python.org/3/library/venv.html
 
### Activate virtual environment
The virtual environment is activated by executing the command:
```sh
source venv/bin/activate
```

### Adding alias for python to python3 and pip to pip3
Add the following to environment variables (located in ~/):
```sh
alias python=python3
alias pip=pip3
```

### Environment variables in Python
Use the os module to set and get in Python:
```sh
import os

# Set environment variables
os.environ['username'] = 'theusername'
os.environ['password'] = 'thepassword'

# Get environment variables
USER = os.getenv('username')
PASSWORD = os.environ.get('password')
```


## Anaconda

### Creating conda environment
```sh
conda create -n py2demo python=2.7
```

### To activate this environment, use
```sh
conda activate py2demo
```

### To deactivate an active environment, use
```sh
conda deactivate
```

### Change python version
```sh
conda install python=2.7.16
```

### Search python versions
```sh
conda search python
```


## Django

### Django render path
.urls --> 

### Createing a project
Create and activate vitual environment by creating directory for project and then creating venv:
```sh
python -m venv my_venv_name
```

Install Django:
```sh
pip install django
```

Check version of Django:
```sh
python -m django --version
```

List Django commands:
```sh
django-admin
```

Create project in project folder:
```sh
django-admin startproject eatdrink_project
```


Create app:
```sh
python manage.py startapp users
```


Create superuser (admin):
```sh
python manage.py createsuperuser
```

### How to run server
Navigate to project folder and start server:
```sh
python3 manage.py runserver
```

### How to update db
Make changes to models.py, then make migrations:
```sh
python3 manage.py makemigrations
```
Migrate migrations:
```sh
python3 manage.py migrate
```

### How to check db
Navigate to folder location of db:
```sh
sqlite3 db.sqlite3
```
Schema:
```sh
.schema
```
Exit:
```sh
.exit
```

Navigate to project folder to start server:
```sh
python manage.py runserver
```

To stop server: enter```control+c```
```sh
^C
```

To make migrations:
```sh
python manage.py makemigrations
```

To view sql:
```sh
python manage.py sqlmigrate blog 0001
```

To migrate:
```sh
python manage.py migrate
```

python shell:
```sh
python manage.py shell
```
example:
```sh
(demo_project_venv) brandonbooth@Brandons-MacBook-Pro demo_project % python manage.py shell
Python 3.7.7 (default, Mar 10 2020, 15:43:33) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: brandonbooth>, <User: testuser>]>
>>> User.objects.first()
<User: brandonbooth>
>>> User.objects.filter(username='brandonbooth')
<QuerySet [<User: brandonbooth>]>
>>> User.objects.filter(username='brandonbooth').first()
<User: brandonbooth>
>>> user = User.objects.filter(username='brandonbooth').first()
>>> user
<User: brandonbooth>
>>> user.id
1
>>> user.pk
1
>>> user = User.objects.get(id=1)
>>> user
<User: brandonbooth>
>>> Post.objects.all()
<QuerySet []>
>>> post_1 = Post(title='Blog 1', content='First Post content!', author=user)
>>> Post.objects.all()
<QuerySet []>
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
>>> 

post.content
post.author
post.date_posted
user.post_set.all()

```
 
To :
```sh

```

To :
```sh

```

To :
```sh

```


###Create app
Start app in project directory with name blog:
```sh
python manage.py startapp blog
```


## Heroku
### Setting up Heroku for mac
1) Create Heroku account.

2) Install Heroku CLI  (will need to ensure xcode is installed):
```sh 
brew tap heroku/brew && brew install heroku
```

3) Check that Heroku installed correctly (this will also list all Heroku commands):
```sh 
Heroku
```

4) Login to heroku:
```sh 
heroku login
```

5) Install gunicorn (The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server):
```sh 
pip install gunicorn
```

6) List all packages in env:
```sh
pip freeze
```

7) Write contents of pip freeze to requirements.txt:
```sh
pip freeze > requirements.txt
```

8) Initialize git project folder:
```sh
git init
```

9) Copy recomended gitignore files and save to .gitignore.

10) Add files:
```sh
git add -A
```

11) Commit files:
```sh
git commit -m "initial commit"
```

12)Create Heroku app:
```sh
heroku create demoprojectdjango
```

13) Visit Heroku domain (from project folder):
```sh
Heroku open
```

14) Push git to Heroku to deploy app:
```sh
git push heroku master
```

15) Create new django key using python:
```sh
python
import secrets
secrets.token_hex(24)
```

16) Add secret key to  .zshrc:

17) Add secret key and other environment variables to heroku:
```sh
heroku config:set HERO_SECRET_KEY="secret_key"
heroku config:set HERO_DEBUG_VALUE="TRUE"
heroku config:set AWS_ACCESS_KEY_ID="secret"
heroku config:set AWS_SECRET_ACCESS_KEY="secret"
heroku config:set AWS_STORAGE_BUCKET_NAME="django-demo-project-blog-files"
heroku config:set EMAIL_USER="email@gmail.com"
heroku config:set EMAIL_PASS='password'
heroku config:set 
```





To visit app homepage:
http://127.0.0.1:8000
or
http://localhost:8000

To visit admin page:
http://localhost:8000

## HTML and CSS
3 types of CSS:
1.	 Inline CSS.
2.	 Internal CSS.
3.	 External CSS
> (https://www.c-sharpcorner.com/UploadFile/e6a884/types-of-css/)

> Class and ID Selectors (https://www.htmldog.com/guides/css/intermediate/classid/)
