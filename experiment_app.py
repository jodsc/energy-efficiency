import streamlit as st
import pickle
import numpy as np

# Load models
heating_model = pickle.load(open("models/xgboost_regression_model1.pkl", "rb"))
cooling_model = pickle.load(open("models/model_cooling.pkl", "rb"))

# App title
st.title("Predictor for Your Heating and AC")

st.write("This app predicts the heating and cooling loads and helps you to find the right heating and AC model.")

col1, col2, col3 = st.columns([1, 1, 3])

with col1:
    X2 = st.number_input("Surface area", 514.5, 808.5)
    X3 = st.number_input("Wall area", 245.0, 416.0)
    X4 = st.number_input("Roof area", 110.25, 220.5)

with col2:
    X5 = st.selectbox("Number of floors", ["One", "Two"])
    X7 = st.selectbox("Window size/amount:", ["Small", "Medium", "Large"])
    X6 = st.selectbox("Aspect:", ["North", "East", "South", "West"])
    energy_usage = st.selectbox("Energy usage level:", ["Low", "Medium", "High"])  # User specifies energy usage level

# Set default or predetermined values for X1 and X8
X1 = -0.00119112 * X2 + 1.5642495965572887  # Calculated by the surface area
X8 = 3  # Example default value for X8

with col3:
    if st.button("Predict"):
        # Convert selections to model inputs
        X5 = 3.5 if X5 == "One" else 7
        aspect_dict = {"North": 2, "East": 3, "South": 4, "West": 5}
        X6 = aspect_dict[X6]
        window_size_dict = {"Small": 0.1, "Medium": 0.25, "Large": 0.4}
        X7 = window_size_dict[X7]

        # Predict heating and cooling loads
        hpred = heating_model.predict(np.array([[X1, X2, X3, X4, X5, X6, X7, X8]]).astype(np.float64))
        cpred = cooling_model.predict(np.array([[X1, X2, X3, X4, X5, X6, X7, X8]]).astype(np.float64))

        # Display predictions
        st.write(f"The heating load prediction is: {hpred[0]}")
        st.write(f"The cooling load prediction is: {cpred[0]}")

        # Energy usage adjustment
        energy_factor = {"Low": 0.33, "Medium": 0.66, "High": 1.0}[energy_usage]
        adjusted_heating_load = hpred[0] * energy_factor

        # Assume cost per unit of energy and heating system efficiency for demonstration
        cost_per_unit = 0.15  # Example cost per kWh
        heating_system_efficiency = 0.9  # Example efficiency factor
        time_period = 365  # Days in a year

        # Calculate yearly heating bill
        yearly_heating_bill = adjusted_heating_load * cost_per_unit * heating_system_efficiency * time_period
        st.write(f"Estimated yearly heating bill: ${yearly_heating_bill:.2f}")
