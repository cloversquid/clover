######## DEBUGGING HELPERS ###########################
check = True  # Switch this to True if you want to enable printed checks of the lists throughout
def check_list(lst):
    if check == True:
        print("~~~~~ Function Test ~~~~~")
        n = 0
        for i in lst:
            print(f"  {n}. {i}")
            n += 1
        print("~~~~~ CHECK COMPLETE *cool robot noise* ~~~~~\n")
    else:
        return False
headers = True # switch to True if you want to enable section headers in output
def disp_header(header, num):
    if headers:
        if num == 1:
            print(f"\n=== {header} ===\n")
        else: 
            print(f"{header}")

############ END DEBUGGING HELPERS #####################################

### | === 3 Lists === | ###
disp_header(" | === 3 Lists === | ", 1)

## === 3.1 List Operations ===
disp_header("3.1 List Operations", 1)

# 0. Make a list of your favorite foods (very serious not silly at all)
disp_header("0. Make a list of your favorite foods (very serious not silly at all)", 2)

foods = ["pasta", "paneer tikka masala", "rocks", "the slime you find under river rocks", "cottage cheese with apples"]

# 1. Print the second food on the list.
disp_header("1. Print the second food on the list.", 2)

print(f"      {foods[1]}")

# 2. Print the last food using negative indexing.
disp_header("2. Print the last food using negative indexing.", 2)

print(f"      {foods[-1]}")

# 3. Add a new food to the end of the list using .append()
disp_header("3. Add a new food to the end of the list using .append()", 2)

foods.append("sour gummy worm (just one)")

check_list(foods)

# 4. Insert "apple" at the start of the list
disp_header("4. Insert 'apple' at the start of the list", 2)

foods.insert(0, "apple")

check_list(foods)

"""
I originally wrote foods.insert("apples"[0])
Got a TypeError: insert expected 2 arguments, got 1
I googled ".insert() python syntax" and fixed the syntax
"""

# 5. Remove the third item on the list using del or .remove()
disp_header("5. Remove the third item on the list using del or .remove()", 2)

del foods[2]

"""
I originally wrote "foods.remove[2]"
Got a ValueError: list.remove(x) not in list
Googled ".remove() python syntax" and then "del python syntax"
switched to del instead so i could use an index #
"""
check_list(foods)

# 6. Print the length of the list with len()
disp_header("6. Print the length of the list with len()", 2)

print(f"      HOW MANY FOODS IS IT?? {len(foods)} MANY FOODS!!!")

# 7. Loop through the list and print each food in uppercase
disp_header("7. Loop through the list and print each food in uppercase", 2)

m = 1
for i in foods:
    print(f"      {m}. {i.upper()}")
    m += 1

"""
Initially wrote "print(i).upper()
Got AttributeError: 'NoneType' object has no attribute 'upper'
Realized I needed to put .upper() inside the print not outside of it
"""
# 8. Make a new list containing only the first and last food (use slicing)
disp_header("8. Make a new list containing only the first and last food (use slicing)", 2)

best_foods = foods[0::5]

check_list(best_foods)

# 9. Use an if statement to check if "potato" is in the list. 
#    If it is, print "A potato!" otherwise, "No potato!"
disp_header("9. Use an if statement to check if 'potato' is in the list.", 2)

def is_a_potato_or_nah(lst):
    if "potato" in lst:
        print(f"      A potato!\n")
    else:
        print(f"      No potato!\n")

is_a_potato_or_nah(best_foods)

## === 3.2 Slicing and Striding ===
disp_header("3.2 Slicing and Striding", 1)

# 0. Create a list of numbers from 0 to 20, inclusive, using the range() function. Store it in a variable called numbers.
disp_header("0. Create a list of numbers from 0 to 20, inclusive, using the range() function. Store it in a variable called numbers.", 2)

numbers = []
for i in range(0, 21):
    numbers.append(i)

check_list(numbers)

# 1. Define and call get_first_15(numbers)
disp_header("Define and call: \n 1. get_first_15(numbers)", 2)

def get_first_15(numbers):
    lst = numbers[0:15]
    return lst
step_1 = get_first_15(numbers)

check_list(step_1)

# 2. get_every_5th returns every fifth element from it (i = 0, 5, 10...) should return three numbers. 
disp_header(" 2. get_every_5th returns every fifth element from it (i = 0, 5, 10...) should return three numbers.", 2)
def get_every_5th(numbers):
    lst = numbers[0:15:5]
    return lst
step_2 = get_every_5th(step_1)
check_list(step_2)

# 3. reverse_and_stride(lst) which takes the list from get_every_5th and reverses it and then returns every third element
# of the reverse list... feels kinda silly to make a whole seperate function to slice it into every third again. 
disp_header(" 3. reverse_and_stride(lst) which takes the list from get_every_5th and reverses it and then returns every third element of the reverse list", 2)

