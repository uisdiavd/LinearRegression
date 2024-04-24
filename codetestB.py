import pandas as pd

# Load the dataset
df = pd.read_csv('top_200_youtubers.csv')

# Calculate the average likes for each country
country_avg_likes = df.groupby('Country')['Likes'].mean().reset_index()

# Calculate the expected views for the next 90 days
# Using the average of 'Avg. 1 Day' to 'Avg. 60 Day' views columns as a daily average,
# then multiplying by 90 to project the next 90 days
daily_avg_columns = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
df['Daily Avg Views'] = df[daily_avg_columns].mean(axis=1)
df['Expected Views 90 Days'] = df['Daily Avg Views'] * 90

# Calculate the average expected views for the next 90 days for each country
country_expected_views = df.groupby('Country')['Expected Views 90 Days'].mean().reset_index()

# Merge the two dataframes on 'Country'
result_df = pd.merge(country_avg_likes, country_expected_views, on='Country')
result_df.to_csv('OutputB.csv')