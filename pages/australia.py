import streamlit as st

from src.data import get_data


def main():
    st.set_page_config("Australia", layout="centered")
    st.title("Australia")

    df = get_data()

    australia_df = df.loc[df['Country'] == 'Australia']
    st.dataframe(australia_df)


if __name__ == "__main__":
    main()
