# notes
by [Brandon Booth](https://brandon-booth.com)

## Table of Contents
- [git Command Line](#git-command-line)

**Helpful links:**
- https://guides.github.com/features/mastering-markdown/#syntax
- https://education.github.com/git-cheat-sheet-education.pdf
- https://guides.github.com/introduction/flow/
- https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

> Note: TBD...

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


After a change is made add the file and then commit the changes (note: Multiple files can be added at the same time - Use “*” to Add multiple files).
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


Pull from GitHub
```sh
git pull https://github.com/brandonbooth/notes.git
```

Created by Brandon Booth (brandon.booth@yahoo.com) - Fall 2020
