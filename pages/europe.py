import streamlit as st

from src.data import get_data
from src.settings import (
    EASTERN_EUROPE,
    NORTHERN_EUROPE,
    SOUTHERN_EUROPE,
    WESTERN_EUROPE,
    VALID_VALUE_SELECTIONS,
    YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
)


def main():
    st.set_page_config("Europe", layout="centered")
    st.title("Europe")

    df = get_data()

    eastern_europe_tab, northern_europe_tab, southern_europe_tab, western_europe_tab = st.tabs(
        ["Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe"]
    )

    with eastern_europe_tab:
        st.subheader("Eastern Europe")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            eastern_europe_selection = st.selectbox("Select country", options=EASTERN_EUROPE)
            eastern_europe_df = df.loc[df['Country'] == eastern_europe_selection]
        with right_column:
            eastern_europe_value = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="eastern_europe_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=eastern_europe_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="eastern_europe_year_selections")

        st.write("---")

        eastern_europe_query = eastern_europe_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(eastern_europe_query, x="Year", y=eastern_europe_value)

        with st.expander(f"Display {eastern_europe_selection} DataFrame"):
            st.dataframe(eastern_europe_df)

    with northern_europe_tab:
        st.subheader("Northern Europe")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            northern_europe_selection = st.selectbox("Select country", options=NORTHERN_EUROPE)
            northern_europe_df = df.loc[df['Country'] == northern_europe_selection]
        with right_column:
            northern_europe_value = st.selectbox(label="Select value to display",
                                                 options=VALID_VALUE_SELECTIONS,
                                                 key="northern_europe_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=northern_europe_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="northern_europe_year_selections")

        st.write("---")

        northern_europe_query = northern_europe_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(northern_europe_query, x="Year", y=northern_europe_value)

        with st.expander(f"Display {northern_europe_selection} DataFrame"):
            st.dataframe(northern_europe_df)

    with southern_europe_tab:
        st.subheader("Southern Europe")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            southern_europe_selection = st.selectbox("Select country", options=SOUTHERN_EUROPE)
            southern_europe_df = df.loc[df['Country'] == southern_europe_selection]
        with right_column:
            southern_europe_value = st.selectbox(label="Select value to display",
                                                 options=VALID_VALUE_SELECTIONS,
                                                 key="southern_europe_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=southern_europe_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="southern_europe_year_selections")

        st.write("---")

        southern_europe_query = southern_europe_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(southern_europe_query, x="Year", y=southern_europe_value)

        with st.expander(f"Display {southern_europe_selection} DataFrame"):
            st.dataframe(southern_europe_df)

    with western_europe_tab:
        st.subheader("Western Europe")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            western_europe_selection = st.selectbox("Select country", options=WESTERN_EUROPE)
            western_europe_df = df.loc[df['Country'] == western_europe_selection]
        with right_column:
            western_europe_value = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="western_europe_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=western_europe_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="western_europe_year_selections")

        st.write("---")

        western_europe_query = western_europe_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(western_europe_query, x="Year", y=western_europe_value)

        with st.expander(f"Display {western_europe_selection} DataFrame"):
            st.dataframe(western_europe_df)


if __name__ == "__main__":
    main()
