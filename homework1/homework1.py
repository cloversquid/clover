# --- 3.1 Variables and Data Types ---

# I have taken a bit of Python before so I think the way I did a bunch
# of this is ahead of the assignment but I am learning a lot
# putting this together this way so I hope it's alright. 

a = 10
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawberry"}
g = (1, 2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4
n = {1, 2, 3, 3}

'''
1. How many different types did you find? 
    Found 9 different types
2. List all the data types you found. 
    (a) int, (b) float, (c) complex, (d) str, (e) list, (f) dict, (g) tuple, (h) list, (i) bool, (j) NoneType, (k) list, (l) str, (m) float
3. What variable have the same data type? 
    int: a | float: b, m | complex: c | str: d, l | list: e, h, k | dict: f | tuple: g | bool: i | NoneType: j | 
4. What was the data type of l? 
    The data type of l was a string
4. Why is it not an integer?
    Because it was reclassified as a string using str()
4. What does str() do? 
    str() converts its input into a string
5. Look up one more data type not given above. Repeat the same procedure. 
    I added a set as variable n. It automatically removes duplicates from the set. In the code it has two 3's, but when it's printed it only has one. 
'''
x = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
y = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

for name, value in zip(y, x):
    print(f"{name}.")
    print(f"    {value}")
    print(f"    {type(value)}")
    print("--")

# --- 3.2 Booleans ---

aa = 10 > 9                                 # True
bb = 10 == 9                                # False
cc = 10 <= 9                                # False
dd = bool("abc")                            # True
ee = bool(123)                              # True
ff = bool(["apple", "cherry", "banana"])    # True
gg = bool(True)                             # True
hh = bool(False)                            # False
ii = bool(0)                                # False
jj = bool("")                               # False
kk = bool(())                               # False
ll = bool([])                               # False
mm = bool({})                               # False
nn = bool(True and False)                   # False
oo = bool(True and True)                    # True
pp = bool(False and False)                  # False
qq = bool(True or False)                    # True
rr = bool(True or True)                     # True
ss = bool(False or False)                   # False
tt = bool(not(False))                       # True
uu = bool(not(True))                        # False
vv = 1 + 2 == 3
ww = "c" in "kool"                         # False

'''
1. What pattern do you notice about expressions returning True or False? 
        The math bits are just returning whether or not the math statements are true or not. 
        The boolean statements are always false when they contain empty sets, lists, etc., like () or [].
        This includes 0. 
        They return true when there is any kind of data in there that is either neutral or true. 
        The last two are just opposites because they are being defined as opposites. 
2. Which expression surprised you about its result? 
        I guess bool(True or False) was interesting because it defaults to true even though it is an "or". 
3. Create an expression, not given above, that will return True. Why is it True? 
        1 + 2 == 3
        It's true because, despite what some people may believe, 1 + 2 does in fact equal 3. 
4. Create an expression, not given above, that will return False. Why is it False? 
        "c" in "kool" returns false because the letter c does not appear in the string kool, 
        which is a way kooler way to spell it anyway. 
'''

xx = [aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq, rr, ss, tt, uu, vv, ww]
yy = ["aa. 10 > 9", "bb. 10 == 9", "cc. 10 <= 9", "dd. bool(''abc'')", "ee. bool(123)", "ff. bool([''apple'', ''cherry'', ''banana''])",
      "gg. bool(True)", "hh. bool(False)", "ii. bool(0)", "jj. bool('''')", "kk. bool(())", "ll. bool([])", "mm. bool({})", "nn. bool(True and False)", 
      "oo. bool(True and True)", "pp. bool(False and False)", "qq. bool(True or False)", "rr. bool(True or True)","ss. bool(False or False)",
      "tt. bool(not(False))", "uu. bool(not(True))","vv. 1 + 2 == 3" ,"ww. ''c'' in ''kool''"]


for name, value in zip(yy, xx):
    print(f"{name} = {value}")
    print(f"    {type(value)}")
    print("--")

# --- 3.3 Operators ---

    ## 3.3.1 Arithmetic Operators
a3 = 10 + 5     # 15  | returns int   | + performs addition
b3 = 10 - 5     # 5   | returns int   | - performs subtraction
c3 = 2 * 4      # 8   | returns int   | * performs multiplication
d3 = 6 / 3      # 2.0 | returns float | / performs division
e3 = 5 % 2      # 1   | returns int   | x % y performs modulo, returning the remainder after dividing x by y
f3 = 3 ** 2     # 9   | returns int   | x ** y puts x to the power of y
g3 = 15 // 2    # 7   | returns int   | x // y performs floor division, rounding down after dividing x by y
    ## 3.3.2 Comparison Operators
h3 = 5 == 2     # False, == compares two values for if they do equal each other
i3 = 10 != 10   # False, != compares two values for if they do not equal each other
j3 = 2 < 5      # True, x < y checks that x is less than y
k3 = 12 > 5     # True, x > y checks that x is greather than y
l3 = 5 <= 6     # True, x <= y checks that x is less than or equal to y
m3 = 1 >= 10    # False, x >= y checks that x is greater than or equal to y
    ##  3.3.3 Assignment Operators
n3 = 5          # 5, x = y sets x equal to y  
n3 += 5         # 10, x += y sets x equal to x plus y
n3 -= 4         # 6, x -= y sets x equal to x minus y
n3 *= 3         # 18, x *= y sets x equal to x times y

x3 = [a3, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3]
y3 = ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3", "j3", "k3", "l3", "m3", "n3"]

for name, value in zip(y3, x3):
    print(f"{name} = {value}")
    print(f"    {type(value)}")
    print("--")


    ## 3.3.4 Logical Operators
'''
1. 
    1.1 What does the operator and do? 
            x and y must both be true for the expression to be considered true. 
    1.2 Write an expression that results in True. 
            5 > 4 and 4 > 3
    1.3 Write an expression that results in False. 
            x =  5
            x == 5 and x == 4
2. 
    2.1 What does the operator or do?
            If either x or y are true then the expression is true
    2.2 Write an expression that results in True. 
            3 > 4 or 5 > 4
    2.3 Write an expression that results in False. 
            4 < 3 or 5 < 4
3. 
    3.1 What does the operator not do? 
            It evaluates an expression an returns the opposite True/False value than the
            expression provided. Flips the boolean. 
    3.2 Write an expression that results in True. 
            not(5 > 10)
    3.3 Write an expression that results in False. 
            not(10 > 5)
'''

    ## More Questions
'''
1. What is the difference between / and //?
        / performs division and returns a float in case it is not cleanly divisible,
        while // does division and returns the number rounded down as an int.  
2. What is the difference between % and //?
        // does division and returns a number rounded down as an int, while
        % is a modulo that returns the remainder after division, also as an int. 
3.
    3.1. What operators would you use to calculate the remainder when dividing two numbers?
            Modulo, %
    3.2. Give an example.
            10 % 5 = 0
4. How do assignment operators work? 
        Saying x = 5, x += 5 = 10 is a shorter way to say x = 5, x = x + 5 = 10. 
        Just eliminates a few extra characters. 
        Example from above: 
            x  = 5         output: 5  | x  = y sets x equal to y  
            x += 5         output: 10 | x += y sets x equal to x plus y
            x -= 4         output: 6  | x -= y sets x equal to x minus y
            x *= 3         output: 18 | x *= y sets x equal to x times y

'''

# --- 3.4 Strings ---

my_string = "hello"
print(f"1.  {my_string}") # Prints: hello

x4 = 0
y4 = 2

while x4 < len(my_string):           # h   | prints each letter in the word at its respective position, 
    print(f"{y4}.  {my_string[x4]}") # e   | starting at index 0 until the length of the word is reached
    x4 += 1                          # l
    y4 += 1                          # l
                                     # o
                                     #
print(f"7.  {my_string[-1]}")        # o   | returns string | prints the last (it loops back to the one before the first)
print(f"8.  {my_string[1:3]}")       # el  | returns string | prints the 1st and 3rd letters
print(f"9.  {my_string[0:5:2]}")     # hlo | returns string | string[start:stop:step] it starts at h, stops at i=5, going up by two steps each time.
print(f"10. {len(my_string)}")       # 5   | returns int    | prints the length of the string
print(f"11. " + my_string + " goodbye") # hello goodbye | returns string | prints the variable and a new string
print(f"12. " + 7 * my_string)          # hellohellohellohellohellohellohello | returns string | prints the variable seven times

    ## 3.4.1 Questions
'''
1. 
    1.1 Define the term slicing. 
            Slicing was used in #9, it used [start:stop:step], so it started at i=0, 
            stopped before i=5 (which doesn't exist in the string, but must be defined
            because it stops in the step *before* the stop index) and incremented by 2 steps. 
            0 -> 2 -> 4, and stopped at 4. If the stop index had been 6, it would have been
            the same because there is no 6th index position in the word "hello" (only has five 
            letters). 
    1.2 For which of the manipulations did you slice your string? 
             In #9. 
2. Call the following, describe the result: 
'''
name = "Oski"
print ("Hello, my name is", name) # Hello, my name is Oski | returns string | prints string within quotes and then whatever is in the variable
'''
3. Call the following, describe the result: 
'''
print(f"Hello, my name is {name}") # Hello, my name is Oski | returns string | prints everything within the quotes, using {replacement fields} to print the variables
'''

4. What is the difference between the two last print statements? 
        #Oof I have been using f-strings the whole time...  
    I was using f-strings to control the white space so I could 
    organize the data more effectively for answering the questions,
    making sure I didn't confuse one line for another. 
    For the two above statements, there is no difference in output,
    but in terms of how customizable it is it becomes easier with f-string. 
    For example, if a + had been used instead of a , then there would 
    not have been a space between the string and the name variable, where
    in an f-string you can just add the space into the whole statement 
    and it just inserts the variable wherever you put it. 
'''

# --- 3.5 Terminal Commands -- 

    # cd
    # Changes directories. Use it to move from one folder to another. 
    # Example: cd Desktop

    # ls
    # Lists files and folders in your working directory. 
    # Example: ls python_decal_sp26
    #          clover/ datatype.py script.py

    # ls -a
    # Lists files and folders in the working directory, including hidden files. 
    # Example: ls -a python_decal_sp26
    #          ./ ../  .git/ homework1/

    # mkdir
    # Makes a new folder/directory within your working directory.
    # Example: mkdir example
    #          ls
    #          example/ homework 1/

    # cat
    # Displays the contents of a file, or tells you it is a directory.
    # Example: cat homework1.py
    #          the entire contents of this file :P
    
    # pwd
    # Shows you the address of your working directory. "print working directory"
    # Example: pwd
    #          /c/Users/franc/python_decal_sp26/clover/homework1

    # cd ..
    # Stands for "change directory", the .. moves you up one directory. 
    # Example: cd ..
    #          /c/Users/franc/python_decal_sp26/clover

    # cd . 
    # Moves you to the current directory you're already in. Effectively does nothing. 
    # Example: cd . 
    #          /c/Users/franc/python_decal_sp26/clover

    # cd ~
    # Moves you to your home directory. It just ~magically~ knows which one is home. (it checks for a variable)
    # Example: cd ~
    #          /c/Users/franc 

    # cp
    # Copies a file or directory.
    # Example: cp homework1.py homework1copy.py
    #          ls
    #          homework1.py homework1copy.py

    # mv
    # Like cp, but doesn't keep the original. Makes a copy, puts it into a specified location, and deletes the old one.
    # Example: mv homework1copy.py ~/python_decal_sp26/clover
    #          ls ~/python_decal_sp26/clover
    #          example/ homework1/ homework1copy.py

    # rm (be careful with this one)
    # Removes/deletes a file or folder, permenantly. 
    # Example: rm homework1copy.py
    #          ls
    #          example/ homework1/

    # clear
    # Clears the terminal. 
    # Example: clear
    #          $ :P

    # grep
    # Searches a file for lines that match and prints them. 
    # Example: grep grep homework.py
    #          # grep
    #          # Example: grep grep homework.py (getting a little meta there...)

# Questions
'''
1. Look up 3 other commands not present. Define and explain how to use them on the command line. 
    a. head
        Prints the first lines of a file. 
        Example: head homework1.py
                    # --- 3.1 Variables and Data Types ---
                    etc. etc. 
    b. tail
        Prints the last lines of a file. 
        Example: tail homework1.py
                    b. tail
                        Prints the last lines of a file
                        Example: tail homework1.py
                        (meta!!!!!!!)
    c. less
        Opens a file in a scrollable viewer
        Example: less homework1.py
2. What is the difference between ls and ls -a? 
        ls shows all files and folders, while ls -a shows all files and folders including hidden ones. 
3. What is a hidden file? 
    Preface the name of a file with a . and it will hide it from ls or the file explorer view. 
4. Look up 3 other flags. Define them and use them on the command line. 
    a. grep -i 
        Ignores case when searching
    b. rm -r 
        Removes recurisively, removing the directory and everything inside it 
    c. cp -r
        Copies recusively, copying the directory and everything inside of it
'''

