#
"""
Prompt:
Please create a new table with the countries on the list and the average likes of each channel in that country.
Next, add a column that shows the expected views for the next 90 days based on the trends found the Avg. 1 Day views up until the Avg. 60 Day views column.
"""

import pandas as pd
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#
#class YouTubeChannel:
#    def __init__(self, csv):
#        self.Country
#        self.Avg. 1 Day
#        self.Avg. 3 Day
#        self.Avg. 7 Day
#        self.Avg. 14 Day
#        self.Avg. 30 day
#        self.Avg. 60 day
#    
#    def load
#

class YouTubeChannelDataManager:
    """ Manages data from raw input """
        
    def process_yt_channel_data(self, csv):
        """ Returns processed data as DataFrame"""
        # Read the csv file into a DataFrame
        df = pd.read_csv(csv)

        # Set columns of training data
        cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
            
        # Set groupby_filter
        groupby_filter = 'Country'
        
        # Prepare data for regression
        views = df.groupby(groupby_filter)[cols].mean().fillna(0)
        dfr = pd.DataFrame(views).reset_index()
        
        return dfr
    
    def data_length(self, file):
        """ Returns length of processed data """
        dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
        
        # Set groupby_filter
        groupby_filter = 'Country'
        
        return len(dfr[groupby_filter])

class LinearRegressionDataPreparation:
    """ Prepares data for linear regression"""
    
    def extract_training_data_for_row(self, file, row):
        """ Extracts one row of data with a country and its view data """
        #
        # Returns training data as a list to enable iteration per country for null or zero values
        #
        
        cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
        dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
        data = dfr[cols].iloc[row].values.reshape(-1, 1)
        
        ## Test print
        #print(data)
        return data
    
    def clean_target_data(self, file, row):
        """ Returns array of target values matched with the non-zero training data and a list of removed indexes """
        # Pass in parameters from prep functions
        data = LinearRegressionDataPreparation().extract_training_data_for_row(file, row)
        removed_data_indexes = []
        
        # Define target data as a list for use with removing corresponding missing values from training data
        targets = [1, 3, 7, 14, 30, 60]

        # Initialize adjustment variable for target list size decreasing after removing a value
        adjustment = 0
        
        # Iterate over data to clean null or zero values in training data and corresponding target data
        for l,d in enumerate(data):
            ## Test print for troubleshooting, displays index of value being evaluated
            #print('l value: ', l)
            
            # If training data point is 0, then clean corresponding target value
            if data[l] == 0:
                ## Test print confirms that the if statement is running correctly
                #print('Zero data row: ', row, '\n',  'Zero data index: ', l)
                #print('Adjustment: ', adjustment)

                # Targeted index accounts for changing length of target list after removing a value
                t = l - adjustment
                ##Test print target index for troubleshooting
                #print('Target index: ', t)

                # Value to be removed from the target values list
                delvalue = targets[t]
                targets.remove(delvalue)
                
                # Add index to removed_data_indexes dict
                removed_data_indexes.append(tuple((row, l)))
                #print('removed_data_indexes: ', removed_data_indexes)

                ## Test print with latest target value corresponding to training data zero value removed
                #print('Targets after zero removed: ', targets)

                # Increase adjustment value to account for length of target list after removing a value
                adjustment += 1

            ## Test print data row number with final set of target values
            #print('Row: ', r)
            #print('Target values: ', targets)
            return targets, removed_data_indexes

    def convert_to_dataframe(self, data):
        """ Converts array to dataframe """
        return pd.DataFrame(data)

    def clean_training_data(self, file, row):
        """ Returns training data after removing zero values. Use after cleaning target data """
        #
        # For use in for loop, pass in row iteration
        # Calls LinearRegressionDataPreparation().extract_training_data_for_row()
        # Passes to LinearRegressionDataPreparation().convert_to_dataframe()
        # Returns cleaned dataframe with training data
        #
        
        data = LinearRegressionDataPreparation().extract_training_data_for_row(file, row)
        
        # Convert training data to dataframe to enable removal of missing values
        X = LinearRegressionDataPreparation().convert_to_dataframe(data)
        
        # Clean zero values from training data dataframe
        X = X[X[0] != 0].reset_index()
            
        return X
        
class FitData:
    """ Forms a linear regression fit model """

    def checkskip(self, file):
        """ Should continue if there is no training data to create a model from """
        
        data_range = range(YouTubeChannelDataManager().data_length(file))
        for r in data_range:
            checkdata = LinearRegressionDataPreparation().clean_training_data(file, r)[0].values
            
            #Troubleshooting test prints
            #print('checkdata type: ', type(checkdata))
            print('checkdata: ', checkdata)
            
            if len(checkdata) == 0:
                warnings.warn(f'Empty training data set skipped for row {r}', Warning)
                continue
            else:
                print(f'The model will continue for row {r}')
                #FitData().linear_regression_model_fit(file)

#    def linear_regression_model_fit(self, file):
#        # Initialize required data
#        model = LinearRegression()
#        data_range = range(YouTubeChannelDataManager().data_length(file))
#             
#        for r in data_range:
#            targets = LinearRegressionDataPreparation().clean_target_data(file, r)
#            y = LinearRegressionDataPreparation.convert_to_dataframe(targets)
#
#            X = LinearRegressionDataPreparation().clean_training_data()
#            
#            # Convert column names to strings 
#            X.columns = X.columns.astype(str)
#            y.columns = y.columns.astype(str)
#
#            ## Test print dataframes
#            #print('X: ', type(X), X, '\n')
#            #print('y: ', type(y), y)
#
#            ## Linear regression model fit
#            #model.fit(X,y)