import streamlit as st

# Function to convert length units
def convert_length(from_unit, to_unit, value):
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048
    }
    
    value_in_meters = value * length_units[from_unit]
    converted_value = value_in_meters / length_units[to_unit]
    return converted_value

# Function to convert speed units
def convert_speed(from_unit, to_unit, value):
    speed_units = {
        "m/s": 1,
        "km/h": 1000 / 3600,
        "mph": 1609.34 / 3600,
        "ft/s": 0.3048
    }
    
    value_in_m_s = value * speed_units[from_unit]
    converted_value = value_in_m_s / speed_units[to_unit]
    return converted_value

# Function to convert time units
def convert_time(from_unit, to_unit, value):
    time_units = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800
    }
    
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value

# Streamlit Interface
st.set_page_config(page_title="Unit Converter", page_icon="⚙️", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f4f4f9;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSelectbox>div>div>div>button {
            background-color: #f1f1f1;
            color: #555;
            border: none;
        }
        .stSelectbox>div>div>div>button:hover {
            background-color: #ddd;
        }
        .stNumberInput>div>div>input {
            border-radius: 5px;
            padding: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("Unit Converter ⚙️")

# Sidebar Layout
st.sidebar.title("Unit Converter Settings")
st.sidebar.markdown("""
    Select a unit category to start converting. You can choose from:
    - Length
    - Speed
    - Time
""")

# Select unit category
units = st.sidebar.selectbox("Select unit category", ("Length", "Speed", "Time"))

# User input for conversion value
from_value = st.number_input(f"Enter the value in {units}", min_value=0.0, step=0.1)

# Conversion logic
if units == "Length":
    # Length conversion options
    length_units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"]
    from_unit = st.sidebar.selectbox("From unit", length_units)
    to_unit = st.sidebar.selectbox("To unit", length_units)
    
    if from_value:
        result = convert_length(from_unit, to_unit, from_value)
        st.write(f"**{from_value} {from_unit}** is equal to **{result:.4f} {to_unit}**")

elif units == "Speed":
    # Speed conversion options
    speed_units = ["m/s", "km/h", "mph", "ft/s"]
    from_unit = st.sidebar.selectbox("From unit", speed_units)
    to_unit = st.sidebar.selectbox("To unit", speed_units)
    
    if from_value:
        result = convert_speed(from_unit, to_unit, from_value)
        st.write(f"**{from_value} {from_unit}** is equal to **{result:.4f} {to_unit}**")

elif units == "Time":
    # Time conversion options
    time_units = ["seconds", "minutes", "hours", "days", "weeks"]
    from_unit = st.sidebar.selectbox("From unit", time_units)
    to_unit = st.sidebar.selectbox("To unit", time_units)
    
    if from_value:
        result = convert_time(from_unit, to_unit, from_value)
        st.write(f"**{from_value} {from_unit}** is equal to **{result:.4f} {to_unit}**")

# Additional styling for better UX
st.markdown("""
    <hr style="border-top: 2px solid #4CAF50;"/>
    <footer style="text-align:center;">
        <p style="color:#777;">Created with ❤️ by Shoaib</p>
    </footer>
""", unsafe_allow_html=True)
