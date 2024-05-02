import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

# Export for creating feature file
df = df.sort_values(by=['Country'])
df.to_csv('FeatureData.csv', sep='|')

"""
#Linear regression function test area

from sklearn.linear_model import LinearRegression

# Prepare data for regression
cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
views = df.groupby('Country')[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].mean()
dfr = pd.DataFrame(views).reset_index()

# Test print
#print('dfr: \n', dfr.head())

# Linear regression per country
model = LinearRegression()
y = pd.DataFrame([1, 3, 7, 14, 30, 60])
print(y)
# CSV export for feature
#y.to_csv('y_dataframe.csv')


for i in range(3): # len(dfr['Country'])):
    data = dfr[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[i].values.reshape(-1,1)
    X = pd.DataFrame(data)
"""
    # CSV export for feature (failed)
    #row = i
    #X.to_csv(f'x_dataframe-{i}.csv')
"""
    X = X.dropna()
    #print(type(X), "\n", X.head())
    #model.fit(X,y)
    #print(model.predict(X))

"""
