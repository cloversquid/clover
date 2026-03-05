# I learned about inputs so I wanted to practice them, ran this in a Jupyter Notebook cell and it seemed to work fine

## 3.1 Say Goodbye
print("3.1 Say Goodbye :(\n")  # print homework section header

my_name = input("What's your name? ")  # asks for input, returns a string

def say_goodbye(name):
    # prints a goodbye message using the name
    print(f"Goodbye, {name} :(")

say_goodbye(my_name)  # call the function


## 3.2 Area of a Circle
import math
print("\n3.2 Area of a Circle\n")  # print homework section header

my_circle = float(input("What is the radius of your circle? "))  # input radius, convert to float

def area_circle(r):
    # returns the area of a circle given the radius r
    area = math.pi * r**2
    return area

print(f"The area of your circle is {area_circle(my_circle)}. And that's a math fact!")  # print result


### 4 Return Functions ###
print("\n4 Return Functions\n")  # print homework section header

# add
firstNum, secondNum = map(float, input(" ex. Adding! Enter two numbers seperated by a space: ").split())
# asks for two numbers separated by a space, converts them to floats

def add(a, b):
    # returns the sum of a and b
    return a + b

print(f"{firstNum} + {secondNum} = {add(firstNum, secondNum)}")


## 4.1 Subtract, Multiply and Divide
# subtract
firstNum, secondNum = map(float, input(" 4.1 Subtracting! Enter two numbers seperated by a space: ").split())
# asks for two numbers separated by a space, converts them to floats

def subtract(a, b):
    # returns a minus b
    return a - b

print(f"{firstNum} - {secondNum} = {subtract(firstNum, secondNum)}")


# multiply
firstNum, secondNum = map(float, input(" 4.1 Multiplying! Enter two numbers seperated by a space: ").split())
# asks for two numbers separated by a space, converts them to floats

def multiply(a, b):
    # returns a times b
    return a * b

print(f"{firstNum} * {secondNum} = {multiply(firstNum, secondNum)}")


# divide
firstNum, secondNum = map(float, input(" 4.1 Dividing! Enter two numbers seperated by a space: ").split())
# asks for two numbers separated by a space, converts them to floats

def divide(a, b):
    # returns a divided by b
    # (assumes b is not 0)
    return a / b

print(f"{firstNum} / {secondNum} = {divide(firstNum, secondNum)}")


### 5 Conditionals
## 5.1 What Should I Wear? 
print("\n5.1 What Should I Wear?\n")

readings = [15, 14, 17, 20, 23, 28, 20]  # temperature readings for the day

def outfit(temp):
    # returns a tuple (low, high) from a list of temperatures
    upper = max(temp)
    lower = min(temp)
    today = (lower, upper)
    return today

print(f" Here's the low and high for the day: {outfit(readings)} \n The rest is up to you, bud.")


## 5.2 Check if it's the Weekend (BEGINNER PATCH)
print(f"\nCheck if it's the Weekend\n")
dow = input(" What day of the week is it? ").strip().lower()
# reads day input, removes extra spaces, makes it lowercase

def is_weekend(day):
    # checks if the day is a weekend day (name OR number)

    # saturday/sunday by name
    if day == "saturday" or day == "sunday":
        return True

    # saturday/sunday by number (6, 7)
    if day == "6" or day == "7":
        return True

    # otherwise, not the weekend
    return False

if is_weekend(dow) == False:
    reply = "It's not the weekend! Get back to work!!"
else:
    reply = "It IS the weekend! Woohoo!"
print(f" {is_weekend(dow)}. {reply}")


## 5.3 Fuel Efficiency Calculator (BEGINNER PATCH)
print(f"\nFuel Efficiency Calculator\n")
my_miles = int(input(" How many miles did you go? "))
my_gallons = int(input(" How many gallons of gas did you use? "))

def fuel_efficiency(miles, gallons):
    # returns miles per gallon, or returns a message if input is not valid

    # both must be positive
    if miles > 0 and gallons > 0:
        efficiency = miles / gallons
        return efficiency

    # gallons is zero or negative
    if gallons <= 0:
        return f" Did you walk? You can't possibly have used {gallons} gallons of gas."

    # miles is zero or negative
    if miles <= 0:
        return f" I am asking for a number, not a vector. Positive number, please!"

print(fuel_efficiency(my_miles, my_gallons))


## 5.4 Secret Code
print("\n5.4 Secret Code\n")

my_number = int(input(" Enter an integer to encrypt (ex. 12345): "))

def secret_code(n):
    # moves the last digit to the front (ex. 12345 -> 51234)
    last_digit = n % 10
    rest = n // 10
    encrypted = int(str(last_digit) + str(rest))
    return encrypted

print(f" Encrypted result: {secret_code(my_number)}")


### 6 Loops ###
print("\n6 Loops\n")


## 6.1 Oski Stole Your Power
print("6.1 Oski Stole Your Power\n")

x = float(input(" Enter a base (x): "))
y = int(input(" Enter an exponent (y, whole number): "))

def power_loop(x, y):
    # computes x^y without using ** or pow()
    result = 1
    for _ in range(y):
        result *= x
    return result

print(f" {x} raised to the power of {y} is {power_loop(x, y)}. Take that, Oski!")


## 6.2 Min & Max with Loops!
print("\n6.2 Min & Max with Loops!\n")

nums = list(map(int, input(" Enter integers separated by spaces: ").split()))
# reads a line of integers and turns it into a list

def min_for(lst):
    # finds the minimum value using a for loop
    current_min = lst[0]
    for val in lst:
        if val < current_min:
            current_min = val
    return current_min

def max_for(lst):
    # finds the maximum value using a for loop
    current_max = lst[0]
    for val in lst:
        if val > current_max:
            current_max = val
    return current_max

print(f" For-loop min: {min_for(nums)}")
print(f" For-loop max: {max_for(nums)}")

def min_while(lst):
    # finds the minimum value using a while loop
    current_min = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] < current_min:
            current_min = lst[i]
        i += 1
    return current_min

def max_while(lst):
    # finds the maximum value using a while loop
    current_max = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] > current_max:
            current_max = lst[i]
        i += 1
    return current_max

print(f" While-loop min: {min_while(nums)}")
print(f" While-loop max: {max_while(nums)}")

## 6.3 Calculate the Sum
print("\n6.3 Calculate the Sum\n")

my_digits = int(input(" Enter an integer (ex. 2468): "))

def sum_digits(n):
    # sums the digits of an integer (ex. 2468 -> 2+4+6+8)
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(f" Sum of digits: {sum_digits(my_digits)}")
print(f" You can take our functions, Oski, but you'll never take our spirit.")