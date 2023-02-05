import streamlit as st

from streamlit_extras.colored_header import colored_header
from src.data import get_data
from src.settings import (
    CARIBBEAN,
    CENTRAL_AMERICA,
    SOUTH_AMERICA,
    VALID_VALUE_SELECTIONS,
    YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
)


def main():
    st.set_page_config("Americas", layout="centered")
    st.title("Americas")

    df = get_data()

    caribbean_tab, central_america_tab, south_america_tab, north_america_tab = st.tabs(
        ["Caribbean", "Central America", "South America", "North America"]
    )

    with caribbean_tab:
        st.subheader("Caribbean")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            caribbean_selection = st.selectbox("Select country", options=CARIBBEAN)
            caribbean_df = df.loc[df['Country'] == caribbean_selection]
        with right_column:
            caribbean_value = st.selectbox(label="Select value to display",
                                           options=VALID_VALUE_SELECTIONS,
                                           key="caribbean_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=caribbean_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="caribbean_year_selections")

        st.write("---")

        caribbean_query = caribbean_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(caribbean_query, x="Year", y=caribbean_value)

        with st.expander(f"Display {caribbean_selection} DataFrame"):
            st.dataframe(caribbean_df)

    with central_america_tab:
        st.subheader("Central America")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            central_america_selection = st.selectbox("Select country", options=CENTRAL_AMERICA)
            central_america_df = df.loc[df['Country'] == central_america_selection]
        with right_column:
            central_america_value = st.selectbox(label="Select value to display",
                                                 options=VALID_VALUE_SELECTIONS,
                                                 key="central_america_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=central_america_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="central_america_year_selections")

        st.write("---")

        central_america_query = central_america_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(central_america_query, x="Year", y=central_america_value)

        with st.expander(f"Display {central_america_selection} DataFrame"):
            st.dataframe(central_america_df)

    with south_america_tab:
        st.subheader("South America")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            south_america_selection = st.selectbox("Select country", options=SOUTH_AMERICA)
            south_america_df = df.loc[df['Country'] == south_america_selection]
        with right_column:
            south_america_value = st.selectbox(label="Select value to display",
                                               options=VALID_VALUE_SELECTIONS,
                                               key="south_america_value_selection")

        low_year, high_year = st.select_slider(label="Select time-frame",
                                               options=south_america_df['Year'],
                                               value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                               key="south_america_year_selections")

        st.write("---")

        south_america_query = south_america_df.query("Year >= @low_year and Year <= @high_year")
        st.bar_chart(south_america_query, x="Year", y=south_america_value)

        with st.expander(f"Display {south_america_selection} DataFrame"):
            st.dataframe(south_america_df)

    with north_america_tab:
        # DataFrame for each country in North America.
        usa_df = df.loc[df['Country'] == 'USA']
        canada_df = df.loc[df['Country'] == 'Canada']
        mexico_df = df.loc[df['Country'] == 'Mexico']

        colored_header("United States of America", description="", color_name="light-blue-70")

        usa_left_col, usa_right_col = st.columns([3, 1])
        with usa_left_col:
            usa_low_year, usa_high_year = st.select_slider(label="Select time-frame",
                                                           options=usa_df['Year'],
                                                           value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                                           key="usa_year_selections")
        with usa_right_col:
            usa_emission_type = st.selectbox(label="Select value to display",
                                             options=VALID_VALUE_SELECTIONS,
                                             key="usa_value_selections")

        usa_df_query = usa_df.query("Year >= @usa_low_year and Year <= @usa_high_year")
        st.bar_chart(usa_df_query, x="Year", y=usa_emission_type)

        with st.expander("Display United States DataFrame"):
            st.dataframe(usa_df)

        st.write("---")

        colored_header("Canada", description="", color_name="red-70")

        canada_left_col, canada_right_col = st.columns([3, 1])
        with canada_left_col:
            canada_low_year, canada_high_year = st.select_slider(label="Select time-frame",
                                                                 options=canada_df['Year'],
                                                                 value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                                                 key="canada_year_selections")
        with canada_right_col:
            canada_emission_type = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="canada_value_selections")

        canada_df_query = canada_df.query("Year >= @canada_low_year and Year <= @canada_high_year")
        st.bar_chart(canada_df_query, x="Year", y=canada_emission_type)

        with st.expander("Display Canada DataFrame"):
            st.dataframe(canada_df)

        st.write("---")

        colored_header("Mexico", description="", color_name="green-70")

        mexico_left_col, mexico_right_col = st.columns([3, 1])
        with mexico_left_col:
            mexico_low_year, mexico_high_year = st.select_slider(label="Select time-frame",
                                                                 options=mexico_df['Year'],
                                                                 value=YEAR_DOUBLE_SELECT_SLIDER_DEFAULT,
                                                                 key="mexico_year_selections")
        with mexico_right_col:
            mexico_emission_type = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="mexico_value_selections")

        mexico_df_query = mexico_df.query("Year >= @mexico_low_year and Year <= @mexico_high_year")
        st.bar_chart(mexico_df_query, x="Year", y=mexico_emission_type)

        with st.expander("Display Mexico DataFrame"):
            st.dataframe(mexico_df)


if __name__ == "__main__":
    main()
