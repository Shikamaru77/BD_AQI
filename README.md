# Bangladesh AQI Prediction

##### Author: Syed Mohammad Afraim

##### Date: 23rd July, 2023

##### [BD AQI prediction website](https://bd-aqi.onrender.com/predict)
##### [Kaggle](https://www.kaggle.com/code/syedmohammadafraim2/bangladesh-aqi-prediction)

## Overview

The "Bangladesh AQI Prediction" project aims to predict the Air Quality Index (AQI) for the city of Dhaka, Bangladesh, using machine learning techniques. Air quality is a critical environmental factor that significantly affects public health, climate, and overall well-being. By developing an end-to-end machine learning project for AQI prediction, we can gain insights into air quality patterns and help policymakers, citizens, and relevant authorities take informed actions to improve air quality and mitigate its impact on health and the environment.

## Data Collection

The dataset for this project was collected from Kaggle, specifically from the dataset titled "Dhaka, Bangladesh Hourly Air Quality (2016-2022)." The dataset contains hourly air quality data for Dhaka, including attributes such as date, hour, nowcast concentration, raw concentration, AQI, AQI category, and quality control name. The data spans from 2016 to 2022, providing a substantial timeframe for analysis.

Dataset Source: [Dhaka, Bangladesh Hourly Air Quality (2016-2022)](https://www.kaggle.com/datasets/shawkatsujon/dhaka-bangladesh-hourly-air-quality-20162022)

## Model Development

In the model development phase, several steps were taken to build an effective AQI prediction model. First, a correlation matrix was used to identify the relationships between different features and the target variable (AQI). The Pearson correlation method was chosen to assess the linear correlations between variables.

Next, the Recursive Feature Elimination with Cross-Validation (RFECV) technique was employed to select the most relevant features for the model. RFECV helps identify the optimal subset of features that contribute significantly to the prediction, leading to improved model performance and reduced computational complexity.

Finally, the Random Forest Regressor algorithm was chosen as the ensemble model for AQI prediction. Random Forest is a robust and versatile algorithm that can handle non-linearity and perform well on large datasets with high dimensionality. It provides accurate predictions and helps capture complex relationships between input features and the target variable.

## Model Evaluation

The model's performance was evaluated using the R-squared (R2) score, a common metric used to assess regression models' goodness-of-fit. The R2 score measures the proportion of variance in the target variable (AQI) explained by the model. A higher R2 score indicates a better fit of the model to the data and better prediction capability.

The "Bangladesh AQI Prediction" project has the potential to raise awareness about air quality issues in Dhaka and provide valuable insights into factors affecting AQI fluctuations. It can aid policymakers in making informed decisions and implement effective measures to improve air quality, leading to better public health and a cleaner environment.

Note: The project's code and detailed documentation can be found in this repository. Feel free to explore the Jupyter Notebook and contribute to further enhancements.
