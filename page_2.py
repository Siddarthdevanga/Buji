import streamlit as st
import base64
import os

def page_2(navigate_to):
    def set_background(image_path):
        if not os.path.exists(image_path):
            st.error(f"❌ Background image not found at {image_path}")
            return

        try:
            with open(image_path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode()
            st.markdown(f"""
                <style>
                    [data-testid="stAppViewContainer"] {{
                        background-image: url("data:image/png;base64,{encoded}");
                        background-size: cover;
                        background-position: center;
                        background-repeat: no-repeat;
                        background-attachment: fixed;
                        color: white;
                        min-height: 100vh;
                        padding-bottom: 0px !important;
                    }}
                    [data-testid="stHeader"],
                    [data-testid="stToolbar"],
                    [data-testid="stDecoration"] {{
                        background: none;
                    }}
                    h1, p {{
                        color: white !important;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    }}
                    div[data-testid="stVerticalBlock"] > div:first-child {{
                        margin-top: 35vh;
                        text-align: center;
                    }}
                    .full-width-bottom-button {{
                        position: fixed;
                        bottom: 0;
                        left: 0;
                        width: 100%;
                        padding: 0;
                        margin: 0;
                        z-index: 9999;
                    }}
                    .full-width-bottom-button .stButton>button {{
                        width: 100vw;
                        height: 60px;
                        font-size: 22px;
                        border: none;
                        border-radius: 0;
                        background-color: #ff69b4;
                        color: white;
                        cursor: pointer;
                    }}
                    .full-width-bottom-button .stButton>button:hover {{
                        background-color: #ff1493;
                        box-shadow: 0 0 12px rgba(255, 105, 180, 0.6);
                    }}
                </style>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"⚠️ Error loading background image: {str(e)}")

    # Set background
    image_path = "C:/Users/DELL/Music/SIDDARTH/photos/pic_4.png"
    set_background(image_path)

    # Initialize session state variable if not set
    if "show_chats" not in st.session_state:
        st.session_state["show_chats"] = False

    # If show_chats is False, show the "Next" button
    if not st.session_state["show_chats"]:
        st.markdown('<div class="full-width-bottom-button">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([0.01, 0.98, 0.01])
        with col2:
            if st.button("Next →", key="page2_next_button"):
                st.session_state["show_chats"] = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Show Instagram-style chat screen
        st.markdown("""
            <style>
                .chats-screen {
                    background-color: #121212;
                    color: #e0e0e0;
                    padding: 10px;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1000;
                    display: flex;
                    flex-direction: column;
                    font-family: sans-serif;
                }
                /* Add all your other chat styles here */
            </style>
            <div class="chats-screen">
                <div class="chats-header">
                    <div class="chats-header-left">
                        <span class="chat-name-header">Buji 💙</span>
                    </div>
                    <div class="chats-header-right">
                        <!-- SVGs here -->
                    </div>
                </div>
                <div class="chat-list">
                    <!-- Chat messages -->
                    <div style="text-align: center; color: #777; margin-bottom: 8px;">2:19 PM</div>
                    <div class="message-container sent">
                        <div class="message">Hey Buji, how are you doing?</div>
                        <div class="timestamp">You</div>
                    </div>
                    <div class="message-container received">
                        <div class="message received">I'm good, just thinking about you ❤️</div>
                        <div class="timestamp">Buji</div>
                    </div>
                </div>
                <div class="bottom-bar">
                    <input type="text" placeholder="Message...">
                </div>
            </div>
        """, unsafe_allow_html=True)
