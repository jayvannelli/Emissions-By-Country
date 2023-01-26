import streamlit as st

from src.data import get_data
from src.settings import (
    CENTRAL_ASIA,
    EAST_ASIA,
    SOUTH_ASIA,
    SOUTHEAST_ASIA,
    WESTERN_ASIA,
)


def main():
    st.title("Asia")

    df = get_data()

    central_asia_tab, east_asia_tab, south_asia_tab, southeast_asia_tab, western_asia_tab = st.tabs(
        ["Central Asia", "East Asia", "South Asia", "Southeast Asia", "Western Asia"]
    )

    with central_asia_tab:
        st.subheader("Central Asia")

        central_asia_selection = st.selectbox("Select country", options=CENTRAL_ASIA)
        central_asia_df = df.loc[df['Country'] == central_asia_selection]

        st.dataframe(central_asia_df)

    with east_asia_tab:
        st.subheader("East Asia")

        east_asia_selection = st.selectbox("Select country", options=EAST_ASIA)
        east_asia_df = df.loc[df['Country'] == east_asia_selection]

        st.dataframe(east_asia_df)

    with south_asia_tab:
        st.subheader("South Asia")

        south_asia_selection = st.selectbox("Select country", options=SOUTH_ASIA)
        south_asia_df = df.loc[df['Country'] == south_asia_selection]

        st.dataframe(south_asia_df)

    with southeast_asia_tab:
        st.subheader("Southeast Asia")

        southeast_asia_selection = st.selectbox("Select country", options=SOUTHEAST_ASIA)
        southeast_asia_df = df.loc[df['Country'] == southeast_asia_selection]

        st.dataframe(southeast_asia_df)

    with western_asia_tab:
        st.subheader("Western Asia")

        western_asia_selection = st.selectbox("Select country", options=WESTERN_ASIA)
        western_asia_df = df.loc[df['Country'] == western_asia_selection]

        st.dataframe(western_asia_df)


if __name__ == "__main__":
    main()
