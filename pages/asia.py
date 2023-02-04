import streamlit as st

from src.data import get_data
from src.settings import (
    VALID_VALUE_SELECTIONS,
    CENTRAL_ASIA,
    EAST_ASIA,
    SOUTH_ASIA,
    SOUTHEAST_ASIA,
    WESTERN_ASIA,
)


def main():
    st.set_page_config("Asia", layout="centered")
    st.title("Asia")

    df = get_data()

    central_asia_tab, east_asia_tab, south_asia_tab, southeast_asia_tab, western_asia_tab = st.tabs(
        ["Central Asia", "East Asia", "South Asia", "Southeast Asia", "Western Asia"]
    )

    with central_asia_tab:
        st.subheader("Central Asia")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            central_asia_selection = st.selectbox("Select country", options=CENTRAL_ASIA)
            central_asia_df = df.loc[df['Country'] == central_asia_selection]
        with right_column:
            central_asia_value = st.selectbox(label="Select value to display",
                                              options=VALID_VALUE_SELECTIONS,
                                              key="central_asia_value_selection")

        st.bar_chart(central_asia_df, x="Year", y=central_asia_value)
        st.dataframe(central_asia_df)

    with east_asia_tab:
        st.subheader("East Asia")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            east_asia_selection = st.selectbox("Select country", options=EAST_ASIA)
            east_asia_df = df.loc[df['Country'] == east_asia_selection]
        with right_column:
            east_asia_value = st.selectbox(label="Select value to display",
                                           options=VALID_VALUE_SELECTIONS,
                                           key="east_asia_value_selection")

        st.bar_chart(east_asia_df, x="Year", y=east_asia_value)
        st.dataframe(east_asia_df)

        # For multi-value purpose (will use later).
        # multi_value_selections = st.multiselect(label="Select value(s) to display:",
        #                                         options=VALID_VALUE_SELECTIONS)

        # if len(multi_value_selections) != 0:
        #     st.bar_chart(east_asia_df, x="Year", y=multi_value_selections)
        # else:
        #     st.info("Please select one or more value to display on bar chart.")

    with south_asia_tab:
        st.subheader("South Asia")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            south_asia_selection = st.selectbox("Select country", options=SOUTH_ASIA)
            south_asia_df = df.loc[df['Country'] == south_asia_selection]
        with right_column:
            south_asia_value = st.selectbox(label="Select value to display",
                                            options=VALID_VALUE_SELECTIONS,
                                            key="south_asia_value_selection")

        st.bar_chart(south_asia_df, x="Year", y=south_asia_value)
        st.dataframe(south_asia_df)

    with southeast_asia_tab:
        st.subheader("Southeast Asia")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            southeast_asia_selection = st.selectbox("Select country", options=SOUTHEAST_ASIA)
            southeast_asia_df = df.loc[df['Country'] == southeast_asia_selection]
        with right_column:
            southeast_asia_value = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="southeast_asia_value_selection")

        st.bar_chart(southeast_asia_df, x="Year", y=southeast_asia_value)
        st.dataframe(southeast_asia_df)

    with western_asia_tab:
        st.subheader("Western Asia")

        left_column, right_column = st.columns([3, 1])
        with left_column:
            western_asia_selection = st.selectbox("Select country", options=WESTERN_ASIA)
            western_asia_df = df.loc[df['Country'] == western_asia_selection]
        with right_column:
            western_asia_value = st.selectbox(label="Select value to display",
                                              options=VALID_VALUE_SELECTIONS,
                                              key="western_asia_value_selection")

        st.bar_chart(western_asia_df, x="Year", y=western_asia_value)
        st.dataframe(western_asia_df)


if __name__ == "__main__":
    main()
