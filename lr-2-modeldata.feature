Feature: Linear regression for average views program should prepare training data

As a programmer for the linear regression program anlyzing average views data 
I need the training data for the linear regression model to contain only average views data for a single country at a time
So that the training data can be converted to a dataframe for clearing unavailable data

Background:
    Given the following prepared data for linear regression on average views of a country from an original data set
    | Country   | Avg. 1 Day    | Avg. 3 Day        | Avg. 7 Day    | Avg. 14 Day       | Avg. 30 day           | Avg. 60 day           |
    | AE	    | 46422.0	    | 575767.9166666670	| 1048158.95	| 1480758.331932770	| 1887680.2016806700	| 2552939.7071428600    |
    | AR	    | 	            | 60916.0	        | 148163.5	    | 439132.4	        | 687614.0	            | 1045667.7142857100    |
    | AU	    | 	            | 	                | 117571.0	    | 117571.0	        | 117571.0	            | 545527.3333333330     |

Scenario: Prepare training data for country AE
Given a prepared data set for linear regression with average views per country
When the program prepares training data for the country AE
Then the training data set should contain only average views data for the country AE
 
Scenario: Prepare training data for country AR
Given a prepared data set for linear regression with average views per country
When the program prepares training data for the country AR
Then the training data should contain only average views data

Scenario: Prepare training data for country AU
Given a prepared data set for linear regression with average views per country
When the program prepares training data for the country AU
Then the training data should contain only average views data