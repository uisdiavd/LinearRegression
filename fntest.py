""" Testing calls to main model """

import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData, TableFunction
from service import app
import pandas as pd

file = 'top_200_youtubers.csv'

print(TableFunction().add_prediction_to_table(file, predict_at=90))