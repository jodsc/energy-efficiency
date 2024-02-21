import streamlit as st
import pickle
import numpy as np

# Load models
heating_model = pickle.load(open("models/xgboost_regression_model1.pkl", "rb"))
cooling_model = pickle.load(open("models/model_cooling.pkl", "rb"))

# App title
st.title("House Energy Efficiency and Energy Cost Calculator")

# Initialize page state in session state if not already present
if 'page' not in st.session_state:
    st.session_state.page = 'Main'

# Function to set the current page
def set_page(page_name):
    st.session_state.page = page_name

# Sidebar title
st.sidebar.header("Menu")

# Sidebar buttons for navigation
if st.sidebar.button("Main"):
    set_page('Main')
if st.sidebar.button("About this App"):
    set_page('About this App')
if st.sidebar.button("Energy Efficiency"):
    set_page('Energy Efficiency')
if st.sidebar.button("Price for Energy Consumption"):
    set_page('Price for Energy Consumption')
if st.sidebar.button("Calculator"):
    set_page('Calculator')

# Custom CSS for button styling
st.sidebar.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #4CAF50;
        color: white;
        background-color: #4CAF50;
        padding: 10px 24px;
        cursor: pointer;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Content for "About this App"
if st.session_state.page == 'About this App':
    st.title("About this App")
    st.markdown("""
        This app is part of a project designed during a class at the Data Science Retreat in Berlin. It serves as a demonstration of how Streamlit can be effectively used for data visualization and interactive data exploration.
        
        The app allows users to upload datasets, specifically tailored for the Palmer Penguins dataset, and explore various visualizations to uncover insights about the data.
    """)

# Content for "Calculator"
elif st.session_state.page == 'Calculator':
    st.title("Calculator")
    # This part should be within the 'Main' or 'Calculator' condition block
col1, col2, col3 = st.columns([1,1,3])
# Override defaults
    
    # Set default or predetermined values for X1 and X8
    X1_default_value = 0.76  # Example default value for X1
    X8_default_value = 3     # Example default value for X8

with col1:
    #X1 = st.number_input("Relative compactness", 0.62, 0.98)
    X2 = st.number_input("Surface area", 514.5, 808.5)
    X3 = st.number_input("Wall area", 245.0, 416.0)
    X4 = st.number_input("Roof area", 110.25, 220.5)

with col2:

    X5 = st.selectbox("Number of floors", ["One", "Two"])
    X6 = st.selectbox("Aspect:", ["North", "East", "South", "West"])
    X7 = st.number_input("Glazing area", 0.0, 0.4)
    #X8 = st.number_input("Glazing area distribution")

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
        cpred = cooling_model.predict(np.array([[X1,X2,X3,X4,X5,X6,X7,X8]]).astype(np.float64))

        st.write(f"The heating load prediction is: {hpred}")
        st.write(f"The cooling load prediction is: {cpred}")
    # Placeholder for Calculator code

# Content for "Main"
elif st.session_state.page == 'Main':
    st.write("Welcome to the main page. Use the menu to navigate through the app.")

# Additional pages like "Energy Efficiency" and "Price for Energy Consumption" can follow the same pattern

