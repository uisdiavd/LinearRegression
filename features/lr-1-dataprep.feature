Feature: Linear regression program for average views data should create a data set with only relevant information to average views

As a programmer for the linear regression program anlyzing average views data 
I need a data set only average views data per country
So that the prepared data set can be used for a linear regression model

Background:
    Given the following data from an original data set
    | Country   | Channel Name  | Category  | Main Video Category   | username  | followers | Main topic    | More topics   | Likes | Boost Index   | Engagement Rate   | Engagement Rate 60days    | Views | Views Avg.    | Avg. 1 Day    | Avg. 3 Day    | Avg. 7 Day    | Avg. 14 Day   | Avg. 30 day   | Avg. 60 day   | Comments Avg  | Youtube Link  |
    | 736|AE|shfa2 - شفا||People & Blogs|shfa2 - شفا|35600000|Lifestyle|Lifestyle,Hobby|33139055.27883881|25|0.1512135034248633|0.027334772808817|20513944057|3087191.1809523813|14977.0|258225.3333333333|328154.9|381734.2352941177|562335.6176470588|947859.4857142858|0.0|UCQ7x25F6YXY9DvGeHFxLhRQ |
    | 536|AE|shfa2 - شفا||People & Blogs|shfa2 - شفا|35600000|Lifestyle|Lifestyle,Hobby|33139055.27883881|25|0.1512135034248633|0.027334772808817|20513944057|3087191.1809523813|14977.0|258225.3333333333|328154.9|381734.2352941177|562335.6176470588|947859.4857142858|0.0|UCQ7x25F6YXY9DvGeHFxLhRQ |
    | 535|AE|shfa|LifeStyle|People & Blogs|shfa|35600000|Food|Lifestyle,Hobby,Food|100292545.15|28|0.5323437337087297|0.1201885306610784|18836836311|20460783.2|77867.0|893310.5|1768163.0|2579782.4285714286|3213024.785714286|4158019.9285714286|2.7796296296296297|UCwHE1kM1CPJd_pI9FQ0-4dg |
    | 735|AE|shfa|LifeStyle|People & Blogs|shfa|35600000|Food|Lifestyle,Hobby,Food|100292545.15|28|0.5323437337087297|0.1201885306610784|18836836311|20460783.2|77867.0|893310.5|1768163.0|2579782.4285714286|3213024.785714286|4158019.9285714286|2.7796296296296297|UCwHE1kM1CPJd_pI9FQ0-4dg |
    | 766|AR|La Granja de Zenón|Music|Music|La Granja de Zenón|31200000|Entertainment|Music,Movies,Entertainment|8862147.77638191|65|0.1396151637032101|0.0340363019654131|22499719782|4673667.25||60916.0|148163.5|439132.4|687614.0|1045667.7142857144|4.085427135678392|UCwpcLKMwiuPg4aqImpGk6Ew |
    | 566|AR|La Granja de Zenón|Music|Music|La Granja de Zenón|31200000|Entertainment|Music,Movies,Entertainment|8862147.77638191|65|0.1396151637032101|0.0340363019654131|22499719782|4673667.25||60916.0|148163.5|439132.4|687614.0|1045667.7142857144|4.085427135678392|UCwpcLKMwiuPg4aqImpGk6Ew |
    | 817|AU|Bounce Patrol - Kids Songs|Music|Music|Bounce Patrol - Kids Songs|26200000|Music|Music|29776135.444444448|60|3.1235834036426944|0.0264478604749787|18680919326|74292444.75|||117571.0|117571.0|117571.0|545527.3333333334|0.0|UC56cowXhoqRWHeqfSJkIQaA |
    | 617|AU|Bounce Patrol - Kids Songs|Music|Music|Bounce Patrol - Kids Songs|26200000|Music|Music|29776135.444444448|60|3.1235834036426944|0.0264478604749787|18680919326|74292444.75|||117571.0|117571.0|117571.0|545527.3333333334|0.0|UC56cowXhoqRWHeqfSJkIQaA |

Scenario: Prepare given data for linear regression of average views data per country
Given the original data set
When I load the original data set into the linear regression program for predicting average views at a future day
Then there should be a new dataset with only the following columns: 'Country', 'Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day'
And there should only be one row of data for the country 'AE'
And there should only be one row of data for the country 'AR'
And there should only be one row of data for the country 'AU'