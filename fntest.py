import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

"""
# Export for creating feature file
df = df.sort_values(by=['Country'])
df.to_csv('FeatureData.csv', sep='|')
"""

#Linear regression function test area
from sklearn.linear_model import LinearRegression

# Prepare data for regression
cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
views = df.groupby('Country')[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].mean().fillna(0)
dfr = pd.DataFrame(views).reset_index()

# Test print
#print('dfr: \n', dfr.head())

# Linear regression per country
model = LinearRegression()
"""
# Defining target data without accounting for missing values in training data
y = pd.DataFrame([1, 3, 7, 14, 30, 60])
#print(y)
# CSV export for feature
#y.to_csv('y_dataframe.csv')
"""

# Iterate over prepared data to extract training data for one country at a time
for r in range(len(dfr['Country'])): # This is a per-row iterative
    print('r = ', r)
    # Initialize training and target data for iteration to find null or zero values
    # Define training data as a list to enable iteration per country for null or zero values
    data = dfr[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[r].values.reshape(-1,1)

    # Test print confirms that 'data' can be used with indexes
    #print("data[0]: ", data[0])

    # Define target data as a list for use with removing corresponding missing values from training data
    targets = [1, 3, 7, 14, 30, 60]
    
    # Test prints confirm target data can be used with indexes
    #print(type(targets))
    #print(targets[0])
    
    # Working conditional statement:
    # Iterate over training data to find null values and remove corresponding values from target data
    # Test print
    #print('len(data)', len(data))
    
    #x Set r as list-iterative variable
    #xl = 0
    
    # Adjustment for target list size decreasing after removing a value
    adjustment = 0

# Iterate over data to clean null or zero values in training data and corresponding target data
#x   if l <= len(data):    
#   for l in enumerate(data): runs into indices error
#   for l in range(len(data)): runs into index out of range error
    for l,d in enumerate(data):
        print('l value: ', l)

        # If 0, then clean corresponding value
        if data[l] == 0:
            # Test print confirms that the if statement is running correctly
            print('Zero data row: ', r, '\n',  'Zero data index: ', l)
            print('Adjustment: ', adjustment)

            # Targeted index accounts for changing length of target list after removing a value
            t = l - adjustment
            print('Target index: ', t)

            # Value to be removed from the target values list
            delvalue = targets[t]
            targets.remove(delvalue)

            # Test print
            print('Targets after zero removed: ', targets)

            adjustment += 1
        
        #xIncrease iterative to move to evaluate next row in training data
        #xl += 1
"""
        # turn targets into a dataframe for use with lr model after removing data corresponding to null values in target data set
        y = pd.DataFrame(targets)
        # Test prints
        #print(type(y))
        #print(y)
    
    # Convert training data to dataframe to enable removal of missing values
    X = pd.DataFrame(data)
    # Clean missing values from training data dataframe
    X = X.dropna()
    # Test prints
    print(
        'Iteration: ', i,
        '\n X: \n', X,
        '\n y: \n', y
    )
    #print(type(X), "\n", X.head())
    #model.fit(X,y)
    #print(model.predict(X))


"""