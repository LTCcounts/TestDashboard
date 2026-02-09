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
        st.image("data/WUWskyline2.png")
        st.text_input("Welcome. Please input password to proceed:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.caption("Password accepted.")
    # ... rest of your app ...
    st.image("data/WUWskyline2.png")
    st.header("Treasurer's Dashboard", divider='gray')
    st.write("This page is under development.")
   