def reverse_and_stride(and_reverse_it):
    flip_it = and_reverse_it[::-1]
    every_third = flip_it[::3]
    return every_third
step_3 = reverse_and_stride(step_2)

check_list(step_3) 

## === 3.3 Nested Lists ===
disp_header("3.3 Nested Lists", 1)
# 3.3.1 Nested List Operations
disp_header("3.3.1 Nested List Operations", 1)
# 0. Define list of numbers
disp_header("0. Define list of numbers", 2)

numbers = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print the third row 
disp_header("1. Print the third row", 2)

print(f"      {numbers[2]}")

# 2. Print the second item in the second row
disp_header("2. Print the second item in the second row", 2)

print(f"      {numbers[1][1]}")

# 3. Add [10, 11, 12] as a new row using .append()
disp_header("3. Add [10, 11, 12] as a new row using .append()", 2)

numbers.append([10, 11, 12])

"""
I used numbers = numbers.append([10,11,12]) instead of just numbers.append([10,11,12]),
which technically compiled but when I used check_list(numbers) it threw a TypeError: 'NoneList' object is not iterable
which I did not understand, so I put the code and the output in ChatGPT and asked what was wrong and it verified that
I was supposed to write numbers.append instead of numbers = numbers.append. Curse you silent error.  
"""

check_list(numbers)

# 4. Write a function called sum_nested() that loops through each row, sums all numbers, and returns the total
disp_header("4. Write a function called sum_nested() that loops through each row, sums all numbers, and returns the total", 2)

def sum_nested(nest):
    sumOfNest = 0                # start total at 0
    for row in nest:             # go through each row
        for number in row:       # go through each number in that row
            sumOfNest += number  # add number to total
    return sumOfNest             # give back final total

print(f"      Sum of nested lists is: {sum_nested(numbers)}\n")

## 3.4 Create a 5x5 List
disp_header("3.4 Create a 5x5 List", 1)

# 0. Write a function that uses nested for loops to create a 5x5
# list of numbers from 1 to 25. Store the results in a new variable. 
disp_header("0. Write a function that uses nested for loops to create a 5x5 list of numbers from 1 to 25", 2) 

def fivebyfive():
    n = 1
    gridtwentyfive = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(n)
            n += 1
        gridtwentyfive.append(row)
    return gridtwentyfive

step1 = fivebyfive()

check_list(step1)

# 1. Write a function that replaces all multiples of 3 with "?".
# Store the updated 5x5 list in a new variable. 
disp_header("1. Write a function that replaces all multiples of 3 with '?'", 2)

def we_hate_threes(big_grid):
    for row in big_grid:
        for i in range(len(row)):
            if row[i] % 3 == 0:
                row[i] = "?"
    return big_grid

step2 = we_hate_threes(step1)

check_list(step2)

# 2. Write a function that adds all elements not equal to "?" and returns the sum. Save the result in a variable. Use ~= to skip "?".
disp_header("2. Write a function that adds all elements not equal to '?'' and returns the sum.", 2) 

def sum_nested_skip(some_grid):
    sumOfNest = 0
    for a_row in some_grid:
        for i in range(len(a_row)):
            if a_row[i] != "?":
                sumOfNest += a_row[i]
    return sumOfNest
            
step3 = sum_nested_skip(step2)
print(f"      The sum of numbers in the five by five grid not including any multiples of three is: {step3}")

### 4 Dictionaries
disp_header("| === 4 Dictionaries === |", 1)
## 4.1 Dictionary Operations
disp_header("4.1 Dictionary Operations", 1)

# Use the following dictionaries:
ages = {
    "Katie":30,
    "Mariam":42,
    "Safia":25,
    "Mira":48
}
# 1. Print Katie's age
disp_header("1. Print Katie's age", 2)
print(f"      {ages["Katie"]}")

# 2. Change Mira's age to 100
disp_header("2. Change Mira's age to 100", 2)
ages["Mira"] = 100

# 3. Add Milana with an age of 52
disp_header("3. Add Milana with an age of 52", 2)

ages["Milana"] = 52

# 4. Remove Mariam from the dictionary
disp_header("4. Remove Mariam from the dictionary", 2)
del ages["Mariam"]

# 5. Use a for loop to print out each person's name and age
disp_header("5. Use a for loop to print out each person's name and age", 2)

for name, age in ages.items():
    print(f"      {name} is {age} years old.")


### 5 VS Code
disp_header(" | === 5 VS Code === | ", 1)

## 5.2 In Your VS Code Terminal
disp_header("5.2 In Your VS Code Terminal\n", 2)
# 3. Pick you favorite functions from the problem set. 
# 4. Include code at the bottom of your file that calls this function and prints the result.
disp_header("4. Include code at the bottom of your file that calls this function and prints the result.",2)
examplefivebyfive = fivebyfive()

print(f"      Down with 3 and everything to do with it! \n      {we_hate_threes(examplefivebyfive)}")