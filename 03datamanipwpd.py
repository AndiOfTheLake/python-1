import numpy as np
import pandas as pd

sales = pd.read_csv("sales_subset.csv")

sales_1_1 = sales[(sales['store'] == 1) & sales['department'] ==1]

# convert store types "supercenters," "discount stores," and "neighborhood markets" 
# to type "A," "B," and "C." respectively

for i in range(len(sales['type'])) : 
    if sales['type'].rename == "supercenters" : 
        sales['type'][i] == "A"
    elif sales['type'][i] == "discount stores" : 
        sales['type'][i] == 'B'
    else: sales['type'][i] == 'C'

print(sales.head()['type'])

# load temperatures data set
temperatures = pd.read_csv('temperatures.csv', parse_dates=[col], encoding='utf-8-sig', usecols= ['Date', 'ids'])


temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    "avg_temp_c", index = ['country', 'city'], columns = 'year'
)

# See the result
print(temp_by_country_city_vs_year)

avocados = pd.read_pickle('avoplotto.pkl')
avocados_2016 = avocados[avocados['year'] == '2016']
avocados_2016.shape

avocados['year'].info()
