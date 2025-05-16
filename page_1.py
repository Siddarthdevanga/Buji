# page_1.py

import streamlit as st
import base64

# --- Helper function to set the background ---
def set_background(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(f"""
            <style>
            /* Target the main app container */
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: 100%;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: white;
            }}
            [data-testid="stHeader"] {{
                background: rgba(0, 0, 0, 0);
            }}
            .stButton > button {{
                width: 160px;
                padding: 10px;
                font-size: 16px;
                border-radius: 8px;
                background-color: #2c662d;
                color: white;
                margin-top: 20px;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            .main-container {{
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
                min-height: 100vh;
                text-align: center;
                gap: 2vh;
                padding: 20px;
            }}
            .heading {{
                font-size: 3em;
                color: #FF69B4;
                text-shadow: 2px 2px #000;
                margin: 0;
                white-space: nowrap;
                overflow: hidden; /* Prevent overflow */
                text-overflow: ellipsis; /* Add ellipsis if text exceeds */
            }}
            .subheading {{
                color: #f5f5f5;
                font-size: 1.5em;
                margin-top: 0.5em;
            }}
            .retro-box {{
                width: 80%;
                max-width: 800px;
                padding: 20px;
                background-color: rgba(255, 239, 213, 0.85);
                border: 4px double #8B0000;
                border-radius: 15px;
                font-family: 'Courier New', Courier, monospace;
                font-size: 1.1em;
                color: #4B0082;
                box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.25);
                margin-bottom: 20px;
            }}
            </style>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"❌ Background image not found at path: {image_path}. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred while setting background: {e}")


# Define the page_1 function
def page_1(navigate):
    """Renders the content for Page 1."""
    set_background("photos/pic_3.png")

    # Use markdown for the content layout
    st.markdown(f"""
    <div class="main-container">
        <div class="heading">🎉🎂 WISH YOU MANY MORE HAPPY RETURNS OF THE DAY 🎂🎉</div>
        <div class="subheading">Wishing you lots of love, joy, and laughter!</div>
        <div class="retro-box">
            🌟 May your smile shine brighter than ever,As the moon shined brigther  on that day as you were born, Achieve all your dreams,and let every moment be as special as your presence!<br><br>
            😍Today is all about you the one who fills my days with happiness with a single text and with your sweet Voice,I feel so lucky you texted me back😍<br><br>
            🫠No matter always remember you are always the best and one of the unique creations of god Just like me🫠<br><br>
            💖 Keep sparkling and spreading happiness. You deserve all the best life has to offer INCLUDING ME! 💖<br><br>
            💙From being stranger to now my day feels incomplete without talking to you ,it has been beautiful for me💙 <br><br>
            🩺Also do remember to take care of yourself and your health🩺
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Display balloons
    st.balloons()

    # Add the navigation button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Next →", key="page1_next_button"):
            navigate("Page_2")
