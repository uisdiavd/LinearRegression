"""
Test cases for linear regression data preparation

Test cases should be run with
    nosetests
    coverage report -m

"""

import unittest
import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData
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
            data = lrprep.extract_target_data_for_row(file, r)
            for l,d in enumerate(data):
                ## Troubleshooting print: index of value being evaluated
                #print('l value: ', l)

                for entry in data:
                    ## Troubleshooting print: entry value being evaluated
                    #print(entry)
                    self.assertIsNotNone(entry)

    def test_missing_training_data_handling(self):
        """ It should remove training data corresponding to null and zero values from training data """
        
        # Initialize variables
        file = self.file
        data_length = YouTubeChannelDataManager().data_length(file)
        data_range = range(data_length)
        lrprep = self.lrprep
        
        # Check cleaned training data
        for r in data_range:
            # Skip if data has insufficient length
            if len(lrprep.clean_target_data(file, r)) <= 1:
                continue
            
            checkdata, removed_data_indexes = lrprep.clean_training_data(file, r)
            data = LinearRegressionDataPreparation().extract_target_data_for_row(file, r)
            
            ## Test prints
            #print('row: ', r)
            #print('checkdata: ', checkdata)
            #print('data: ', data)
            #print('rdi: ', removed_data_indexes)

            self.assertEqual(len(checkdata), len(data) - len(removed_data_indexes))
    
    def test_convert_to_dataframe(self):
        """Test that the model should return dataframes for both target and training data"""
        # Initialize variables
        file = self.file
        data_range = range(YouTubeChannelDataManager().data_length(file))
             
        for r in data_range:
            convertdata = LinearRegressionDataPreparation().clean_target_data(file, r)
            data = LinearRegressionDataPreparation().convert_to_dataframe(convertdata)
            checkdata = type(data)
            self.assertEqual(f"{checkdata}", "<class 'pandas.core.frame.DataFrame'>", "Object 'data' not converted to a DataFrame")

            converttrainings = LinearRegressionDataPreparation().clean_training_data(file, r)
            trainings = LinearRegressionDataPreparation().convert_to_dataframe(converttrainings)
            checktrainings = type(trainings)
            self.assertEqual(f"{checktrainings}", "<class 'pandas.core.frame.DataFrame'>", "Object 'trainings' not converted to a DataFrame")
    
    def test_missing_target_data_handling(self):
        """ It should remove null and zero values from target data """
        #
        # Set up file, use to define data range, use in entry iteration for loop
        # Entry iteration calls lrprep.clean_target_data() 
        # and checks for existence of value 0
        #
        
        # Initialize variables
        file = self.file
        data_range = range(YouTubeChannelDataManager().data_length(file))
        lrprep = self.lrprep
        
        # Check cleaned target data
        for r in data_range:
            checkdata = lrprep.clean_target_data(file, r)[0].values
            
            ##Troubleshooting test prints
            #print('checkdata type: ', type(checkdata))
            #print('checkdata: ', checkdata)
            
            self.assertNotIn(0, checkdata, f'A zero value is still detected in the target data for row {r}')
    
class TestLinearRegression(unittest.TestCase):
    """ Test functionality of linear regression """
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
        self.data_manager = YouTubeChannelDataManager()
        self.lrprep = LinearRegressionDataPreparation()
        
    # # # # # # # #
    # TEST CASES  #
    # # # # # # # #
    
    def test_insufficient_data_handling(self):
        """ It should skip linear regression model fitting when target dataframe is empty """
        
        # Initialize variables
        file = self.file
        data_manager = self.data_manager
        data_range = range(data_manager.data_length(file))
        lrprep = self.lrprep
        
        # Check if linear regression model fitting is skipped for insufficient target data rows
        for r in data_range:
            checkdata = lrprep.clean_target_data(file, r)[0].values
            #checkreturn = FitData().insufficient_data_handling(file, r)
            #Troubleshooting test prints
            #print('checkdata type: ', type(checkdata))
            #print('checkdata: ', checkdata)
            
            
            if len(checkdata) <= 1:
                ## Print to check that empty rows are skipped
                #print('checkdata: ', checkdata)
                #print(f"Row {r} should be skipped for having insufficient target data")
                #print(f'Checkdata for row {r} identified as <= 1')
                with warnings.catch_warnings(record = True) as w:
                    FitData().insufficient_data_handling(file, r)
                    assert len(w) > 0
            
    def test_lr_model_first_coeff_and_intercept(self):
        """ It should return an accurate coefficient and intercept from the linear regression model fit """
        
        # Initialize variables
        file = self.file
        
        row = 0
        LRmodel = FitData().linear_regression_model_fit(file, row)
        coef = LRmodel.coef_[0][0]
        intercept = LRmodel.intercept_[0]
        
        self.assertAlmostEqual(36905.64154215,coef)
        self.assertAlmostEqual(557929.72167922, intercept)
        
    def test_linear_regression_model_fit(self):
        """ For each row, the coeff and intercept should be arrays of length 1 """
        file = self.file
        lrprep = self.lrprep
        
        #Initialization for iterating through rows
        data_manager = self.data_manager
        data_range = range(data_manager.data_length(file))
        
        for r in data_range:
            # Skip if data has insufficient length
            if len(lrprep.clean_target_data(file, r)) <= 1:
                continue
            
            LRmodel = FitData().insufficient_data_handling(file, r)
            coef = LRmodel.coef_
            intercept = LRmodel.intercept_
            coeftype = type(coef)
            itype = type(intercept)
            self.assertEqual(f'{coeftype}', "<class 'numpy.ndarray'>")
            self.assertEqual(f'{itype}', "<class 'numpy.ndarray'>")
            self.assertEqual(len(coef), 1)
            self.assertEqual(len(intercept), 1)
            
    def test_linear_regression_prediction(self):
        """ It should return an accurate prediction """
        file = self.file
        row = 0
        predict_at = 90
        
        #LRmodel = FitData().linear_regression_model_fit(file, row)
        #coef = LRmodel.coef_[0][0]
        #intercept = LRmodel.intercept_[0]
        
        #prediction90 = coef * predict_at + intercept
        prediction90 = FitData().linear_regression_prediction(file, row, predict_at)
        
        self.assertAlmostEqual(prediction90, 3879437.46, places = 3)
