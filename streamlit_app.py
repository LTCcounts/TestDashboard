import streamlit as st
import pandas as pd
import math
from pathlib import Path
from numpy.random import default_rng as rng
import webbrowser

def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.image("data/header.png")
        st.text_input("Welcome. Please input password to proceed:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password. Please try again.")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.caption("Password accepted.")
    # ... rest of your app ...
    st.image("header.png")
    st.header("Treasurer's Dashboard", divider='gray')
    #st.write("This page is under development.")
   



    df = pd.read_csv('data/chapter_bal.csv')
    df_dues = pd.read_csv('data/pnwsu_dues.csv')
    df_pl = pd.read_csv('data/pnwsu_pl.csv')
    #with st.expander('About the dashboard'):
        #st.header("About the dashboard:")
    st.caption("If you run into any issues or have questions about the data, please email: Treasurer@pnwsu.org.")

    chapters = st.multiselect(
        "Select chapter(s)",
        df.Chapter.unique(),
        ['WORKING WA',
    'BSSU',
    'LA LABOR FED',
    'PROTEC17',
    'SEIU 925 ',
    'SEIU 2015 ',
    'SEIU 221 ',
    'UFCW 3000',
    'MEAWU',
    'NVLF',
    'UDWU',
    'UFCW367',
    'KIWA',
    'SEIU 121RN ',
    'UFCW 21 '
    ],
    )

    years = st.slider("Select year(s)", 2023, 2026, (2025, 2026),key="years")

    df_filtered = df[(df["Chapter"].isin(chapters)) & (df["Year"].between(years[0], years[1]))]
    df_dues_filtered = df_dues[(df_dues["Chapter"].isin(chapters)) & (df_dues["Year"].between(years[0], years[1]))]

    with st.expander('At-Large Finances'):
        #st.header("About the dashboard:")
        st.write("This table displays the total income and expenses for PNWSU by year. This information is also reported on our LM forms. You can search for the full LM reports with OLMS at the link below.")
        st.link_button("OLMS Union Search","https://olmsapps.dol.gov/query/getOrgQry.do")
        st.dataframe(df_pl.set_index(df_pl.columns[0]))

    with st.expander('Chapter Account Balances'):
        #st.header("About the dashboard:")
        st.write("These records reflect account balances presented at monthly e-board meetings, and so offer a snapshot of account balances over time.")
        st.write("Last updated: 1/22/2026")
        st.dataframe(df_filtered.set_index(df.columns[0]))
    
        col1, col2 = st.columns(2)
        # GF
        with col1:
            st.line_chart(
                df_filtered,
                x='Date',
                y='General Fund',
                color='Chapter'
                )
        # Strike/Savings
        with col2:
            st.line_chart(
                df_filtered,
                x='Date',
                y='Savings/Strike',
                color='Chapter'
            )

    with st.expander('Annual Dues Income'):
        #st.header("About the dashboard:")
        st.write("Total dues income by chapter, by year")
        st.dataframe(df_dues_filtered.set_index(df.columns[0]))

    with st.expander('Resources'):
        #st.header("About the dashboard:")
        st.write("Find other PNWSU content below")
        colz1, colz2, colz3 = st.columns(3)

        with colz1:

            st.link_button("PNWSU website","https://pnwsu.org")

        with colz2:
        
            st.link_button("At-Large C&B and CBAs","https://pnwsu.org/resources/")
        
        with colz3:

            st.link_button("Online store","https://pnwsu.myshopify.com/")
            
