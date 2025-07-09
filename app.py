import streamlit as st
import pandas as pd

# Load data directly from GitHub
url = "https://raw.githubusercontent.com/BUFFALO-BLUE/toxic-divide/main/chester_mini.csv"
df = pd.read_csv(url)

# Simple dashboard
st.title("🚨 Toxic Divide: Chester, PA")
st.write("27% childhood asthma rate - 3x national average")

# Map
st.header("Pollution Hotspots")
st.map(df)

# Chart
st.header("Asthma vs. Income")
st.bar_chart(df.set_index('Neighborhood')[['Income', 'Asthma_Rate']])

# "ML" Insight
st.header("High-Risk Zones")
st.write(df[df['Pollution'] > 7]['Neighborhood'].tolist())
