# Coding Notes
by [Brandon Booth](https://brandon-booth.com/index.php) - Fall 2020


## Table of Contents
- [Git Command Line](#git-command-line)
- [Python / Django](#Python-/-Django)
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

## Misc. Commands
Show hidden files on Mac: ```Command+Shift+.```

## How to set and get environment variables
To see environment variable enter the following into terminal 
```sh
printenv
```
```sh
printenv
```

Use the os module
```sh
import os

# Set environment variables
os.environ['username'] = 'theusername'
os.environ['password'] = 'thepassword'

# Get environment variables
USER = os.getenv('username')
PASSWORD = os.environ.get('password')
```

## How to edit bash file
Enter the following into terminal 
```sh
nano .bash_profile
```

Enter envrionment variables
```sh
export db_user="username"
```

Save changes
Enter ```Control+X```, then ```Y``` to save, then ```Enter``` to keep the same file name.


## Git Command Line

Check version of Git installed on mac
```sh
git -–version
```

Add GitHub username and email to git on mac
```sh
git config --global user.email "brandon.booth@yahoo.com"
```
```sh
git config --global user.name "brandonbooth"
```

Navigate to location of folder or project
```sh
cd projects
```

Initialize the git repository within the chosen folder location
```sh
git init
```

Use terminal to view the hidden git repository that was created (this will make files visible in finder)
```sh
defaults write com.apple.find AppleShowAllFiles YES
```

Check status of git folder
```sh
git status
```

Add a file to git (after adding file it is a good practice to check the status to validate)
```sh
git add test1.txt
```

Commit file to git repository with message
```sh
git commit -m "Initial Commit - add test file"
```

Check git log
```sh
git log
```

After a change is made add the file and then commit the changes (note: multiple files can be added at the same time - Use “*” as a wildcard).
```sh
git add *.txt
```

Add location of repository
```sh
git remote add origin https://github.com/brandonbooth/projects.git
```
```sh
git remote add origin https://github.com/brandonbooth/python.git
```
```sh
git remote add origin https://github.com/brandonbooth/brandon-booth_com.git
```

Push to repository
```sh
git push -u origin main
```

Pull from GitHub
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
List git commands
```sh
git --help
```
```sh
git status --help
```

List branch
```sh
git branch
```

Checkout a branch
```sh
git checkout main
```

Merge a branch
```sh
git merge otherbranch
```

## Python / Django

### How to create virtual environment
Creation of virtual environments is done by executing the command venv:
```sh
python3 -m venv /path/to/new/virtual/environment
```
> https://docs.python.org/3/library/venv.html
 
### Activate virtual environment
The virtual environment is activated by executing the command:
```sh
source /Users/brandonbooth/projects/django_project/venv/bin/activate
```

### alias for python to python3
Add the following to .bash_profile (located in ~/)
```sh
alias python=python3
```

### How to run server
Navigate to mysite to start server:
```sh
python3 manage.py runserver
```

### How to update db
Make changes to models.py, then makemigrations and migrate:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

### How to check db
Navigate to folder location of db:
```sh
sqlite3 db.sqlite3
```
then
```sh
.schema
```

```sh
.exit
```
## Django
### starting project


Create and activate vitual environment by creating directory for project and then creating venv:
```sh
python -m venv my_venv_name
```

Install django
```sh
pip install django
```

Check version of django
```sh
python -m django --version
```

list django commands
```sh
django-admin
```

create app:
```sh
python manage.py startapp users
```



Navigate to mysite to start server:
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
start app in project directory with name blog:
```sh
python manage.py startapp blog
```


## Heroku
### Setting up Heroku for mac
1) Create Heroku account
2) Install Heroku CLI  (will need to ensure xcode is installed).
```sh 
brew tap heroku/brew && brew install heroku
```
3) Check that Heroku installed correctly (this will also list all Heroku commands)
```sh 
Heroku
```

4) Login to heroku
```sh 
heroku login
```

5) Install gunicorn (The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server).
```sh 
pip install gunicorn
```

6) List all packages in env
```sh
pip freeze
''

7) Write contents of pip freeze to requirements.txt
```sh
pip freeze > requirements.txt
''

8) 
```sh

''


) 
```sh

''



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
