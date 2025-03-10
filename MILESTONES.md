
 ## 2025-02-17
 
 ### Team Evaluation

 Our team feels that we are working at a good pace to have our dashboard completed by the end of the semester. We have been using our class time to work on brainstorming ideas and obtaining our data. We think that in the future we could have challenges with technical issues. We have already had a few issues using git. We are also unsure of what problems we may face once we start to create our database. When these issues come up we will work together to try and find a solution and will ask for outside help if needed.


 ### Technology Plan

 We are using python for most processes. It will be used for downloading our data and the sqlite3 library will be used to host a database for cleaning and transforming data within the python program. We are planning on using power bi for a dashboard and are still looking into how that could work. From our research so far we think it should be possible to run our python script inside power bi and access the datasets, but we are still looking into the specifics of that process.  


 ### Data Wrangling
 
We are looking the crime data. We have the dataset of Arrests, homicides, and population. We also have the various features related to qualtity of life in each states. We have the dataset recidivism which says what percenatge of prisoner are incarcerated again after being released. We do have prison population and imprisoment rate. So far, we have set database and put the data into the database. We are working on transformation of the dataset. Some of the dataset are found in Json file which we need to convert it into csv file. 


 ### Project Goals
 
 Our project aims to investigate how crime rates and recidivism rates are influenced by various demographic and economic factors. Specifically, we seek to understand the relationship between population size, economic status, quality of life, and crime trends, using census and economic data to identify potential correlations. Our main question is: How are crime rates and recidivism rates affected by other demographic information? The intended audience for this research includes future classes studying crime and sociology, as well as a PSA that could help inform communities and policy makers.

  
  ## 2025-02-23
 
 ### Exploratory Analysis

We are using the Power Bi,  pandas, Matplotlib for making visualization, Sklearn for good for modelling. There is the linear correlation between the different variables in the data.csv. There is  .62 correlation between imprisonment rate and recidivism rate or comparing the imprisonment rate to the quality of life scores. Again, this is only looking at linear correlations, so there may be stronger correlations that are not showing in this map because the data may be non-linear. I have encountered the issue in the dataset mainly in json dataset. We changed  json to css file. Imprisonment rate and Quality of lifeTotal scores are the important predictors of our dataset. We have seen the correlation between the varicose but we haven't discuss trends of our dataset. Delaware  has the highest sum of recidivismRate by state , Mississippi has the highest sum of imprisonmentRate by state, Kentucky has lowest  sum of recidivismRate by state, New Mexico got the highest sum of quality go life safety by state, California has the highest sum of quality of life adorability by state. We haven't got any outliers and missing values yet. By the help of power Bi, we have done basis visualization so far. We haven't discuss what visuals needed to be included for final, so it's not final. 

### Modeling Plan

We plan to use linear regression if relationships are linear or follow quadratic/logarithmic trends (e.g., recidivism, state percentages). For non-linear patterns, we will use decision trees, random forests, boosting, and bagging. Ridge and lasso regression will help manage variable relationships. Our response variable is likely recidivism probability. Linear regression fits well with our dashboard for visualization, while tree-based models provide insights through feature importance. We will compare original vs. retrained models to track improvements.

### Project Progress

Our team has been making good progress on achieving our goals for our milestones. Each week we have been planning out our goals for the next Sunday and work on completing them throughout the week. This week we worked on starting our exploratory data analysis. We were able to get Python and Power BI set up on our local machines to start our analysis. Our team has been communicating well. We use our time in class for group discussions about what needs to be done and will communicate outside of class using discord. Moving forward we will start to focus on making models for our data and start to plan out visualizations we want for our dashboard.

### Project Goals

Our target audience is future data science classes as well as the general public. Our dashboard focuses on factors that affect recidivism which we think can raise awareness to real issues that exist today. This dashboard can be useful for pointing out what problems exist that lead to the high recidivism rates in the US as well as looking at what policies and factors have helped to fix this problem in states with lower recidivism. To communicate our findings and conclusions we will create some charts and models to include in our dashboard that will highlight important points. While doing research we have found other websites with graphs and tables showing similar data to what we might end up with on our dashboard. The kind of questions we want our dashboard to answer involve what different factors can increase and decrease recidivism rates in states. Our main research question is: What factors and policies have negative and positive effects on recidivism rates in the US?

## 2025-03-02

### Project Progress
Our team has been making good progress this week towards completing our exploratory analysis milestones. We have all been using Power BI to create some initial visualizations and to find trends in our data. We have been communicating our findings and visualizations in our groups discord so that we can all have access to them. We have had some issues with Power BI for our group members using macs. There is no Power BI desktop app for ios so they have been using the web service which has had some issues. These group members will be switching to Tableau for their exploratory analysis. We still plan to use Power BI for our final dashboard. Our next steps will be to start making visualizations we may want to use in the dashboard and to start working in some modeling.

### Data Report
We don't need to rethink our data but we will continue collecting more data as we find more specific areas to research. The data that we have will be used to determine what further research and data will be needed for our project. We did get rid of some of the original data that we collected as we decided to look at states instead of cities. Most of our data will be combined into one file that will help make every easy to organize and find.

<<<<<<< HEAD
## 2025-03-09

### Brainstorm Dashboard

Our dashboard highlights factors contributing to recidivism to improve prison systems. It will use interactive elements like drill-through and filters to explore deeper into the data visually. Key questions include what factors increase recidivism. Power BI will be used to create visualizations with DAX functions. The dashboard will be stored in the project repository with instructions in a .MD file for reproducibility. We also plan on using power query and tableau. 

=======
### 2025-03-09: Brainstorm Dashboard Milestone

Initial Modeling Approaches
For this mini-milestone, we will begin by exploring initial modeling techniques to determine whether our data is better suited for linear or nonlinear models.Decision trees and linear regression will serve as our initial baseline models. Decision tree will enable us to capture extra difficult, non-linear correlations between variables, whereas linear regression will simplify and make the relationships among variables simpler to recognize. By evaluating these performances, we're planning to use sophisticated approaches processes like boosting, random forests, or regularized regression strategies like ridge and lasso.

 Research Areas:

Prison-related variables: Niraj Amgai

Quality of life: Kat Amundson

Specific crimes committed: Macy Schanbacher

Demographic information on people committing the crimes: Joshua Morningstar
>>>>>>> d3844ba (Brainstorm Dashboard Milestone)

