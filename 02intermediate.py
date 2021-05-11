## Intermediate python

# Basic plots with Matplotlib


import numpy as np
import pandas as pd

dt1 = pd.read_csv("https://assets.datacamp.com/production/repositories/287/datasets/5b1e4356f9fa5b5ce32e9bd2b75c777284819cca/gapminder.csv")

# Line plot 3
dt1.head()
gdp_cap = dt1["gdp_cap"]
life_exp = dt1["life_exp"]
pop = dt1["population"]

import matplotlib.pyplot as plt

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

type(pop)

import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop =  2 * np_pop

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()



## Dictionary to DataFrame
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':'names', 'drives_right':'dr','cars_per_cap':'cpc'}
print(my_dict)

# While loop
# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    offset = offset - 1
    print(offset)  


np_height = np.array([75]* 10)
np_weight = np.array([200]*10)

import random as rd
rd.seed(500)
e1 = np.random.normal(loc=0.0, scale=1.0, size=len(np_height))
e2 = np.random.normal(loc=200, scale=5.0, size=len(np_height))

np_height = np_height + e1
np_weight = np_weight + e2

np_baseball = np.column_stack((np_height, np_weight))
np_baseball.shape


help(sort_values())