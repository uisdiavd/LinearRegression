#
"""
Prompt:
1. Create a new table with the countries on the list and the average likes of each channel in that country.
2. Add a column that shows the expected views for the next 90 days based on the trends found the Avg. 1 Day views up until the Avg. 60 Day views column.
"""

"""
Final output called with TableFunction().add_prediction_to_table(file, predict_at)
File should be a csv with columns 'Country' and views data for 'Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day' for YouTuber data
predict_at is the training value to predict the views data for
"""

import pandas as pd
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class YouTubeChannelDataManager:
    """ Manages data from raw input """
        
    def process_yt_channel_data(self, csv):
        """ Returns processed data as DataFrame """
        # Read the csv file into a DataFrame
        df = pd.read_csv(csv)

        # Set columns of target data
        cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
            
        # Set groupby_filter
        groupby_filter = 'Country'
        
        # Clean country formatting
        df['Country'] = df['Country'].str.strip()
        
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
    
    def extract_target_data_for_row(self, file, row):
        """ Extracts one row of data with a country and its view data """
        #
        # Returns target data as a list to enable iteration per country for null or zero values
        #
        
        cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
        dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
        data = dfr[cols].iloc[row].values.reshape(-1, 1)
        
        ## Test print
        #print(data)
        return data
    
    def clean_training_data(self, file, row):
        """ Returns array of training values matched with the non-zero target data and a list of removed indexes """
        # Pass in parameters from prep functions
        data = LinearRegressionDataPreparation().extract_target_data_for_row(file, row)
        removed_data_indexes = []
        
        ##Test print data being evaluated
        #print(data)
        
        # Define training data as a list for use with removing corresponding missing values from target data
        trainings = [1, 3, 7, 14, 30, 60]
        
        # Initialize adjustment variable for target list size decreasing after removing a value
        adjustment = 0

        # Iterate over data to clean null or zero values in target data and corresponding training data
        for l,d in enumerate(data):
            ## Test print for troubleshooting, displays index of value being evaluated
            #print('index evaluation: ', l)
            
            # If target data point is 0, then clean corresponding training value
            if data[l] == 0:
                ## Test print confirms that the if statement is running correctly
                #print('IDENTIFIED: \n Zero data row: ', row, '\n',  'Zero data index: ', l)

                # Targeted index accounts for changing length of target list after removing a value
                t = l - adjustment
                ##Test print training index for troubleshooting
                #print('training index: ', l)

                # Value to be removed from the training values list
                delvalue = trainings[t]
                trainings.remove(delvalue)
                
                ## Test print to show value of removed list member
                #print(f'Deleting value: {delvalue}')
                
                # Add index to removed_data_indexes dict
                removed_data_indexes.append(tuple((row, t)))
                
                ## Test print to show removed data indexes
                #print('removed_data_indexes: ', removed_data_indexes)

                # Test print with latest training value corresponding to target data zero value removed
                #print('trainings after zero removed: ', trainings)
                
                # Increase adjustment value to account for length of target list after removing a value
                adjustment += 1
                continue

            ## Test print data row number with final set of training values
            #print('Row: ', r)
            #print('training values: ', trainings)
            
            return trainings, removed_data_indexes
        
    def convert_to_dataframe(self, data):
        """ Converts array to dataframe """
        return pd.DataFrame(data)

    def clean_target_data(self, file, row):
        """ Returns target data after removing zero values. Use after cleaning training data """
        #
        # For use in for loop, pass in row iteration
        # Calls LinearRegressionDataPreparation().extract_target_data_for_row()
        # Passes to LinearRegressionDataPreparation().convert_to_dataframe()
        # Returns cleaned dataframe with target data
        #
        
        data = LinearRegressionDataPreparation().extract_target_data_for_row(file, row)
        
        # Convert target data to dataframe to enable removal of missing values
        y = LinearRegressionDataPreparation().convert_to_dataframe(data)
        
        # Clean zero values from target data dataframe
        y = y[y[0] != 0]#.reset_index()
            
        return y
        
class FitData:
    """ Forms a linear regression fit model """

    def insufficient_data_handling(self, file, row):
        """ Should continue if there is no target data to create a model from """
        checkdata = LinearRegressionDataPreparation().clean_target_data(file, row)[0].values
            
        #Troubleshooting test prints
        #print('checkdata type: ', type(checkdata))
        #print('checkdata: ', checkdata)
            
        if len(checkdata) <= 1:
            warnings.warn(f'Empty target data set skipped for row {row}', Warning)
        else:
            #print(f'The model will continue for row {row}')
            ##temporary pass until continuing to regression fit is functional
            #pass
            return FitData().linear_regression_model_fit(file, row)

    def linear_regression_model_fit(self, file, row):
        """ Generates a linear regression model fit for a row """
        
        # Initialize required data
        model = LinearRegression()

        trainings, testreturn = LinearRegressionDataPreparation().clean_training_data(file, row)
        X = LinearRegressionDataPreparation().convert_to_dataframe(trainings)
        y = LinearRegressionDataPreparation().clean_target_data(file, row)
        
        # Convert column names to strings 
        X.columns = X.columns.astype(str)
        y.columns = y.columns.astype(str)

        ## Test print dataframes
        #print('X: ', type(X), X, '\n')
        #print('y: ', type(y), y)
        
        ##Test print training and target data
        #print(f'training data: \n {X}')
        #print(f'target data: \n {y}')
        #return y
    
        # Linear regression model fit
        return model.fit(X, y)
    
    def linear_regression_prediction(self, file, row, predict_at):
        """ Predicts value for a specific training value """
        LRmodel = FitData().linear_regression_model_fit(file, row)
        coef = LRmodel.coef_[0][0]
        intercept = LRmodel.intercept_[0]
        
        prediction = coef * predict_at + intercept
        
        return prediction
    
class TableFunction:
    """ Table functions """
    def add_prediction_to_table(self, file, predict_at):
        data_range = range(YouTubeChannelDataManager().data_length(file))
        dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
        result = []
        for r in data_range:
            checkdata = LinearRegressionDataPreparation().clean_target_data(file, r)[0].values
            
            if len(checkdata) > 1:
                prediction = FitData().linear_regression_prediction(file, r, predict_at)
                result.append(prediction)
            else:
                result.append('0')
        
        dfr["90 Day Prediction"] = result
        
        return dfr
