""" Testing calls to main model """

import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData
from service import app

file = 'top_200_youtubers.csv'
row = 0

print('row: ', row)


#dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
#print(dfr.head())

# LinearRegressionDataPreparation().clean_target_data(file, row)

LRmodel = FitData().linear_regression_model_fit(file, row)
print(f'LR model: {LRmodel}')

coef = LRmodel.coef_
print(f'coef: {coef}')
print('coeflength for index 0: ', len(coef[0]))
coeftype = type(coef)
print(f'coef type: {coeftype}')

intercept = LRmodel.intercept_
print(f'intercept: {intercept}')
itype = type(intercept)
print(f'intercept type: {itype}')