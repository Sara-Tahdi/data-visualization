import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Step 3: Upload CSV File
st.title("Formula Electric Car Data Viewer")

uploaded_file = st.file_uploader("data", type="csv")

if uploaded_file is not None:
    # Step 4: Load Data
    data = pd.read_csv(uploaded_file)
    st.write("Data Loaded Successfully!")
    
    # Step 5: Display Data
    st.subheader("Data Preview")
    st.dataframe(data.head())
    
    # Step 6: Choose Plotting Options
    st.subheader("Visualization Options")
    plot_type = st.selectbox("Select Plot Type", ["Line Plot", "Bar Chart"])
    
    # Step 7: Select X and Y Axes for Plotting
    x_axis = st.selectbox("Select X Axis", data.columns)
    y_axis = st.selectbox("Select Y Axis", data.columns)

    if st.button("Generate Plot"):
        plt.figure(figsize=(10, 5))
        
        if plot_type == "Line Plot":
            plt.plot(data[x_axis], data[y_axis], label=y_axis)
            plt.title(f"{y_axis} vs {x_axis}")
        
        elif plot_type == "Bar Chart":
            plt.bar(data[x_axis], data[y_axis], label=y_axis)
            plt.title(f"{y_axis} vs {x_axis}")
        
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.legend()
        plt.grid()
        st.pyplot(plt)
