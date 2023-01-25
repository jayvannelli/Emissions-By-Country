import streamlit as st

from src.data import get_data
from src.settings import (
    EASTERN_EUROPE,
    NORTHERN_EUROPE,
    SOUTHERN_EUROPE,
    WESTERN_EUROPE,
)


def main():
    st.title("Europe")

    df = get_data()

    eastern_europe_tab, northern_europe_tab, southern_europe_tab, western_europe_tab = st.tabs(
        ["Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe"]
    )

    with eastern_europe_tab:
        st.subheader("Eastern Europe")

        east_europe_selection = st.selectbox("Select country", options=EASTERN_EUROPE)
        east_europe_df = df.loc[df['Country'] == east_europe_selection]

        st.dataframe(east_europe_df)

    with northern_europe_tab:
        st.subheader("Northern Europe")

        north_europe_selection = st.selectbox("Select country", options=NORTHERN_EUROPE)
        north_europe_df = df.loc[df['Country'] == north_europe_selection]

        st.dataframe(north_europe_df)

    with southern_europe_tab:
        st.subheader("Southern Europe")

        south_europe_selection = st.selectbox("Select country", options=SOUTHERN_EUROPE)
        south_europe_df = df.loc[df['Country'] == south_europe_selection]

        st.dataframe(south_europe_df)

    with western_europe_tab:
        st.subheader("Western Europe")

        west_europe_selection = st.selectbox("Select country", options=WESTERN_EUROPE)
        west_europe_df = df.loc[df['Country'] == west_europe_selection]

        st.dataframe(west_europe_df)


if __name__ == "__main__":
    main()