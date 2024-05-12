"""
Test cases for linear regression data preparation

Test cases should be run with
    nosetests
    coverage report -m

"""

import unittest
import logging
from service.models import YouTubeChannelDataManager
from service import app

class TestYouTubeChannelDataManager(unittest.TestCase):
    """ Test if it manages data from raw input """
    
    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.logger.setLevel(logging.INFO)
    #
    # Test cases
    #
    
    def test_process_yt_channel_data(self, CSV = 'top_200_youtubers.csv'):
        """ Test if only one entry exists for each country when preparing the 'top_200_youtubers.csv' file """
        self.csv = CSV
        data_manager = YouTubeChannelDataManager()
        dfr = data_manager.process_yt_channel_data(self.csv)
        
        # Testing that only one entry exists for each country
        start = 1
        for country in dfr['Country']:
            length = len(dfr['Country'])
            logging.info("Looking for duplicates of country %s", country)
            self.assertNotIn(country, dfr['Country'].values[start:length], "Multiple of country entry found")
            start += 1
#
#    def test_avgviews_data_filter(self):
#        """It should create a table with only views data in it"""
#        raise NotImplementedError('Not implemented yet')
#
#    def test_avgviews_by_country(self):
#        """It should combine the data from avgviewsdatafilter by country"""
#        raise NotImplementedError('Not implemented yet')
#class TestLinearRegressionDataPreparation(unittest.TestCase):
#    """Test cases for linear regression data preparation"""
#    
#    def test_convert_to_dataframe(self):
#        """It should return dataframes for both training and target data"""
#        raise NotImplementedError('Not implemented yet')
#    
#    def test_missing_data_handling(self):
#        """It should remove null and zero values from training data and the corresponding target data"""
#        raise NotImplementedError('Not implemented yet')
#    
#    def test_zero_data_handling(self):
#        """It should skip linear regression model fitting when training dataframe is empty"""
#        raise NotImplementedError('Not implemented yet')
#
#class TestLinearRegression: