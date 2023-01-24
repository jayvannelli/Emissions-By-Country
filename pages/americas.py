import streamlit as st

from src.data import get_data
from src.settings import CARIBBEAN, CENTRAL_AMERICA, SOUTH_AMERICA


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
        north_america_selection = st.selectbox("Select country", options=["Canada", "Mexico", "USA"])

        north_america_df = df.loc[df['Country'] == north_america_selection]
        st.dataframe(north_america_df)


if __name__ == "__main__":
    main()
