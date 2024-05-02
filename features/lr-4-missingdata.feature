Feature: Linear regression for average views program should handle null values for average views

As a programmer for the linear regression program anlyzing average views data 
I need null values dropped from training dataframe
And the target dataframe to have integers corresponding to the available average views data for the same country
So that the dimensions of the target dataframe and training dataframe match for use in a linear regression model

Background:
    Given a dataframe with missing data
    
Scenario: One null value
Given a prepared training data set for linear regression on average views of a single country
And the first value in the training data is null
When null values are dropped from the training dataframe
Then there should be no null data in the training dataframe
And the target data set should be 
|     | 0   |
| 0   | 3   |
| 1   | 7   |
| 2   | 14  |
| 3   | 30  |
| 4   | 60  |

Scenario: Two null values
Given a prepared training data set for linear regression on average views of a single country
And the first two values in the training data is null
When null values are dropped from the training dataframe
Then there should be no null data in the training dataframe
And the target data set should be 
|     | 0   |
| 0   | 7   |
| 1   | 14  |
| 2   | 30  |
| 3   | 60  |