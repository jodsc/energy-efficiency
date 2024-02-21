import streamlit as st

#https://tarjomefa.com/wp-content/uploads/2017/04/6453-English-TarjomeFa.pdf

st.title("Heating / cooling predictor")

st.write("This app predicts the heating and cooling loads given eight input features.")

def heating_model(X1,X2,X3,X4,X5,X6,X7,X8):
    pass

def cooling_model(X1,X2,X3,X4,X5,X6,X7,X8):
    pass

# Inititalise features to means
# Volume must equal 771.5m3 but unclear how this relates to the input features

X1 = 0.764
X2 = 672
X3 = 319
X4 = 177
X5 = 5.25
X6 = 3.5 
X7 = 0.234
X8 = 2.81

# Override defaults

X1 = st.number_input("Relative compactness", 0.62, 0.98)
X2 = st.number_input("Surface area", 514.5, 808.5)
X3 = st.number_input("Wall area", 245.0, 416.0)
X4 = st.number_input("Roof area", 110.25, 220.5)
X5 = st.number_input("Overall height", 3.5, 7.0)
X6 = st.number_input("Orientation", 2.0, 5.0)
X7 = st.number_input("Glazing area", 0.0, 0.4)
X8 = st.number_input("Glazing area distribution", 0.0, 5.0)

hpred = heating_model(X1,X2,X3,X4,X5,X6,X7,X8)
cpred = cooling_model(X1,X2,X3,X4,X5,X6,X7,X8)

st.write(f"The heating load prediction is: {hpred}")
st.write(f"The cooling load prediction is: {cpred}")
