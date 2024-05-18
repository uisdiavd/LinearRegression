""" Testing calls to main model """

import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData
from service import app

file = 'top_200_youtubers.csv'
row = 6

data = LinearRegressionDataPreparation().extract_target_data_for_row(file, row)
print(data)

printthis = FitData().insufficient_data_handling(file, row)
print(printthis)