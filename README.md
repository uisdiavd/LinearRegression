-- ABOUT --
Personal project from scratch to prepare data from a csv, perform linear regression to predict values, and output a table with the predicted values.

== RUN INSTRUCTIONS ==
Linear regression runs on the provided file via test cases (nosetests) as a baseline case for the program. Modifying the provided csv file will break the test cases.
======================

-- DEVELOPMENT --
Future functionality to input a file is anticipated (last updated: 05/2024).

-- NOTES -- 
Current function is rigid
  -requires exact column names ['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']
  -requires corresponding day intervals (1, 3, 7, 14, 30, 60)
Current function will account for null values in the data.


Data file provided by Kaggle, and used under the CC0 Public Domain license.
