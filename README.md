# Project-4-Heart-Prediction-Model
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/77715068-04c1-4800-9d59-315746bb2122)

Introduction

Cardiovascular Disease (CVD) remains a significant threat, impairing the functionality of our heart and blood vessels. Detecting CVD at an early stage is crucial to saving lives. Numerous efforts have been made to achieve this, yet opportunities persist to enhance performance and reliability in detection methods. This study introduces a machine learning-driven approach aimed at predicting heart attacks by analysing diverse risk factors. It employs several machines learning techniques, including Support Vector Machines, Logistic Regression, XGBoost, and a combination of methods, to enhance accuracy and precision in CVD prediction. The end XGBOOST was choosen for the model.

The Data Processing Steps:

Data Gathering: Initially, data was collected from publicly available sources. This involved assessing physical conditions and transforming numerical samples into a format usable by computers.
Pre-processing: The second stage focused on addressing data issues such as missing values, outlier identification, and the removal of redundant information to ensure dataset cleanliness.
Integration: Through the use of Python, disparate libraries and subsets were consolidated by importing independent modules and merging them for essential experimental procedures.
Variable Comparison: Following integration, a comparison of variables was conducted to comprehend correlations, allowing for a comprehensive analysis of similar variables.
Application of ML Algorithms: The final phase cantered on selecting optimal ML models for predictive purposes and developing a heart attack risk prediction app using Streamlet.

Data Information
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/e77ad7d3-6984-4844-b866-ecc0b84cba18)
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/6a2ac014-9f60-4364-87a1-392d05239949)
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/f793a0ce-43b2-4f36-b230-abd1a4ff690e)


The Data Frame
The dataset consists of 26 columns, with 25 columns representing features and the remaining column, "Heart Attack Risk," serving as the target variable for prediction

Data Modeling
Initial modelling employed Logistic Regression (LR), Decision Tree (DT), Random Forest (RF), and K-Nearest Neighbors (KNN). These models achieved accuracy scores of 65%, 52%, 64%, and 66%, respectively. Efforts were made to improve model performance by exploring data reengineering techniques, aiming to augment the dataset and enhance predictive capabilities and overall accuracy.

![image](https://github.com/steve3636/Project-4-Heart-Prediction-ModReferencesel/assets/139638282/af5f7b8d-6a6b-412b-b88b-58abbb7410aa)

Enhancing Accuracy Through Diverse Modeling Strategies

The accuracies obtained from the initial set of models—Logistic Regression, Decision Tree, Random Forest, and KNN Model—fall within a range of 52% to 66%. Despite these attempts, the anticipated results weren't achieved. 

A strategic approach involving the partitioning of the dataset into smaller, more focused sections for in-depth analysis was deployed. Concentrating solely on crucial features, identified through robust feature importance techniques. The aim is to achieve higher predictive accuracy and uncover nuanced insights essential for more robust and reliable predictions regarding heart attack risk.
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/aa0f7cfa-2867-475b-af21-cec73399154b)
Combination Model

![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/e9e72174-ee90-40d1-9a3a-fac004fbfb1e)

Combination model also did notshown any major improvement rather than Logistic regression and Gradient Booster abale to performe better individually. Finally Gradient Booster ML was choosen for deployment due to: 
Flexibility and Versatility:
*Handles Various Data Types: Supports different types of data and can handle both numerical and categorical features.
*Feature Importance: Provides insights into feature importance, allowing the identification of critical factors influencing predictions.
![image](https://github.com/steve3636/Project-4-Heart-Prediction-Model/assets/139638282/93fd1c0c-a511-4653-a4e3-096e9e6f6103)
Streamlit modeling used for deployment.
 
References
Pal M, Parija S, Panda G, Dhama K, Mohapatra RK. Risk prediction of cardiovascular disease using machine learning classifiers. Open Med (Wars). 2022 Jun 17;17(1):1100-1113. doi: 10.1515/med-2022-0508. PMID: 35799599; PMCID: PMC9206502.
Nandal N, Goel L and TANWAR R. Machine learning-based heart attack prediction: A  symptomatic heart attack prediction method and exploratory analysis [version 1; peer review: 1 approved]. F1000Research 2022, 11:1126 (https://doi.org/10.12688/f1000research.123776.1)
https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/code
https://www.kaggle.com/code/khanmdsaifullahanjar/heart-attack-prediction-analysis-dtc-rfc-knn