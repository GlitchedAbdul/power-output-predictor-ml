import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Streamlit app title
st.title("Power Output Prediction Tool")

# **Text Field Input Section**
st.header("Input Parameters Using Text Fields")
temperature_text = st.number_input("Temperature (°C):", value=25.0, step=0.1)
humidity_text = st.number_input("Humidity (%):", value=50.0, step=0.1)
pressure_text = st.number_input("Pressure (hPa):", value=1013.25, step=0.1)
wind_speed_text = st.number_input("Wind Speed (km/h):", value=5.0, step=0.1)

# Button for Text Field Input
if st.button("Predict using Text Fields"):
    # Create a DataFrame with text field inputs
    input_data_text = pd.DataFrame([[temperature_text, humidity_text, pressure_text, wind_speed_text]],
                                   columns=["AT", "V", "AP", "RH"])
    # Predict using the loaded model
    prediction_text = rf_model.predict(input_data_text)
    # Display the result
    st.success(f"Projected Power Output (Text Fields): {prediction_text[0]:.2f} MW")

# **Slider Input Section**
st.header("Input Parameters Using Sliders")
temperature_slider = st.slider("Temperature (°C):", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
humidity_slider = st.slider("Humidity (%):", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
pressure_slider = st.slider("Pressure (hPa):", min_value=900.0, max_value=1100.0, value=1013.25, step=0.1)
wind_speed_slider = st.slider("Wind Speed (km/h):", min_value=0.0, max_value=50.0, value=5.0, step=0.1)

# Button for Slider Input
if st.button("Predict using Sliders"):
    # Create a DataFrame with slider inputs
    input_data_slider = pd.DataFrame([[temperature_slider, humidity_slider, pressure_slider, wind_speed_slider]],
                                     columns=["AT", "V", "AP", "RH"])
    # Predict using the loaded model
    prediction_slider = rf_model.predict(input_data_slider)
    # Display the result
    st.success(f"Projected Power Output (Sliders): {prediction_slider[0]:.2f} MW")