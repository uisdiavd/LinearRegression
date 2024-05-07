#
"""
Prompt:
Please create a new table with the countries on the list and the average likes of each channel in that country.
Next, add a column that shows the expected views for the next 90 days based on the trends found the Avg. 1 Day views up until the Avg. 60 Day views column.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

"""
class YouTubeChannel:
    def __init__(self, csv):
        self.Country
        self.Avg. 1 Day
        self.Avg. 3 Day
        self.Avg. 7 Day
        self.Avg. 14 Day
        self.Avg. 30 day
        self.Avg. 60 day
    
    def load
"""

class YouTubeChannelDataManager:
    """ Manages data from raw input """
    def __init__(self, file):
        self.yt_channel_data = []
        self.file = file
        
    def process_yt_channel_data(self, CSV):
        """ Returns length of processed data """
        # Read the CSV file into a DataFrame
        df = pd.read_csv(CSV)

        # Set columns of training data
        cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
            
        # Set groupby_filter
        groupby_filter = 'Country'
        
        # Prepare data for regression
        views = df.groupby(groupby_filter)[cols].mean().fillna(0)
        dfr = pd.DataFrame(views).reset_index()
        
        print('Number of countries: ', len(dfr[groupby_filter]))
        return len(dfr[groupby_filter])
    
    def convert_to_dataframe(self):
        for r in range(len(dfr[groupby_filter])):
            # Initialize training and target data for iteration to find null or zero values
            # Define training data as a list to enable iteration per country for null or zero values
            data = dfr[cols].iloc[r].values.reshape(-1, 1)
            # Test print
            #print(data)
        
        
"""
class LinearRegression(df):

    # Test print
    #print('dfr: \n', dfr.head())

    # Linear regression per country
    model = LinearRegression()

    # Iterate over prepared data to extract training data for one country at a time


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

            # Test print data row number with final set of target values
    #        print('Row: ', r)
    #        print('Target values: ', targets)

        # Convert target values into a dataframe
        y = pd.DataFrame(targets)

        # Convert training data to dataframe to enable removal of missing values
        X = pd.DataFrame(data)
        # Clean zero values from training data dataframe
        X = X[X[0] != 0].reset_index()

        # Convert column names to strings
        X.columns = X.columns.astype(str)
        y.columns = y.columns.astype(str)

        # Test print dataframes
        print('X: ', type(X), X, '\n')
        print('y: ', type(y), y)

        # Linear regression model fit
    #    model.fit(X,y)
"""