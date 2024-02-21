import streamlit as st
import pickle
import numpy as np

heating_model = pickle.load(open("models/xgboost_regression_model1.pkl","rb"))

#https://tarjomefa.com/wp-content/uploads/2017/04/6453-English-TarjomeFa.pdf
#st.image("image.jpg")

st.title("House energy efficency and energy cost calculator")

st.write("This app predicts the heating and cooling loads and calculates energy costs.")

# Custom CSS to style the sidebar radio buttons as a menu
st.sidebar.markdown("""
    <style>
    .reportview-container .sidebar-content {
        padding-top: 0rem;
    }
    .sidebar .sidebar-content {
        padding: 1rem;
    }
    .widget-container .stRadio > div {
        display: flex;
        flex-direction: column;
    }
    .css-1b4g6e5 {
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
    }
    .css-1b4g6e5:hover {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'About this App'

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'About this App'

# Function to set the page state
def set_page(page_name):
    st.session_state.page = page_name

# Sidebar buttons for navigation
st.sidebar.header("Menu")
if st.sidebar.button("About this App"):
    set_page('About this App')

if st.sidebar.button("Energy Efficency"):
    set_page('Energy Efficency')

if st.sidebar.button("Price for energy consumption"):
    set_page('Price for energy consumption')

# Content for "About this App"
if st.session_state.page == 'About this App':
    st.title("About this App")
    st.markdown("""
        This app is a part of a project designed during a class for the Data Science Retreat in Berlin. It serves as a demonstration of how Streamlit can be effectively used for data visualization and interactive data exploration.

        The app allows users to upload datasets, specifically tailored for the Palmer Penguins dataset, and explore various visualizations to uncover insights about the data.
    """)

# Content for "Penguins"
elif st.session_state.page == 'Penguins':
    st.title("Penguins")
    st.markdown("""
        The Palmer Penguins dataset contains data on three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The dataset includes measurements such as bill length, bill depth, flipper length, body mass, and more, along with the species and islands.

        This dataset is popular in the data science community for exploratory data analysis, data visualization, and machine learning tasks due to its simplicity and variety of data points.

        More information about the dataset can be found on the [Palmer Penguins dataset GitHub page](https://github.com/allisonhorst/palmerpenguins).
    """)
    
# Content for "Data Visualisation"
elif st.session_state.page == 'Data Visualisation':
    st.title("Data Visualisation")
    st.write("Please upload the penguin CSV file. You can find the dataset ")
    st.markdown("[here](https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv).", unsafe_allow_html=True)

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
        #st.write(f"The cooling load prediction is: {cpred}")