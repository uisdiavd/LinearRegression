""" Testing calls to main model """

import logging
import warnings
from service.models import YouTubeChannelDataManager, LinearRegressionDataPreparation, FitData
from service import app
import pandas as pd

file = 'top_200_youtubers.csv'

#""" Test if only one entry exists for each country when preparing the 'top_200_youtubers.csv' file """
#dfr = YouTubeChannelDataManager().process_yt_channel_data(file)
#            
## Testing that only one entry exists for each country
#start = 1
#for country in dfr['Country']:
#    print(f"Testing country {country}")
#    length = len(dfr['Country'])
#    app.logger.info("Looking for duplicates of country %s", country)
#    if country in dfr['Country'].values[start:length]:
#        print(f"Multiple of country entry found for {country}")
#        break
#    else:
#        start += 1
    
df = pd.read_csv(file)

# Set columns of target data
cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
counter = 1

# Set groupby_filter
groupby_filter = 'Country'

# Clean country formatting
for country in df['Country']:
    df['Country'][counter] = str(country).strip()
    print(counter, country)
    counter += 1

views = df.groupby(groupby_filter)[cols].mean().fillna(0)
dfr = pd.DataFrame(views).reset_index()
print(dfr)