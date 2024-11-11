import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the page configuration
st.set_page_config(page_title="Traffic Analysis", layout="wide")

# Title and Description
st.title("Traffic Data Analysis")
st.write("This application provides an interactive analysis of traffic data.")

# Load the data
@st.cache
def load_data():
    # Replace 'your_data.csv' with your actual data file if needed
    data = pd.read_csv('traffic_sao_paulo.csv')  # update with the path to your dataset
    return data

data = load_data()

# Display raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Traffic Data")
    st.write(data)

# Basic Data Information
st.subheader("Basic Data Overview")
st.write(f"Number of rows: {data.shape[0]}")
st.write(f"Number of columns: {data.shape[1]}")
st.write(data.describe())

# Exploratory Data Analysis (EDA)
st.subheader("Exploratory Data Analysis")

# Select Columns for EDA
columns = st.multiselect("Select Columns to Analyze", data.columns)

if columns:
    st.write("Selected Data")
    st.write(data[columns].describe())

    # Plotting
    st.subheader("Distribution of Selected Columns")
    for col in columns:
        fig, ax = plt.subplots()
        sns.histplot(data[col], kde=True, ax=ax)
        st.pyplot(fig)

# Correlation Analysis
st.subheader("Correlation Analysis")
correlation = data.corr()
st.write("Correlation Matrix")
st.write(correlation)

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Time-Series Analysis (If applicable)
if 'Date' in data.columns:
    st.subheader("Time Series Analysis")
    data['Date'] = pd.to_datetime(data['Date'])
    time_series_data = data.set_index('Date')

    # Plotting
    st.line_chart(time_series_data)

# Conclusion
st.subheader("Conclusion")
st.write("This dashboard provides a basic analysis of traffic data.")

