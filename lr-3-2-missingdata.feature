Feature: Linear Regression with missing data

As a programming data analyst
I need a linear regression function that handles multiple data points for a single category with a variable number of training values
So that I can predict a future value of any of the categories with a valid number of training data points based on the given data

Background:
    Given the appropriately prepared data for linear regression on average views of a country from a given data set
    | Country   | Avg. 1 Day    | Avg. 3 Day    | Avg. 7 Day    | Avg. 14 Day   | Avg. 30 day   | Avg. 60 day   |
    

Scenario: Linear regression with missing data in given data set
Given a data set with multiple data points for a category
And some of the categories have no data for a given target value
When I run the linear regression program on the given data set
And use the model to predict a data point on a future target
Then the program should output the correct prediction value