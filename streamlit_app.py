import streamlit as st
from src.data import get_data


def main():
    st.title("Emissions by Country | 2002-2022")

    df = get_data()

    country = st.selectbox("Select country:", options=df['Country'].unique())
    country_df = df.loc[df['Country'] == country]

    st.bar_chart(country_df, x="Year", y="Total")
    st.dataframe(country_df)
    # st.dataframe(df)


if __name__ == "__main__":
    main()
