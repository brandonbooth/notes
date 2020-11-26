# Coding Notes
by [Brandon Booth](https://brandon-booth.com/index.php) - Fall 2020


## Table of Contents
- [Git Command Line](#git-command-line)
- [Python](#Python)
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

Navgate to directory where you would like to save the project and enter the following into command line:
```sh
django-admin startproject demo_project
```


## HTML and CSS
3 types of CSS:
1.	 Inline CSS.
2.	 Internal CSS.
3.	 External CSS
> (https://www.c-sharpcorner.com/UploadFile/e6a884/types-of-css/)

> Class and ID Selectors (https://www.htmldog.com/guides/css/intermediate/classid/)
