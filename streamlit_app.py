import streamlit as st


def main():
    st.title("Emissions by Country | 2002-2022")
    st.info("Note: A blank chart means there is no available data for that country & emission type.")

    st.write("---")

    st.write("For more information on data used throughout this application, check out the kaggle listing below.")
    with st.expander("Data Source"):
        st.write("https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022")


if __name__ == "__main__":
    main()
