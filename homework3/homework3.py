## 3.1 Say Goodbye
def say_goodbye(name):
    # prints a goodbye message using the name
    print(f"Goodbye, {name} :(")


## 3.2 Area of a Circle
import math

def area_circle(r):
    # returns the area of a circle given the radius r
    area = math.pi * r**2
    return area


### 4 Return Functions ###
# add
def add(a, b):
    # returns the sum of a and b
    return a + b


## 4.1 Subtract, Multiply and Divide
# subtract
def subtract(a, b):
    # returns a minus b
    return a - b


# multiply
def multiply(a, b):
    # returns a times b
    return a * b


# divide
def divide(a, b):
    # returns a divided by b
    # (assumes b is not 0)
    return a / b


### 5 Conditionals
## 5.1 What Should I Wear?
readings = [15, 14, 17, 20, 23, 28, 20]  # temperature readings for the day

def outfit(temp):
    # returns a tuple (low, high) from a list of temperatures
    upper = max(temp)
    lower = min(temp)
    today = (lower, upper)
    return today


## 5.2 Check if it's the Weekend
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


## 5.3 Fuel Efficiency Calculator 
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


## 5.4 Secret Code
def secret_code(n):
    # moves the last digit to the front (ex. 12345 -> 51234)
    last_digit = n % 10
    rest = n // 10
    encrypted = int(str(last_digit) + str(rest))
    return encrypted


### 6 Loops ###
## 6.1 Oski Stole Your Power
def power_loop(x, y):
    # computes x^y without using ** or pow()
    result = 1
    for _ in range(y):
        result *= x
    return result


## 6.2 Min & Max with Loops!
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


## 6.3 Calculate the Sum
def sum_digits(n):
    # sums the digits of an integer (ex. 2468 -> 2+4+6+8)
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total