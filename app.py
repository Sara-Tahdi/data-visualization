import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objs as go
import numpy as np
import os

# Set up page configuration
st.set_page_config(page_title="MFE", page_icon="🚗", layout="wide")
st.header("Logs Analysis")

# Custom CSS not Streamlit
theme_plotly = None

# Load Style css
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar

# MFE logo
st.sidebar.image("assets/MFE_logo.jpg", use_column_width=True)

# Place the file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader('Upload your data file', type="xlsx")

# Function to load the default file if no file is uploaded
def load_default_data():
    # Use raw string or double backslashes for Windows paths
    default_file_path = r"data\mfe_log.xlsx"  # Correcting the file path for Windows
    print(f"Looking for the file at: {default_file_path}")
    
    if os.path.exists(default_file_path):
        return pd.read_excel(default_file_path, header=14)
    else:
        st.sidebar.error(f"Default file '{default_file_path}' not found. Please upload a file.")
        return None

# Data display
def dataView():
    with st.expander("VIEW DATASET"):
        selected_variables = st.multiselect('Filter: ', table_df.columns, default=["Time"])
        st.dataframe(table_df[selected_variables], use_container_width=True)
        
    # Create a space
    st.write("")
    st.write("")
    
    graphs(selected_variables)

colours = []  # Colours used in the graph

# Choosing a colour to plot the different graph variables
def colour_picker():
    color = list(np.random.choice(range(256), size=3))
    if color in colours:
        colour_picker()
    else:
        colours.append(color)
        return color

# Line graph
def graphs(selected_variables):
    st.line_chart(table_df)

# Check if file is uploaded
if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file, header=14)
    # Select data starting from row 19
    table_df = df.iloc[4:]

    # Removing blank cells
    table_df = table_df.dropna(how='all')
    
    # HOME PAGE
    dataView()
else:    
    # If no file is uploaded, attempt to load the default data
    st.sidebar.info("No file uploaded. Loading the default data...")
    df = load_default_data()

    if df is not None:
        table_df = df.iloc[4:].dropna(how='all')
        dataView()  # Show the default data
    else:
        st.sidebar.warning("Unable to load the default file. Please upload a file.")
