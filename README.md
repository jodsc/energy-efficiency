# Energy Efficiency Analysis with XGBoost and Streamlit

## Overview
This project utilizes the Energy Efficiency dataset from the UCI Machine Learning Repository to analyze energy efficiency based on various building characteristics. The original study simulated 12 different building shapes in Ecotect, varying by surface area, overall height among other parameters. The dataset consists of 768 samples and 8 features, aiming to predict two real-valued responses: Heating Load (Y1) and Cooling Load (Y2).

https://archive.ics.uci.edu/dataset/242/energy+efficiency

## Project Goal
The aim is to provide a predictive tool for homeowners or individuals planning to construct a house, enabling them to estimate energy costs based on specific house characteristics. 

Features from the dataset have been consolidated, reworded and coded to provide a user-friendly experience with clear prompts.

Users input data related to building shape, orientation, and other features to receive estimates for heating and cooling loads, essential 
for planning energy-efficient buildings.

Once the forecasts have been made, the app will propose an approporiate HVAC (Heating, Ventilation and Air Conditioning) system to efficiently heat and cool the property.

## Approach
1. Data Exploration: Initial examination of the dataset to understand its features and target variables.
2. Model Development: Trained two XGBoost models to predict Heating Load (Y1) and Cooling Load (Y2), respectively.
3. Feature Importance Analysis: Conducted analysis to identify significant features influencing energy efficiency, visualized through a feature importance bar chart.
4. Serialization: Serialized the trained models into Pickle files for integration into a Streamlit application.
5. Streamlit Application: Developed a user-friendly web application using Streamlit, allowing for interactive user input and prediction of energy costs.

## Usage
To use the application, ensure all required packages are installed as listed in requirements.txt. Run the Streamlit app locally by navigating to the app directory and executing:

streamlit run app.py

The web interface will guide you to input various house characteristics, and provide estimates for Heating and Cooling Loads based on the input data.

## Requirements
For the required Python packages, please refer to requirements.txt. Install these packages using:

pip install -r requirements.txt

## Acknowledgments
Special thanks to the creators of the Energy Efficiency dataset at the UCI Machine Learning Repository for providing this valuable resource to the community.
