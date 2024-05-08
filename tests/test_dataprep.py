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
        """ Then there should be a new dataset with only the following columns: 'Country', 'Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day'
            And there should only be one row of data for the country 'AE'
            And there should only be one row of data for the country 'AR'
            And there should only be one row of data for the country 'AU'
        """
        CSV = 'top_200_youtubers.csv'
        data_manager = YouTubeChannelDataManager()
        data_manager.process_yt_channel_data(CSV)

    def test_avgviews_data_filter(self):
        """It should create a table with only views data in it"""
        raise NotImplementedError('Not implemented yet')

    def test_avgviews_by_country(self):
        """It should combine the data from avgviewsdatafilter by country"""
        raise NotImplementedError('Not implemented yet')
class TestLinearRegressionDataPreparation(unittest.TestCase):
    """Test cases for linear regression data preparation"""
    
    def test_convert_to_dataframe(self):
        """It should return dataframes for both training and target data"""
        raise NotImplementedError('Not implemented yet')
    
    def test_missing_data_handling(self):
        """It should remove null and zero values from training data and the corresponding target data"""
        raise NotImplementedError('Not implemented yet')
    
    def test_zero_data_handling(self):
        """It should skip linear regression model fitting when training dataframe is empty"""
#        raise NotImplementedError('Not implemented yet')

#class TestLinearRegression: