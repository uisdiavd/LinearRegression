"""
Test cases for linear regression data preparation

Test cases should be run with
    nosetests
    coverage report -m

"""

import unittest
import logging
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation
from service import app

class TestYouTubeChannelDataManager(unittest.TestCase):
    """ Test if it manages data from raw input """
    
    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.logger.setLevel(logging.ERROR)
        
    def setUp(self):
        # Test data setup
        file = 'top_200_youtubers.csv'
        data_manager = YouTubeChannelDataManager()
        self.dfr = data_manager.process_yt_channel_data(file)
        
    # # # # # # # #
    # TEST CASES  #
    # # # # # # # #
    
    def test_process_yt_channel_data(self):
        """ Test if only one entry exists for each country when preparing the 'top_200_youtubers.csv' file """
        dfr = self.dfr
                 
        # Testing that only one entry exists for each country
        start = 1
        for country in dfr['Country']:
            length = len(dfr['Country'])
            app.logger.info("Looking for duplicates of country %s", country)
            self.assertNotIn(country, dfr['Country'].values[start:length], "Multiple of country entry found")
            start += 1

class TestLinearRegressionDataPreparation(unittest.TestCase):
    """Test cases for linear regression data preparation"""
    
    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.logger.setLevel(logging.INFO)
        
    def setUp(self):
        # Test data setup
        file = 'top_200_youtubers.csv'
        self.file = file
        data_manager = YouTubeChannelDataManager()
        self.dfr = data_manager.process_yt_channel_data(file)
        self.lrprep = LinearRegressionDataPreparation()
        
    # # # # # # # #
    # TEST CASES  #
    # # # # # # # #

    def test_null_to_zero(self):
        """ Test that null values are converted to zero from the managed data set """
        file = self.file
        data_range = range(YouTubeChannelDataManager().data_length(file))
        lrprep = self.lrprep
        
        for r in data_range:
            data = lrprep.extract_training_data_for_row(file, r)
            for l,d in enumerate(data):
                ## Troubleshooting print: index of value being evaluated
                #print('l value: ', l)

                for entry in data:
                    ## Troubleshooting print: entry value being evaluated
                    #print(entry)
                    self.assertIsNotNone(entry)
    
    def test_missing_data_handling(self):
        """It should remove null and zero values from training data and the corresponding target data"""
        # Initialize variables
        file = self.file
        data_range = range(YouTubeChannelDataManager().data_length(file))
        lrprep = self.lrprep
        
        for r in data_range:
            checkdata = lrprep.clean_target_data(file, r)
            for entry in checkdata:
                self.assertNotEqual(entry, 0, f'A zero value is still present in the training data for row {r}')
        
        raise NotImplementedError('Target data still needs to be tested for removal of corresponding missing data')
    
#    def test_convert_to_dataframe(self):
#        """Test that the model should return dataframes for both training and target data"""
#        
#        data_length = YouTubeChannelDataManager().data_range(file)
#             
#        for r in data_length:
#            convertdata = LinearRegressionDataPreparation().extract_training_data_for_row(r)
#            data = LinearRegressionDataPreparation().convert_to_dataframe(convertdata)
#            checkdata = type(data)
#            self.assertEqual(f"{checkdata}", "<class 'pandas.core.frame.DataFrame'>", "Object 'data' not converted to a DataFrame")
#
#            converttargets = LinearRegressionDataPreparation().match_target_to_training_dimension(self, file, r)
#            targets = LinearRegressionDataPreparation().convert_to_dataframe(converttargets)
#            checktargets = type(targets)
#            self.assertEqual(f"{checktargets}", "<class 'pandas.core.frame.DataFrame'>", "Object 'targets' not converted to a DataFrame")
    

#    
#    def test_zero_data_handling(self):
#        """It should skip linear regression model fitting when training dataframe is empty"""
#        raise NotImplementedError('Not implemented yet')
#
#class TestLinearRegression: