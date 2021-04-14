## USA-cases-number-prediction-model
**In this model, we predict the number of cases and deaths based on three features: Temperature, 
number of days since the pandemic started (21 January 2020) and the number of days since the vaccination process had started (February 2021)**

## Models
We tried two models:  
1- Linear Regression Model.  
2- Random Forest Model.  
**In the end, we find that linear regression is the best model**

## Data
I collected the data from two websites:  
1- [accuweather](https://www.accuweather.com/en/us/new-york/10007/january-weather/349727?year=2020)  
2- [worldometers](https://www.worldometers.info/coronavirus/)  
3- Some data have been collected from [kaggle](https://www.kaggle.com/)

## Data Info:
> **Data Summary:**  
1- **date**   
2- **year**  
3- **month**  
4- **day**  
5- **cases** (total number of cases since the beginning of the pandemic to mentioned date)  
6- **deaths** (total number of deaths since the beginning of the pandemic to mentioned date)  
7- **daily_cases** (the number of cases in the mentioned date only)  
8- **daily_deaths** (the number of deaths in the mentioned date only)  
9- **no_days_since_jan** (the number of days since the january month, we we know that the pandemic startes in USA in that month)  
10- **no_days_since_vaccination** (the number of days since the vaccination have been started)  
11- **temp_high** (the tempreature of the mentioned date in the afternoon)  
12- **temp_low** (the tempreature of the mentioned date at the night)  
13- **moving_avg_temp_high** (the moving average of temp_high of the previous 7 days from the mentioned date)  
14- **moving_avg_temp_low** (the moving average of temp_low of the previous 7 days from the mentioned date)
