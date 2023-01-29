import streamlit as st

from src.data import get_data
from src.settings import (
    VALID_VALUE_SELECTIONS,
    CARIBBEAN,
    CENTRAL_AMERICA,
    SOUTH_AMERICA,
)


def main():
    st.title("Americas")

    df = get_data()

    caribbean_tab, central_america_tab, south_america_tab, north_america_tab = st.tabs(
        ["Caribbean", "Central America", "South America", "North America"]
    )

    with caribbean_tab:
        st.subheader("Caribbean")
        caribbean_selection = st.selectbox("Select country", options=CARIBBEAN)

        caribbean_df = df.loc[df['Country'] == caribbean_selection]
        st.bar_chart(data=caribbean_df, x="Year", y="Total")

        caribbean_multiple_selections = st.multiselect(label="Select countries",
                                                       options=CARIBBEAN,
                                                       default=CARIBBEAN[:5])

        if len(caribbean_multiple_selections) >= 1:
            caribbean_query = df.query('Country == @caribbean_multiple_selections')

            st.dataframe(caribbean_query)

    with central_america_tab:
        st.subheader("Central America")
        central_america_selection = st.selectbox("Select country", options=CENTRAL_AMERICA)

        central_america_df = df.loc[df['Country'] == central_america_selection]
        st.dataframe(central_america_df)

    with south_america_tab:
        st.subheader("South America")
        south_america_selection = st.selectbox("Select country", options=SOUTH_AMERICA)

        south_america_df = df.loc[df['Country'] == south_america_selection]
        st.dataframe(south_america_df)

    with north_america_tab:
        st.subheader("North America")
        st.write("---")

        # DataFrame for each country in North America.
        usa_df = df.loc[df['Country'] == 'USA']
        canada_df = df.loc[df['Country'] == 'Canada']
        mexico_df = df.loc[df['Country'] == 'Mexico']

        st.subheader("United States of America")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            usa_low_year, usa_high_year = st.select_slider(label="Select time-frame",
                                                           options=usa_df['Year'],
                                                           value=(usa_df['Year'].min(), usa_df['Year'].max()))
        with right_column:
            usa_emission_type = st.selectbox(label="Select value to display",
                                             options=VALID_VALUE_SELECTIONS)

        usa_df_query = usa_df.query("Year >= @usa_low_year and Year <= @usa_high_year")
        st.bar_chart(usa_df_query, x="Year", y=usa_emission_type)

        st.dataframe(usa_df)

        st.subheader("Canada")
        st.dataframe(canada_df)

        st.subheader("Mexico")
        st.dataframe(mexico_df)


if __name__ == "__main__":
    main()
