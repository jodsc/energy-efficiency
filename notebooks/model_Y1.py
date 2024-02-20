from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objs as go
import plotly.express as px
  
# fetch dataset 
energy_efficiency = fetch_ucirepo(id=242) 
  
# data (as pandas dataframes) 
X = energy_efficiency.data.features 
y = energy_efficiency.data.targets 
  
# metadata 
print(energy_efficiency.metadata) 
  
# variable information 
print(energy_efficiency.variables) 

import pandas as pd

# Combine 'X' and 'y' into a single DataFrame
combined_df = pd.concat([X, y], axis=1)

# Display the DataFrame
print(combined_df.head())  # .head() shows the first 5 rows

# Assuming combined_df is your DataFrame with features and target variables

# Splitting the data into training and testing sets, focusing on 'Y1' as the target variable
X_train, X_test, y_train, y_test = train_test_split(
    combined_df.drop(['Y1', 'Y2'], axis=1),  # Features (excluding both Y1 and Y2)
    combined_df['Y1'],  # Target variable (Y1 - Heating Load)
    test_size=0.2,  # 20% of the data for testing
    random_state=42  # For reproducibility
)

# Convert data into DMatrix, an optimized data format for XGBoost
dtrain = DMatrix(X_train, label=y_train)

# Parameters for XGBoost
params = {
    'objective': 'reg:squarederror',
    'n_estimators': 100,
    'seed': 42
}

# Perform Cross-Validation
cv_results = cv(
    dtrain=dtrain, 
    params=params, 
    nfold=5,  # Number of folds in K-Fold Cross-Validation
    num_boost_round=100,  # Number of boosting rounds, equivalent to n_estimators
    metrics='rmse',  # Root Mean Square Error as evaluation metric
    as_pandas=True,  # Return results as a Pandas DataFrame
    seed=42
)

# Display Cross-Validation results
print(cv_results)

# Initialize the XGBoost regressor with the best parameters found
xg_reg = XGBRegressor(objective='reg:squarederror', n_estimators=100, seed=42)

# Initialize the XGBoost regressor
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, seed=42)

# Train the model
xg_reg.fit(X_train, y_train)

# Predictions on the test set
y_pred = xg_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Extract feature importance from the XGBoost model
feature_importance = xg_reg.feature_importances_
features = X_train.columns

# Create a DataFrame for feature importance
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})

# Sort the DataFrame by importance
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Create a bar chart with Plotly
fig = px.bar(importance_df, 
             x='Importance', 
             y='Feature', 
             orientation='h',
             title='Feature Importance')

# Display the chart
fig.show()