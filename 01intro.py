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

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

# different ways of importing
# Suppose you want to use the function inv()
# which is in the linalg subpackage of the scipy package. 
# You want to be able to use this function as follows:

# my_inv([[1,2], [3,4]])
# We need the following import statement
from scipy.linalg import inv as my_inv
my_inv([[1,2], [3,4]])

## Your First NumPy Array

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# height is available as a regular list
height_in = [74, 74, 72, 75, 75, 73]

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# subsetting of arrays
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]

high = y > 5
y[high]
print(y[high])

## Side effects of Numpy
np.array([True, 1, 2]) + np.array([3, 4, False])


## 2D numpy arrays
# Your first 2D Numpy Array
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
# Notice that np_baseball.shape is not a method,
# as there would be round brackets around shape
print(np_baseball.shape)

## Subsetting 2D NumPy Arrays
# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]


## 2D Arithmetic
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

## Average versus median
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)


## load data set
import pandas as pd

mlb= "https://assets.datacamp.com/production/repositories/288/datasets/e5d60ff535f86d27609312f9e41c35a1d737ddc0/baseball.csv"
fifa="https://assets.datacamp.com/production/repositories/288/datasets/026a5211b906ac118a09b1a0dbf7df48faafb379/fifa.csv"

mlb = np.array(pd.read_csv (mlb))

fifa = np.arrary(pd.read_csv (fifa))

height_in = mlb[:,3]


## Download Jupyter Notebook
# https://www.youtube.com/watch?v=otmWEEFysms
# go to C/Users/user/AppData/local/programs/python/scripts
# Open a windows terminal and type: pip install jupyter
# go to a folder. open a windows terminal and type: jupyter notebook


## create PAT on github
# https://www.youtube.com/watch?v=kHkQnuYzwoo
# Also check out happy git with r for "gitcreds" package
