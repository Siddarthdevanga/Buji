# main.py

import streamlit as st

# Import your page functions from their respective files
# Ensure these files exist and contain the functions defined
# to accept one argument (which will be the navigate_to function)
try:
    from Buji import buji
    from page_1 import page_1
    from page_2 import page_2
    from page_3 import page_3
    from page_4 import page_4
except ImportError as e:
    st.error(f"Error importing page module: {e}. Please ensure all page files (Buji.py, page_1.py, etc.) exist and the function names match the imports.")
    st.stop() # Stop execution if imports fail

# --- Navigation logic ---
def navigate_to(page_name):
    """Changes the current page state in session_state and reruns the app."""
    st.session_state.current_page = page_name
    st.rerun() # Rerun to immediately display the new page

# --- Page Controller ---

# Initialize session state for the current page if it doesn't exist
if "current_page" not in st.session_state:
    st.session_state.current_page = "Buji" # Set the initial page

# Call the appropriate page function based on the current state
# Pass the navigate_to function to each page function
if st.session_state.current_page == "Buji":
    buji(navigate_to)
elif st.session_state.current_page == "Page_1":
    # Ensure your page_1 function in page_1.py accepts one argument
    page_1(navigate_to)
elif st.session_state.current_page == "Page_2":
     # Ensure your page_2 function in page_2.py accepts one argument
    page_2(navigate_to)
elif st.session_state.current_page == "Page_3":
     # Ensure your page_3 function in page_3.py accepts one argument
    page_3(navigate_to)
elif st.session_state.current_page == "Page_4":
     # Ensure your page_4 function in page_4.py accepts one argument
    page_4(navigate_to)