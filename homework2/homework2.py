# File: homework2.py

# Your file path should look like:
	# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?

	# Git is the actual version control method, it is the repository. Github is where you can host them to collaborate with others. Git Bash is a kind of terminal that mimics unix based OSs like Macs. 

# 2) What’s the difference between the terminal and the command line?

	# the terminal is the program that shows you the command line, and the command line is where you actually put in commands for the computer to interpret. 

# 3) How does Windows PowerShell differ from Git Bash?

	# Windows PowerShell is not Unix based and so it uses a different foundational OS and so a different "language". 

# 4) What’s the difference between Anaconda, conda, and Python?

	# Anaconda is the full Python bundle. Python itself, conda, lots of preinstalled libraries, and the translation dictionary between C and Python. 
	# conda/miniconda is the tool inside of Anaconda that installs packages and manages virtual environments. 
	# Python is the language that interacts with bytecode which is then executed by a virtual machine, which uses machine code written in C, which ultimately runs as machine code so the computer go whrrrr so I can watch Netflix (and do homework :P). 

# 5) What is VS Code? 
	# It is a code editor designed by Microsoft that pretends not to be an IDE until you turn around, at which point it definitely is one, until you look at it again and it breaks. 

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab? 
	# A Jupyter Notebook is a file type that represents an interactive document, served by a Jupyter server and viewed in a browser or editor, where code, text, and output live together and can be executed in seperate chunks, either on a local or remote machine. JupyterLab is an interface for working with Jupyter Notebooks, designed by the same people who created the Jupyter Notebook filetype. 

# 7) What does ~/ mean? 

	# That is shorthand for your home directory. /c/Users/franc, on my computer. His name is Franc. 

# 8) What’s the difference between an absolute path and a relative path? 

	# An absolute path is the address to a directory. Like a mailing address. pwd shows the absolute address for the directory you are currently in. A relative path is instructions to another address relative to the current directory you're in. Like instructions to the corner store: turn right, turn left, then walk halfway down the block.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".	

	# Absolute: /c/Users/franc/python_decal_sp26/clover/course_assignments/homework2
	# Relative: course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"? 
	# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!) 
	# Without the -r, it would error, because ./ is referencing a directory, and rm alone deletes files. 

# 12) What do the following commands do?
	# git add: adds selected changes to the staging area (local, not saved, just proposed)
	# git commit: saves the staged changes as a commit with message attached (local, saved)
	# git push: sends local commits to remote repo destination (remote/public changes)

# 13) What's the difference between "git add ." and "git add <file>"?
	# git add .: stages all modified and/or untracked files in current directory tree
	# git add <file>: stages only that one specific file
# 14) What do "git status" and "git log -1" do?
	# git status: current repo state (what am i about to do)
	# most recent commit info (what did i just do)

# 15) What’s the difference between cloning a repository and pulling from it?
	# cloning is the first time you get the repo, and pulling is updates to the repo you already cloned. 
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
	# I was having trouble connecting my SSH, so I copy pasted the error log into chatGPT and it told me what step I missed. I've done it before a long time ago so I was just going too fast, thinking I was clever. :eyeroll: Oh the consequences of my hubris! Humbled by the mighty machine. 
# 17) What’s a question you still have? What’s something you’re confused about?
	# still not *entirely* sure why working through terminal or nano is "more convenient" than VS code or file manager? but I think it is because they are more complicated and so are easier to break while... it feels like it might be one of those things that comes with time. 
# 18) Tell me a fun fact!
	# Jupyter Notebooks were developed by Project Jupyter, co-founded by UC Berkeley professor and researcher Fernando Perez, who originally created IPython during graduate school in Colorado while studying particle physics. IPython began as an interactive Python shell and grew into a playground for experimenting with code because he was frustrated by the OG Python shell. 

# 19) Print your favorite math expression you've learned in Python so far.
xs = [2, 4, 6, 8] # the number of interesting jars i have in each room in my house
average = sum(xs) / len(xs) # the sum of all of the jars divided by the number of rooms in my house
print(f"{xs} = the number of interesting jars in each room of my house.")
print(f"{len(xs)} = the number of rooms in my house")
print(f"{average} = The average number of interesting jars in any given room.") # average number of interesting jars in any given room in my house
# (Hint: Use print() and add a comment explaining what it does.)
