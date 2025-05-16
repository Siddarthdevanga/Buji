import streamlit as st
import base64
import os

# --- Background Images ---
login_bg = "C:/Users/DELL/Music/SIDDARTH/photos/multi.jpg"
welcome_bg = "C:/Users/DELL/Music/SIDDARTH/photos/pic_2.jpg"

# --- Set Background Image Function ---
def set_background(image_path):
    if not os.path.exists(image_path):
        st.error(f"Background image not found: {image_path}")
        return

    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0);
    }}
    .stButton>button {{
        width: 100%;
        padding: 15px;
        font-size: 18px;
        border-radius: 8px;
        background-color: #2c662d;
        color: white;
    }}
    .stButton>button#next_button {{
        width: auto;
        padding: 12px 20px;
        font-size: 16px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Main Buji Function ---
def buji(navigate_to):
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "welcome_shown" not in st.session_state:
        st.session_state.welcome_shown = False

    # --- LOGIN PAGE ---
    if not st.session_state.logged_in:
        set_background(login_bg)

        st.markdown("<h2 style='text-align: center; color:#ffffff; margin-top: 200px;'>LOGIN TO YOUR UNIVERSE</h2>", unsafe_allow_html=True)

        email = st.text_input("Email Address", key="email")
        password = st.text_input("Password", type="password", key="password")
        login_button = st.button("Login", key="login_button")

        if login_button:
            if email == "harshithasiddarth@gmail.com" and password == "bemineforever":
                st.session_state.logged_in = True
                st.session_state.welcome_shown = False
                navigate_to("Buji")  # Keep in Buji to show welcome page next
            else:
                st.error("Invalid email or password.")

    # --- WELCOME PAGE ---
    elif not st.session_state.welcome_shown:
        set_background(welcome_bg)

        st.markdown("""
        <style>
        .welcome-container {
            background: rgba(0, 0, 0, 0.5);
            padding: 50px;
            border-radius: 20px;
            margin: 150px auto 0;
            width: 60%;
            text-align: center;
            color: #fff;
            font-family: 'Georgia', serif;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }
        .welcome-heading {
            font-size: 22px;
            font-style: italic;
            margin-bottom: 20px;
        }
        .welcome-text {
            font-size: 16px;
            line-height: 1.6;
            font-weight: 300;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="welcome-container">
            <div class="welcome-heading">Welcome to the Universe and making it even more beautiful 🌌</div>
            <div class="welcome-text">
                After all the trials and heartfelt prayers, the couple’s dream finally blossomed into reality the moment they saw their precious bundle of joy. A sweet little princess had arrived, bringing endless smiles and filling the family with happiness. She’s her daddy’s darling (BUJI), her mommy’s treasure, and already a mischievous whirlwind for her brothers!
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Next →", key="next_button"):
            st.session_state.welcome_shown = True
            navigate_to("Page_1")

    # Optional fallback if something goes wrong
    else:
        st.warning("Unable to determine next step. Please refresh the page.")
