import streamlit as st

from streamlit_extras.colored_header import colored_header
from src.data import get_data
from src.settings import YEAR_DOUBLE_SELECT_SLIDER_DEFAULT, VALID_VALUE_SELECTIONS


def main():
    st.set_page_config("Australia", layout="centered")
    colored_header("Australia", description="", color_name="blue-70")

    df = get_data()

    australia_df = df.loc[df['Country'] == 'Australia']

    left_col, right_col = st.columns([3, 1])
    with left_col:
        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=australia_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="australia_year_selections")
    with right_col:
        emission_type = st.selectbox(label="Select value to display",
                                     options=VALID_VALUE_SELECTIONS,
                                     key="canada_value_selections")

    australia_df_query = australia_df.query("Year >= @low_year and Year <= @high_year")
    st.bar_chart(australia_df_query, x='Year', y=emission_type)
    st.dataframe(australia_df)


if __name__ == "__main__":
    main()
