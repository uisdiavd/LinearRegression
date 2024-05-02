Feature: Linear regression for average views program should convert training data into a dataframe for use in the linear regression model

As a programmer for the linear regression program anlyzing average views data
I need the training data can be converted to a dataframe 
So that null values can be cleared

Background:
    Given the appropriately prepared training data array for linear regression on average views of a single country from an original data set
    [[  46422.        ]
 [ 575767.91666667]
 [1048158.95      ]
 [1480758.33193277]
 [1887680.20168067]
 [2552939.70714286]]
[[             nan]
 [  60916.        ]
 [ 148163.5       ]
 [ 439132.4       ]
 [ 687614.        ]
 [1045667.71428571]]
[[            nan]
 [            nan]
 [117571.        ]
 [117571.        ]
 [117571.        ]
 [545527.33333333]]

Scenario: Convert to dataframe
Given the training data has been extracted for each country
When it is converted into a dataframe
Then the type should be dataframe