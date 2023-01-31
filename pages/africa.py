import streamlit as st

from src.data import get_data
from src.settings import (
    NORTH_AFRICA,
    WESTERN_AFRICA,
    SOUTHERN_AFRICA,
    EAST_AFRICA,
    CENTRAL_AFRICA,
)


def main():
    st.title("Africa")

    df = get_data()

    north_africa_tab, western_africa_tab, central_africa_tab, east_africa_tab, southern_africa_tab = st.tabs(
        ["North Africa", "Western Africa", "Central Africa", "East Africa", "Southern Africa"]
    )

    with north_africa_tab:
        st.subheader("North Africa")

        north_africa_selection = st.selectbox("Select country", options=NORTH_AFRICA)
        north_africa_df = df.loc[df['Country'] == north_africa_selection]

        st.bar_chart(north_africa_df, x="Year", y="Total")
        st.dataframe(north_africa_df)

    with western_africa_tab:
        st.subheader("Western Africa")

        western_africa_selection = st.selectbox("Select country", options=WESTERN_AFRICA)
        western_africa_df = df.loc[df['Country'] == western_africa_selection]

        st.bar_chart(western_africa_df, x="Year", y="Total")
        st.dataframe(western_africa_df)

    with central_africa_tab:
        st.subheader("Central Africa")

        central_africa_selection = st.selectbox("Select country", options=CENTRAL_AFRICA)
        central_africa_df = df.loc[df['Country'] == central_africa_selection]

        st.bar_chart(central_africa_df, x="Year", y="Total")
        st.dataframe(central_africa_df)

    with east_africa_tab:
        st.subheader("East Africa")

        east_africa_selection = st.selectbox("Select country", options=EAST_AFRICA)
        east_africa_df = df.loc[df['Country'] == east_africa_selection]

        st.bar_chart(east_africa_df, x="Year", y="Total")
        st.dataframe(east_africa_df)

    with southern_africa_tab:
        st.subheader("Southern Africa")

        southern_africa_selection = st.selectbox("Select country", options=SOUTHERN_AFRICA)
        southern_africa_df = df.loc[df['Country'] == southern_africa_selection]

        st.bar_chart(southern_africa_df, x="Year", y="Total")
        st.dataframe(southern_africa_df)


if __name__ == "__main__":
    main()
