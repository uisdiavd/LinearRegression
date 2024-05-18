""" Testing calls to main model """

import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData
from service import app

file = 'top_200_youtubers.csv'
row = 2

print(f'row: {row}')

data = LinearRegressionDataPreparation().extract_target_data_for_row(file, row)
print(f'data: \n {data}')

#y = LinearRegressionDataPreparation().clean_target_data(file, row)
#print(f'y: {y}')

trainings, testreturn = LinearRegressionDataPreparation().clean_training_data(file, row)
clean = LinearRegressionDataPreparation().convert_to_dataframe(trainings)
print(f'clean: {clean}')

printthis = FitData().linear_regression_model_fit(file, row)
print(printthis)