Feature: Linear regression for average views program should convert training data into a dataframe for use in the linear regression model

As a programmer for the linear regression program anlyzing average views data
I need the training data can be converted to a dataframe 
So that null values can be cleared

Background:
    Given the appropriately prepared training data array for linear regression on average views of a single country from an original data set
    | 46422.            |
    | 575767.91666667   |
    | 1048158.95        |
    | 1480758.33193277  |
    | 1887680.20168067  |
    | 2552939.70714286  |


Scenario: Convert to dataframe
Given the prepared training data array
When it is extracted as an array
Then the it should be converted into a dataframe