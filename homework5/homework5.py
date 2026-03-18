
"""
================================================================================

3 Homework 1 + 2 Review

3.1 Vocabulary Review

Git vs Github
    a.  Git is a version control system, it runs locally on my computer. 
        It tracks changes to files in a repository, and keeps track of history.
    b.  GitHub is a website/service that hosts my Git repos online. 
        It is like Google Drive and LinkedIn for coding, saves and displays
        changes to a users repositories so if your computer falls off a boat 
        you don't lose your life's work. 

Terminal vs CommandLine
    a.  A terminal is a program that lets you access and interact with the 
        command line on your computer. It provides a window where you can 
        type commands and see the results.
    b.  CommandLine is the way to talk directly to your computer, and allows
        you to navigate your computer with your keyboard.
    b.  The command line is a text-based interface used to communicate with 
        your computer by typing commands. It allows you to navigate files, 
        run programs, and control the system using the keyboard.

Local vs Remote Repository
    a.  A local repository is a copy of a Git project stored on a local
        computer, not necessarily backed up on another device. It still
        allows for version control but isn't backed up. 
    b.  A remote respository is the same, a saved version of a project
        that is stored on a server like GitHub. It allows you to share
        and syncrhonize work with other people without overwriting
        files.

Version Control
    a.  A system that tracks changes in a repository of files over time
        so you can see past versions and restore them if needed. It also
        when used remotely allows multiple people to work on the same
        project without overwriting each other's work. 

Staging Area
    a.  The staging area is a temporary place where you select changes
        that you want to include in the next commit. It lets you plan
        what changes will be recorded in the version control. 

git add
    a.  Moves changes from your working directory into the staging area.
        Prepares those changes to be included in the next commit.

git commit
    a.  Saves the staged changes as a snapshot in the respository's
        history.

git push
    a.  Uploads the local commits to a remote repository like GitHub.

git status
    a.  Shows the current state of your repository, like which are
        modified, staged, or not tracked.

git pull
    a.  Downloads changes from a remote repository and merges them
        with your local repository.

pwd
    a.  Prints the current working directory, showing the folder
        address.

ls
    a.  Lists all the files and folders in the current directoryu.

cd
    a. Changes the current directory either by using an address
        or just jumping up to the parent directory.

nano
    a.  Opens a file editor in your command line, directly in 
        the terminal.

touch
    a.  Creates a new empty file as long as it does not exist.

mv
    a.  Moves a file to a new location by copying and then
        deleting the original copy.

rm
    a.  Removes or deletes a file, permenantly. 

cat
    a.  Prints the contents of a file into the terminal. Good 
        for previewing file contents by listing the first or
        last couple lines.

        
================================================================================

3.2 A Directory Tree

1.  You have been plopped into Judy's directory system. What command will tell you
    what your current working directory is?
        a.  pwd

2.  The terminal responds by saying you are in ~/python_decal/judy_decal. What 
    command will list all the files in your current working directory? 
        a. ls

3.  Oh no! Brianna just sent out an announcement saying that there was a typo in
    homework.py. You will need to pull the brianna_repo repository to find the
    updated file. What command(s) will let you move to the correct repository
    and pull the latest changes? 
        a.  cd ..
            cd brianna_repo
            git pull

4.  How would you move this new homework.py to the homework/ folder in your
    personal repository?
        a.  mv homework.py judy_decal/homework/

5.  How would you move yourself to the same repository as homework.py?
        a. cd homework/
6.  You want to see the contents of homework.py in your terminal, how would you 
    do this?
        a. cat homework.py
7.  What commands allow you to save the changes and push from your local
    repository to your remote repository? 
        a.  git add .
            git commit -m "message"
            git push
8.  What commands should you call to resolve this error and push your homework
    properly?
        a.  git pull origin main
            git push origin main
8.2 What does the error mean?
        a.  Someone else has pushed to the same branch or made some kind of
            change to the remote repo and the changes will be out of sync.
9.  What absolute path will allow you to move to Recents/?
        a.  cd ~/Recent/  

        
================================================================================

3.3 Draw Your Directory Tree

================================================================================

4 Homework 3 Review

4.1 Data Types
    1.  Write a function that takes any input and returns a string indicating its
        data type. 
"""

def checkDataType(num):
    numtype = type(num).__name__
    return numtype

print(checkDataType(3.14))

"""
================================================================================

4.2 Conditionals

1.  Write a function that takes an integer as input and returns 'Even' if the
    integer is even and 'Odd' otherwise.

"""

def evenorOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(evenorOdd(13))

"""
================================================================================

5 Loops

1.  Write a function that takes a list of integers and returns their sum using
    a loop (do not use sum()).

"""

numbers = [1, 2, 3, 4, 5]

def sumWithLoop(num):
    i = 0
    total = 0
    while i < len(num):
        total += num[i]
        i += 1
    return total

print(sumWithLoop(numbers))

"""
================================================================================

6 Homework 4 Review

6.1 Lists

1.  Write a function that takes a list and returns a new list with each element 
    duplicated.

"""

def duplicateList(lst):
    i = 0
    n = len(lst)
    while i < n:
        lst.append(lst[i])
        i += 1
    return lst

print(duplicateList(numbers))

"""
6.2 Debugging

1.  There's an error in the following function that's supposed to return the
    square of a number. Find and correct it:

"""

def square(num):
    return num * num

print(square(4))

"""
7   Running Your Code

1.  There's an error in the following function that's supposed to return the
    square of a number. Find and correct it:

"""

print(sumWithLoop([1,3,5,7,9]))