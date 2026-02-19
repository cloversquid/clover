fruits = ['apple', 'banana', 'cherry']
print(fruits)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

mixed = ['hello', 5, True, None]
print(mixed)

print(fruits[1])
print(numbers[1])

## NEGATIVE INDEXING ##
print(fruits)
print(fruits[-1]) # prints the last item in the list
print(fruits[-2]) # gets middle because it is both the 2 and -2 positons

fruits[0] = 'grape' # changed my first fruit to grape
print(fruits)

## INSERT VS APPEND ##

numbers.append(7) # append adds a 7 at the END of numbers list
print(numbers)

mixed.insert(1,False) # inserting False as the second thing in the mixed list
print(mixed)

## REMOVING FROM LISTS ##
fruits.remove('banana') # removes the FIRST instance of banana, does not remove ALL bananas
print(fruits) 
fruits.append('banana')
print(fruits)

fruits.pop(0) # removes the zeroth element
print(fruits)

## FOR LOOPS ##
alist = fruits

for item in alist: # using fruit
    print(item)

colors = ['green', 'red', 'purple']
print(colors[1])
print(colors[-1])
colors.append('yellow')
for color in colors:
	print(color)
      

## DICTIONARIES ##

students = {"name":"Clover", "year": 4, "major":"Astro"}
print(students["name"]) # to access "name" use this syntax: dictionary_name["key_name"]
print(students["major"]) # and again!

students["major"]="English"
print(students["major"])

print(students) # prints the whole dict with no label
print(students.items()) # prints pairs with a lil label in a tuple within a tuple
print(students.keys()) # prints the keys w label
print(students.values()) # prints the values w label

students["school"] = "UC Berkeley" # adds another item: old_dict["new_key"] = "new_item"
print(students) 

for key, value in students.items():
        print(f"{key} = {value}")


pet = {"name":"Luna", "type":"cat", "age":3}
print(pet["name"])
pet["age"] = 4
pet["favorite toy"] = "string"

for key, value in pet.items():
       print(f"{key} = {value}")


## ADVANCED LISTS ##

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums)
print(nums[1:4])    # prints 2, 3, 4
print(nums[:5])     # starts at the beginning, goes all the way to the sixth number
print(nums[1:])     # starts at the second, goes to the end
print(nums[::2])    # striding, prints every other number
print(nums[1:6:2])  # start at 2, got every other number, ends at 6