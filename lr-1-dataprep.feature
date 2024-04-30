Feature: Linear regression program should create a data set with only relevant information to average views

Background:
    Given the following data
    | Country   | Channel Name  | Category  | Main Video Category   | username  | followers | Main topic    | More topics   | Likes | Boost Index   | Engagement Rate   | Engagement Rate 60days    | Views | Views Avg.    | Avg. 1 Day    | Avg. 3 Day    | Avg. 7 Day    | Avg. 14 Day   | Avg. 30 day   | Avg. 60 day   | Comments Avg  | Youtube Link  |

Scenario: Prepare given data for linear regression of average views data for country AE
Given the given data set
When I load the given data set into the linear regression program 
Then there should be a new dataset with only data relevant to average views
And there should only be one row of data for the country 'AE'

Scenario: Prepare given data for linear regression of average views data for country AR
Given the given data set
When I load the given data set into the linear regression program 
Then there should be a new dataset with only data relevant to average views
And there should only be one row of data for the country 'AR'

Scenario: Prepare given data for linear regression of average views data for country AU
Given the given data set
When I load the given data set into the linear regression program 
Then there should be a new dataset with only data relevant to average views
And there should only be one row of data for the country 'AU'