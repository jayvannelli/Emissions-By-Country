import streamlit as st

from src.data import get_data
from src.settings import (
    VALID_VALUE_SELECTIONS,
    NORTH_AFRICA,
    WESTERN_AFRICA,
    SOUTHERN_AFRICA,
    EAST_AFRICA,
    CENTRAL_AFRICA,
)


def main():
    st.set_page_config("Africa", layout="centered")
    st.title("Africa")

    df = get_data()

    north_africa_tab, western_africa_tab, central_africa_tab, east_africa_tab, southern_africa_tab = st.tabs(
        ["North Africa", "Western Africa", "Central Africa", "East Africa", "Southern Africa"]
    )

    with north_africa_tab:
        st.subheader("North Africa")

        left_column, right_column = st.columns([3, 1])

        with left_column:
            north_africa_selection = st.selectbox("Select country", options=NORTH_AFRICA)
            north_africa_df = df.loc[df['Country'] == north_africa_selection]
        with right_column:
            north_africa_value = st.selectbox(label="Select value to display",
                                              options=VALID_VALUE_SELECTIONS,
                                              key="north_africa_value_selection")

        st.bar_chart(north_africa_df, x="Year", y=north_africa_value)

        st.dataframe(north_africa_df)

    with western_africa_tab:
        st.subheader("Western Africa")

        left_column, right_column = st.columns([3, 1])

        with left_column:
            western_africa_selection = st.selectbox("Select country", options=WESTERN_AFRICA)
            western_africa_df = df.loc[df['Country'] == western_africa_selection]
        with right_column:
            western_africa_value = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="western_africa_value_selection")

        st.bar_chart(western_africa_df, x="Year", y=western_africa_value)
        st.dataframe(western_africa_df)

    with central_africa_tab:
        st.subheader("Central Africa")

        left_column, right_column = st.columns([3, 1])

        with left_column:
            central_africa_selection = st.selectbox("Select country", options=CENTRAL_AFRICA)
            central_africa_df = df.loc[df['Country'] == central_africa_selection]
        with right_column:
            central_africa_value = st.selectbox(label="Select value to display",
                                                options=VALID_VALUE_SELECTIONS,
                                                key="central_africa_value_selection")

        st.bar_chart(central_africa_df, x="Year", y=central_africa_value)
        st.dataframe(central_africa_df)

    with east_africa_tab:
        st.subheader("East Africa")

        left_column, right_column = st.columns([3, 1])

        with left_column:
            east_africa_selection = st.selectbox("Select country", options=EAST_AFRICA)
            east_africa_df = df.loc[df['Country'] == east_africa_selection]
        with right_column:
            east_africa_value = st.selectbox(label="Select value to display",
                                             options=VALID_VALUE_SELECTIONS,
                                             key="east_africa_value_selection")

        st.bar_chart(east_africa_df, x="Year", y=east_africa_value)
        st.dataframe(east_africa_df)

    with southern_africa_tab:
        st.subheader("Southern Africa")

        left_column, right_column = st.columns([3, 1])

        with left_column:
            southern_africa_selection = st.selectbox("Select country", options=SOUTHERN_AFRICA)
            southern_africa_df = df.loc[df['Country'] == southern_africa_selection]
        with right_column:
            southern_africa_value = st.selectbox(label="Select value to display",
                                                 options=VALID_VALUE_SELECTIONS,
                                                 key="southern_africa_value_selection")

        st.bar_chart(southern_africa_df, x="Year", y=southern_africa_value)
        st.dataframe(southern_africa_df)


if __name__ == "__main__":
    main()
