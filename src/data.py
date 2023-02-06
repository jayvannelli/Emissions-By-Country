import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)
def get_data():
    return pd.read_csv("data/emissions_data.csv")
