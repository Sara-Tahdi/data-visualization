def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call this in the main function with a path to your CSS file
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS for styling
local_css("style.css")

# Logo display
st.markdown("<div class='logo'><img src='logo.png' width='200'></div>", unsafe_allow_html=True)

# File upload
st.title('Upload xlsx')
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write('### VIEW EXCEL DATASET')
    st.dataframe(df)

    # Sidebar
    st.sidebar.title("Sidebar")
    st.sidebar.write("Xlsx cell 11: ", df.iloc[0, 0])  # Example for displaying specific cells
    st.sidebar.write("Xlsx cell 12: ", df.iloc[0, 1])
    st.sidebar.write("Xlsx cell 21: ", df.iloc[1, 0])
    st.sidebar.write("Xlsx cell 33: ", df.iloc[2, 2])

    # Plotting a chart from the Excel file
    st.write("### Chart Title")
    chart_data = df.iloc[:, :4]  # Modify this based on your Excel structure
    chart_data.plot(kind='bar')
    plt.title("Chart Title")
    plt.ylabel("Values")
    plt.xlabel("Categories")
    st.pyplot(plt)
else:
    st.write("Please upload an xlsx file.")
