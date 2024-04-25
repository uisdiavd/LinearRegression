import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('top_200_youtubers.csv')

from sklearn.linear_model import LinearRegression

# Prepare data for regression
cols = ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
views = df.groupby('Country')[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].mean()
dfr = pd.DataFrame(views).reset_index()

# Test print
print('dfr: \n', dfr.head())

# Linear regression per country
model = LinearRegression()
y = pd.DataFrame([1, 3, 7, 14, 30, 60])
for i in range(len(dfr['Country'])):
    data = dfr[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[1].values.reshape(-1,1)
    X = pd.DataFrame(data)
    X = X.dropna()
    print(type(X))
    #model.fit(X,y)
    #print(model.predict(X))
    





"""
#print("X: ", X.info())
#print("Y: ", y.info())


# Drop rows with any missing values
X = X.dropna()
y = y.loc[X.index]

#print("X2: ", X.info())
#print("Y2: ", y.info())
#X.to_csv('xclean.csv')
#y.to_csv('yclean.csv')


# Linear regression model
model = LinearRegression()
model.fit(X, y)


# Predict views for next 30, 60, 90 days (assuming linear trend holds)
last_day_data = df[['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']].iloc[-1].values

# User check
print(last_day_data)

next_90_days_pred = model.predict([last_day_data + 90])

#print(next_90_days_pred)
"""
"""
# Add the predictions to the dataframe
df_out['Expected Views (Next 90 Days)'] = next_90_days_pred[0]

# Display the data
print(df_out.head())
df_out.to_csv('ExportA.csv')
"""