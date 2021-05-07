import numpy as np
import pandas as pd

sales = pd.read_csv("sales_subset.csv")

sales_1_1 = sales[(sales['store'] == 1) & sales['department'] ==1]

# convert store types "supercenters," "discount stores," and "neighborhood markets" 
# to type "A," "B," and "C." respectively

if sales['type'] == "supercenters" : 
    sales['type'] == "A"
elif sales['type'] == "discount stores" :
    sales['type'] == 'B'
else: sales['type'] == 'C'
    