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

# Iterate over prepared data to extract training data for one country at a time
for r in range(len(dfr['Country'])):
    # Initialize training and target data for iteration to find null or zero values
    # Define training data as a list to enable iteration per country for null or zero values
    data = dfr[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[r].values.reshape(-1,1)
    
    # Define target data as a list for use with removing corresponding missing values from training data
    targets = [1, 3, 7, 14, 30, 60]

    # Initialize adjustment variable for target list size decreasing after removing a value
    adjustment = 0

# Iterate over data to clean null or zero values in training data and corresponding target data
    for l,d in enumerate(data):
        # Test print for troubleshooting, displays index of value being evaluated
#        print('l value: ', l)
   
        # If training data point is 0, then clean corresponding target value
        if data[l] == 0:
            # Test print confirms that the if statement is running correctly
#            print('Zero data row: ', r, '\n',  'Zero data index: ', l)
#            print('Adjustment: ', adjustment)

            # Targeted index accounts for changing length of target list after removing a value
            t = l - adjustment
#            print('Target index: ', t)

            # Value to be removed from the target values list
            delvalue = targets[t]
            targets.remove(delvalue)


            # Test print with latest target value corresponding to training data zero value removed
#            print('Targets after zero removed: ', targets)

            # Increase adjustment value to account for length of target list after removing a value
            adjustment += 1

        # Print data row number with final set of target values
#        print('Row: ', r)
#        print('Target values: ', targets)

    # Convert target values into a dataframe
    y = pd.DataFrame(targets)

    # Clean zero values from training data
#    data.remove(0)
    # Convert training data to dataframe to enable removal of missing values
    X = pd.DataFrame(data)
    # Clean missing values from training data dataframe
#    X = X.dropna()
    X = X[X[0] != 0].reset_index()

    # Convert column names to strings
    X.columns = X.columns.astype(str)
    y.columns = y.columns.astype(str)

    # Test print dataframes
    print('X: ', type(X), X, '\n')
    print('y: ', type(y), y)

    # Linear regression model fit
    model.fit(X,y)

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