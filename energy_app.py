import streamlit as st
import pickle
import numpy as np

heating_model = pickle.load(open("models/xgboost_regression_model1.pkl","rb"))
cooling_model = pickle.load(open("models/model_cooling.pkl", "rb"))


#https://tarjomefa.com/wp-content/uploads/2017/04/6453-English-TarjomeFa.pdf
#st.image("image.jpg")

st.title("Predictor for your heating and acc")

st.write("This app predicts the heating and cooling loads and helps you to find the right heating and acc model.")

col1, col2, col3 = st.columns([1,1,3])

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
    X2 = st.number_input("Surface area", 514.5, 808.5)
    X3 = st.number_input("Wall area", 245.0, 416.0)
    X4 = st.number_input("Roof area", 110.25, 220.5)

with col2:

    X5 = st.selectbox("Number of floors", ["One", "Two"])
    X7 = st.selectbox("Window size/amount:", ["Small", "Medium", "Large"])
    X6 = st.selectbox("Aspect:", ["North", "East", "South", "West"])

 # Set default or predetermined values for X1 and X8
    X1 = -0.00119112 * X2 + 1.5642495965572887  # Calculated by the surface area
    X8 = 3     # Example default value for X8


with col3:
    st.write("")
    st.write("")
    if st.button("Predict"):

        if X5 == "One" :
            X5 = 3.5
        else:
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
        st.write(f"The cooling load prediction is: {hpred_rounded}")
        
        # Assuming cpred contains the cooling load prediction
        cpred_rounded = round(cpred[0], 2)
        st.write(f"The heating load prediction is: {cpred_rounded}")