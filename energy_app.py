import streamlit as st
import pickle
import numpy as np

heating_model = pickle.load(open("models/xgboost_regression_model1.pkl","rb"))

#https://tarjomefa.com/wp-content/uploads/2017/04/6453-English-TarjomeFa.pdf
#st.image("image.jpg")
st.title("Heating / cooling load predictor")

st.write("This app predicts the heating and cooling loads given eight input features.")

col1, col2, col3 = st.columns([1,1,3])

def cooling_model(X1,X2,X3,X4,X5,X6,X7,X8):
    pass

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

    # Override defaults

    X1 = st.number_input("Relative compactness", 0.62, 0.98)
    X2 = st.number_input("Surface area", 514.5, 808.5)
    X3 = st.number_input("Wall area", 245.0, 416.0)
    X4 = st.number_input("Roof area", 110.25, 220.5)

with col2:

    X5 = st.selectbox("Number of floors", ["One", "Two"])
    X6 = st.selectbox("Aspect:", ["North", "East", "South", "West"])
    X7 = st.number_input("Glazing area", 0.0, 0.4)
    X8 = st.number_input("Glazing area dist", 0.0, 5.0)

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

        hpred = heating_model.predict(np.array([[X1,X2,X3,X4,X5,X6,X7,X8]]).astype(np.float64))
        #cpred = cooling_model(np.array([[X1,X2,X3,X4,X5,X6,X7,X8]]).astype(np.float64))

        st.write(f"The heating load prediction is: {hpred}")
        st.write(f"The cooling load prediction is: {cpred}")