#
"""
Prompt:
Please create a new table with the countries on the list and the average likes of each channel in that country.
Next, add a column that shows the expected views for the next 90 days based on the trends found the Avg. 1 Day views up until the Avg. 60 Day views column.
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

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
    for l in range(len(data)):
        # Test print for troubleshooting, displays index of value being evaluated
#        print('l value: ', l)
   
        # If nan, then clean corresponding value
        # Initialize nancheck to iterate over training data list
        nancheck = np.isnan(data[l])

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
        print('Row: ', r)
        print('Target values: ', targets)
        
"""
Generated code
#print("X: ", X.info())
#print("Y: ", y.info())


# Drop rows with any missing values
X = X.dropna()
y = y.loc[X.index]

#print("X2: ", X.info())
#print("Y2: ", y.info())
#X.to_csv('xclean.csv')
#y.to_csv('yclean.csv')


# Linear regression model
model = LinearRegression()
model.fit(X, y)


# Predict views for next 30, 60, 90 days (assuming linear trend holds)
last_day_data = df[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[-1].values

# User check
print(last_day_data)

next_90_days_pred = model.predict([last_day_data + 90])

#print(next_90_days_pred)
"""
"""
# Add the predictions to the dataframe
df_out['Expected Views (Next 90 Days)'] = next_90_days_pred[0]

# Display the data
print(df_out.head())
df_out.to_csv('ExportA.csv')
"""