import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

from sklearn.linear_model import LinearRegression

# fill missing `Country` values
df['Country'] = df['Country'].fillna('Unknown')

# calculate average likes per country
avg_likes = df.groupby('Country')['Likes'].mean()
#print(avg_likes)

df_out = pd.DataFrame(avg_likes).reset_index().rename(columns={'Likes': 'Avg. Likes'})

# Prepare data for regression
X = df[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']]
y = df['Avg. 60 day']

print('X type: \n', type(X))
#print("X: ", X.info())
#print("Y: ", y.info())

"""
# Drop rows with any missing values
X = X.dropna()
y = y.loc[X.index]

print("X2: ", X.info())
print("Y2: ", y.info())
"""
"""
# Linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict views for next 30, 60, 90 days (assuming linear trend holds)
last_day_data = df[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[-1].values
next_30_days_pred = model.predict([last_day_data + 30])
next_60_days_pred = model.predict([last_day_data + 60])
next_90_days_pred = model.predict([last_day_data + 90])

# Add the predictions to the dataframe
df_out['Expected Views (Next 90 Days)'] = next_90_days_pred[0]

# Display the data
print(df_out.head())
df_out.to_csv('ExportA.csv')
"""