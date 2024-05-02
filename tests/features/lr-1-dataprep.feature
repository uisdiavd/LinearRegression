Feature: Linear regression program for average views data should create a data set with only relevant information to average views

As a programmer for the linear regression program anlyzing average views data 
I need a data set only average views data per country
So that the prepared data set can be used for a linear regression model

Background:
    Given the following data from an original data set
    | Country   | Channel Name  | Category  | Main Video Category   | username  | followers | Main topic    | More topics   | Likes | Boost Index   | Engagement Rate   | Engagement Rate 60days    | Views | Views Avg.    | Avg. 1 Day    | Avg. 3 Day    | Avg. 7 Day    | Avg. 14 Day   | Avg. 30 day   | Avg. 60 day   | Comments Avg  | Youtube Link  |

Scenario: Prepare given data for linear regression of average views data per country
Given the original data set
When I load the original data set into the linear regression program for predicting average views at a future day
Then there should be a new dataset with only the following columns: 'Country', 'Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day'
And there should only be one row of data for the country 'AE'
And there should only be one row of data for the country 'AR'
And there should only be one row of data for the country 'AU'