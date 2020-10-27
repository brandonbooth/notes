# Coding Notes
by [Brandon Booth](www.brandon-booth.com) - Fall 2020


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

## Add environment variables
Enter the following into terminal 
```sh
nano .bash_profile
```

Enter envrionment variables
```sh
export DB_user="brandonb"
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

## Python

TBD...
```sh
TBD
```


## HTML and CSS
3 types of CSS:
1.	 Inline CSS.
2.	 Internal CSS.
3.	 External CSS
> (https://www.c-sharpcorner.com/UploadFile/e6a884/types-of-css/)

> Class and ID Selectors (https://www.htmldog.com/guides/css/intermediate/classid/)
