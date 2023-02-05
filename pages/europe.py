import streamlit as st

from src.data import get_data
from src.settings import (
    EASTERN_EUROPE,
    NORTHERN_EUROPE,
    SOUTHERN_EUROPE,
    WESTERN_EUROPE,
    VALID_VALUE_SELECTIONS,
)


def main():
    st.set_page_config("Europe", layout="wide")
    st.title("Europe")

    df = get_data()

    eastern_europe_tab, northern_europe_tab, southern_europe_tab, western_europe_tab = st.tabs(
        ["Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe"]
    )

    with eastern_europe_tab:
        st.subheader("Eastern Europe")

        eastern_europe_selection = st.selectbox("Select country", options=EASTERN_EUROPE)
        eastern_europe_df = df.loc[df['Country'] == eastern_europe_selection]

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.subheader("Coal")
            st.bar_chart(eastern_europe_df, x="Year", y="Coal")
        with c2:
            st.subheader("Oil")
            st.bar_chart(eastern_europe_df, x="Year", y="Oil")
        with c3:
            st.subheader("Gas")
            st.bar_chart(eastern_europe_df, x="Year", y="Gas")
        with c4:
            st.subheader("Cement")
            st.bar_chart(eastern_europe_df, x="Year", y="Cement")

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

        st.bar_chart(northern_europe_df, x="Year", y=northern_europe_value)

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

        st.bar_chart(southern_europe_df, x="Year", y=southern_europe_value)

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

        st.bar_chart(western_europe_df, x="Year", y=western_europe_value)

        with st.expander(f"Display {western_europe_selection} DataFrame"):
            st.dataframe(western_europe_df)


if __name__ == "__main__":
    main()
