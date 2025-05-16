# main.py

import streamlit as st

# Import page functions
try:
    from Buji import buji
    from page_1 import page_1
    from page_2 import page_2
except ImportError as e:
    st.error(f"Error importing page module: {e}. Please ensure Buji.py, page_1.py, and page_2.py exist and contain the correct functions.")
    st.stop()

# --- Navigation logic ---
def navigate_to(page_name):
    """Changes the current page state in session_state and reruns the app."""
    st.session_state.current_page = page_name
    st.rerun()

# --- Page Controller ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "Buji"  # Default initial page

# Route to the correct page
if st.session_state.current_page == "Buji":
    buji(navigate_to)
elif st.session_state.current_page == "Page_1":
    page_1(navigate_to)
elif st.session_state.current_page == "Page_2":
    page_2(navigate_to)
