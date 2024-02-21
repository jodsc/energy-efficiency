import streamlit as st
import pickle
import numpy as np

heating_model = pickle.load(open("models/xgboost_regression_model1.pkl","rb"))
cooling_model = pickle.load(open("models/model_cooling.pkl", "rb"))


#https://tarjomefa.com/wp-content/uploads/2017/04/6453-English-TarjomeFa.pdf
#st.image("image.jpg")

st.title("Predictor for your heating and cooling")

st.write("This app predicts the heating and cooling loads and helps you to find the right heating and cooling system.")

col1, col2= st.columns([1, 2])
with col1:

    # Inititalise features to means
    # Volume must equal 771.5m3 but unclear how this relates to the input features

    #X1 = 0.764
    #X2 = 672
    #X3 = 319
    #X4 = 177
    #X5 = 5.25
    #X6 = 3.5 
    #X7 = 0.234
    #X8 = 2.81
    #X1 = st.number_input("Relative compactness", 0.62, 0.98)
    
    X5 = st.selectbox("Number of floors", ["One", "Two"])
    if X5 == "One":
        X2 = st.slider("Surface area", 686, 808, 720)
    else:
        X2 = st.slider("Surface area", 514, 661, 540)
    
    # X2 = st.number_input("Surface area", 514.5, 808.5)
    # X3 = st.number_input("Wall area", 245.0, 416.0)
    # X4 = st.number_input("Roof area", 110.25, 220.5)
    X7 = st.selectbox("Window size:", ["Small", "Medium", "Large"])
    X6 = st.selectbox("Building Orientation:", ["North", "East", "South", "West"])

 # Set default or predetermined values for X1 and X8
    X1 = -0.00119112 * X2 + 1.5642495965572887  # Calculated by the surface area
    X8 = 3     # Example default value for X8


with col2:
    st.write("")
    st.write("")
    if st.button("Predict"):

        if X5 == "One" :
            X3 = X2 - 441
            X4 = 220.5
            X5 = 3.5
        else:
            X3 = 0.68571429 * X2 - 78
            X4 = 110.25
            X5 = 7

        if X6 == "North":
            X6 = 2
        elif X6 == "East":
            X6 = 3
        elif X6 == "South":
            X6 = 4
        else:
            X6 = 5

        if X7 == "Small":
            X7 = 0.1
        elif X7 == "Medium":
            X7 = 0.25
        else:
            X7 = 0.4

        hpred = heating_model.predict(np.array([[X1,X2,X3,X4,X5,X6,X7,X8]]).astype(np.float64))
        cpred = cooling_model.predict(np.array([[X1,X2,X3,X4,X5,X6,X7,X8]]).astype(np.float64))

        
        # Assuming cpred contains the cooling load prediction
        hpred_rounded = round(hpred[0], 2)
        st.write(f"The cooling load prediction is: {hpred_rounded :.2F}")
        
        # Assuming cpred contains the cooling load prediction
        cpred_rounded = round(cpred[0], 2)
        st.write(f"The heating load prediction is: {cpred_rounded :.2f}")

        import math
        # Constants
        HEATING_PUMP_CAPACITY = 14  # in kWh
        AC_CAPACITY = 9  # in kWh
        HEATING_PUMP_COST = 11000  # in €
        AC_COST = 6000  # in €

        # Predictions from the model
        # Example predictions, replace with actual predictions from your model
        heating_load = hpred_rounded 
        cooling_load = cpred_rounded

        # Calculating the number of heating pumps and ACs needed
        num_heating_pumps = math.ceil(heating_load / HEATING_PUMP_CAPACITY)
        num_acs_for_heating = math.ceil(max(0, heating_load - num_heating_pumps * HEATING_PUMP_CAPACITY) / AC_CAPACITY)
        num_acs_for_cooling = math.ceil(cooling_load / AC_CAPACITY)

        # Total number of ACs needed is the max of ACs needed for heating and cooling
        total_acs_needed = max(num_acs_for_heating, num_acs_for_cooling)

        # Calculating total costs
        total_cost = (num_heating_pumps * HEATING_PUMP_COST) + (total_acs_needed * AC_COST)

        # Displaying the results
        
        st.write(f"Number of heating pumps needed: {num_heating_pumps}")
        st.write(f"Total number of additional ACs needed: {total_acs_needed}")
        st.write(f"Estimated investment needed for covering your cooling and heating given the characteristics of your house: {total_cost:.2f} €")

        # Checking if additional ACs are needed for cooling load
        if total_acs_needed > num_acs_for_heating:
            additional_acs_for_cooling = total_acs_needed - num_acs_for_heating
            st.write(f"Out of the total ACs, {additional_acs_for_cooling} are additionally needed to cover the cooling load.")
        else:
            st.write("No additional ACs are needed beyond those required for the heating load.")


        # Costs for energy
        cost_per_unit = 0.31  # Costs per kWh in Euro

        # Asumed consumption heating based on the usage per m2
        average_annual_consumption_h = 95 * X2  # Durchschnittlicher Jahresverbrauch in kWh

        # Annual costs for warming pump
        yearly_heating_bill = average_annual_consumption_h * cost_per_unit

        # Ergebnis anzeigen
        st.write(f"Estimaed anual costs for heating based on your surface area: {yearly_heating_bill:.2f} €")

         # Asumed consumption cooling based on the usage per m2
        average_annual_consumption_c = 48 * X2  # Durchschnittlicher Jahresverbrauch in kWh

        # Annual costs for AC
        yearly_cooling_bill = average_annual_consumption_c * cost_per_unit

        # Ergebnis anzeigen
        st.write(f"Estimaed anual costs for cooling based on your surface area: {yearly_cooling_bill:.2f} €")

