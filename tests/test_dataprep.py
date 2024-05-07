"""
Test cases for linear regression data preparation

Test cases should be run with
    nosetests
    coverage report -m

"""

import unittest
import logging
from service.models import YouTubeChannelDataManager

class TestYouTubeChannelDataManager(unittest.TestCase):
    """ Test if it manages data from raw input """
    def test_process_yt_channel_data(self):
        """ Test if it prepares views data by country with 'top_200_youtubers.csv' file """
        CSV = 'top_200_youtubers.csv'
        data_manager = YouTubeChannelDataManager(CSV)
        data_manager.process_yt_channel_data(CSV)

#class TestAverageViewsLinearRegressionDataPreparation(unittest.TestCase):
#    """Test cases for linear regression data preparation"""
#
#    def test_avgviews_data_filter(self):
#        """It should create a table with only views data in it"""
#        pass
#    
#    def test_avgviews_by_country(self):
#        """It should combine the data from avgviewsdatafilter by country"""
#        pass
#    
#    def test_convert_to_dataframe(self):
#        """It should return dataframes for both training and target data"""
#        pass
#    
#    def test_missing_data_handling(self):
#        """It should remove null and zero values from training data and the corresponding target data"""
#        pass
#    
#    def test_zero_data_handling(self):
#        """It should skip linear regression model fitting when training dataframe is empty"""
#        pass
