import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data function
def load_data(file):
    # Assuming it's an Excel file; adapt for other formats
    df = pd.read_excel(file)
    return df

# Display basic info
def display_info(df):
    st.write(df.at[3,'b'])
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")
    st.write("Sample Data:")
    st.dataframe(df.head())

# Plot data function
def plot_data(df, selected_variable):
    st.write(f"### {selected_variable} Over Time")
    fig, ax = plt.subplots()
    ax.plot(df.iloc[:, 0], df[selected_variable])
    ax.set_xlabel('Time')
    ax.set_ylabel(selected_variable)
    ax.set_title(f'{selected_variable} over Time')
    st.pyplot(fig)

# Main Streamlit app
def main():
    st.title('MFE Log')

    # Upload file
    uploaded_file = st.file_uploader("Choose a log file", type=["xlsx", "csv"])

    if uploaded_file is not None:
        # Load the data
        df = load_data(uploaded_file)
        
        # Display information
        display_info(df)

        # Select a variable to visualize
        selected_variable = st.selectbox('Select a variable to plot', df.columns[1:])
        
        # Plot the selected variable
        plot_data(df, selected_variable)

if __name__ == '__main__':
    main()
