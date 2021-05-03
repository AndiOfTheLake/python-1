## As a calculator

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100*(1.1 ** 7))

## variables and types
# Create a variable savings
savings=100

# Print out savings
print(savings)

# growth multiplier
growth_multiplier = 1.1

result = savings * growth_multiplier ** 7
print(result)

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

# exercise

"I can add integers, like " + str(5) + " to strings."

"I said " + ("Hey " * 2) + "Hey!"

"The correct answer to this multiple choice exercise is answer number " + str(2)

True + False

## Python lists
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# possible ways to build lists
[1, 3, 4, 2] 
[[1, 2, 3], [4, 5, 7]] 
[1 + 2, "a" * 5, 3]

## Subsetting list
# 0 indexing
# list slicing 
# [start(inclusive):end(exclusive)]

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(upstairs)
print(downstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]

# more subsettings
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]

## Manipulating Lists
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Delete list elements
x = ["a", "b", "c", "d"]
del(x[1])


areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
        
# We want to delete "poolhouse" and "24.5", which of the 
# following lines does the job?

del(areas[10]); del(areas[11])

del(areas[10:11])

del(areas[-4:-2])

del(areas[-3]); del(areas[-4])

## Inner working of lists
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas) # they point to the same list! (In R it's different)

# Change the second command, that creates the variable areas_copy, 
# such that areas_copy is an explicit copy of areas. 
# After your edit, changes made to areas_copy shouldn't affect areas

## FUNCTIONS
max(areas)
round(1.68, 2)

# documentation
help(round) 

# documentation(NO space btw question mark and funciton name) (this is 
# often invalid
# syntax: ?round

# In the documentation we see that there are square brackets around
# ndigits, meaning that this is an optional argument

# Familiar functions
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

## Multiple arguments
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

## Methods

# String Methods
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

## List methods
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

## List methods (2)
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

## Packages
# Install packages
# In the terminal, type pip3 install package.name
# update pip: python -m pip install --upgrade pip
import math

# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

## Download Jupyter Notebook
# https://www.youtube.com/watch?v=otmWEEFysms
# go to C/Users/user/AppData/local/programs/python/scripts
# Open a windows terminal and type: pip install jupyter
# go to a folder. open a windows terminal and type: jupyter notebook


## create PAT on github
# https://www.youtube.com/watch?v=kHkQnuYzwoo
