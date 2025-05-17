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

    # Set background - Replace with your actual image path
    image_path = "photos/pic_4.png"
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
                /* Ensure the app container doesn't hide the fixed elements */
                [data-testid="stAppViewContainer"] > .main {
                    padding-bottom: 0px !important; /* Remove default padding if it interferes */
                    padding-top: 0px !important;
                }
                [data-testid="stVerticalBlock"] {
                    gap: 0rem; /* Remove gap between vertical blocks if any */
                }


                .chats-screen {
                    background-color: #000; /* Instagram dark mode background */
                    color: #fff;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1000;
                    display: flex;
                    flex-direction: column;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
                    overflow: hidden; /* Hide scrollbar on the main container */
                }

                .chats-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 15px; /* Adjusted padding */
                    background-color: #000; /* Pure black header */
                    border-bottom: 1px solid #262626; /* Subtle border */
                    flex-shrink: 0; /* Prevent header from shrinking */
                }

                .chats-header-left {
                    display: flex;
                    align-items: center;
                    gap: 10px; /* Space between back arrow, avatar, and name */
                }

                .header-back-arrow {
                    font-size: 1.5em;
                    color: #fff;
                    cursor: pointer;
                }

                .header-avatar {
                    width: 32px; /* Smaller avatar */
                    height: 32px;
                    background-color: #555; /* Placeholder color */
                    border-radius: 50%;
                    flex-shrink: 0; /* Prevent avatar from shrinking */
                }


                .chat-name-header {
                    font-weight: 600; /* Semi-bold */
                    font-size: 1em; /* Slightly smaller font */
                    color: #fff;
                    display: flex;
                    flex-direction: column; /* Allow name and status on separate lines */
                    line-height: 1.2;
                }

                .chat-status-header {
                     font-size: 0.7em;
                     font-weight: 400;
                     color: #a0a0a0; /* Lighter gray for status */
                }


                .chats-header-right {
                    display: flex;
                    align-items: center;
                    gap: 20px; /* Space between icons */
                    color: #fff; /* Icon color */
                }

                 .header-icon {
                    /* Using text placeholders for icons, ideally SVGs */
                    font-size: 1.3em; /* Adjusted icon size */
                    cursor: pointer;
                 }


                .chat-list {
                    flex-grow: 1;
                    overflow-y: auto; /* Enable scrolling for messages */
                    padding: 10px;
                    display: flex;
                    flex-direction: column; /* Stack messages vertically */
                    gap: 5px; /* Smaller space between message containers */
                }

                /* Style for the scrollbar (optional) */
                .chat-list::-webkit-scrollbar {
                    width: 5px;
                }

                .chat-list::-webkit-scrollbar-track {
                    background: #1a1a1a;
                }

                .chat-list::-webkit-scrollbar-thumb {
                    background: #333;
                    border-radius: 2.5px;
                }

                .chat-list::-webkit-scrollbar-thumb:hover {
                    background: #555;
                }


                .message-container {
                    display: flex;
                    width: 100%;
                    position: relative; /* Needed for timestamp positioning */
                    margin-bottom: 8px; /* Space below the message container */
                }

                .message-container.sent {
                    justify-content: flex-end; /* Align sent messages to the right */
                }

                .message-container.received {
                    justify-content: flex-start; /* Align received messages to the left */
                }

                .message {
                    max-width: 75%; /* Limit message width */
                    padding: 10px 12px;
                    border-radius: 18px; /* More rounded corners */
                    line-height: 1.4;
                    word-wrap: break-word; /* Break long words */
                    font-size: 0.95em;
                    position: relative; /* Needed for triangle tail effect if added later */
                }

                .message-container.sent .message {
                    background-color: #8a2be2; /* Purple color from image */
                    color: white;
                    /* Adjust border radius for the tail side */
                    border-top-right-radius: 18px;
                    border-bottom-right-radius: 4px; /* Less rounded tail corner */
                    border-top-left-radius: 18px;
                    border-bottom-left-radius: 18px;
                }

                .message-container.received .message {
                    background-color: #262626; /* Dark gray from image */
                    color: white;
                     /* Adjust border radius for the tail side */
                    border-top-left-radius: 18px;
                    border-bottom-left-radius: 4px; /* Less rounded tail corner */
                    border-top-right-radius: 18px;
                    border-bottom-right-radius: 18px;
                }

                .timestamp {
                    font-size: 0.7em;
                    color: #888; /* Lighter gray for timestamps */
                    margin-top: 2px;
                    position: absolute;
                    bottom: -15px; /* Adjust vertical position */
                    white-space: nowrap; /* Prevent timestamp from wrapping */
                }

                 .message-container.sent .timestamp {
                    right: 0; /* Align timestamp to the right for sent messages */
                    transform: translateX(calc(100% + 5px)); /* Position right of the bubble */
                 }

                /* Adjusting received timestamp position to be slightly to the right of the message end */
                 .message-container.received .timestamp {
                    left: auto; /* Override default left positioning */
                    right: 0; /* Position relative to the right edge of the container */
                    transform: translateX(calc(100% + 5px)); /* Position right of the bubble */
                 }


                 /* Basic styling for date/time dividers */
                 .chat-date-divider {
                     text-align: center;
                     color: #888; /* Match timestamp color */
                     margin: 15px 0 8px 0;
                     font-size: 0.75em; /* Slightly larger than timestamp */
                     font-weight: 500; /* Semi-bold like in image */
                 }


                .bottom-bar {
                    flex-shrink: 0; /* Prevent bottom bar from shrinking */
                    padding: 8px 15px; /* Adjusted padding */
                    background-color: #000; /* Pure black */
                    display: flex;
                    align-items: center;
                    gap: 10px; /* Space between input and icons */
                }

                .bottom-bar .icon-container {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                }


                .bottom-bar input[type="text"] {
                    flex-grow: 1; /* Input takes up available space */
                    padding: 10px 15px;
                    border: none;
                    border-radius: 25px; /* Rounded input field */
                    background-color: #262626; /* Input background color */
                    color: white;
                    font-size: 1em;
                    outline: none; /* Remove outline on focus */
                    height: 40px; /* Fixed height for input */
                }

                .bottom-bar input[type="text"]::placeholder {
                    color: #888; /* Placeholder color */
                }

                 .bottom-bar .icon {
                    font-size: 1.5em; /* Icon size */
                    color: #0095F6; /* Instagram blue for icons */
                    cursor: pointer;
                 }

                .bottom-bar .like-icon {
                     color: #fff; /* White like/heart icon */
                     font-size: 1.5em;
                     cursor: pointer;
                }

            </style>
            <div class="chats-screen">
                <div class="chats-header">
                    <div class="chats-header-left">
                         <span class="header-back-arrow">&lt;</span>
                         <div class="header-avatar"></div>
                        <span class="chat-name-header">
                            Buji 💙
                            <span class="chat-status-header">harshuuu..</span>
                        </span>
                    </div>
                    <div class="chats-header-right">
                        <span class="header-icon">📞</span> <span class="header-icon">ℹ️</span> </div>
                </div>
                <div class="chat-list">
                    <div class="chat-date-divider">20 DEC AT 9:44 PM</div>
                    <div class="message-container sent">
                        <div class="message">Hi Harshitha<br>I know this is little awkward, But wanted to let you know something. you had updated a story of yours few days back in black saree, You were looking really pretty in traditionals, I think i have little crush on you.<br><br>I was thinking to ask you on date for a long time.<br>Please do let me know if your interested and comfortable<br><br>Zero pressure.<br><br>If you Dont remember me, I was one of your seniors in school</div>
                        <div class="timestamp">2:19 PM</div> </div>
                    <div class="chat-date-divider">20 DEC AT 11:38 PM</div>
                     <div class="message-container received">
                        <div class="message">Heyy hii</div>
                        <div class="timestamp">2:20 PM</div> </div>
                     <div class="message-container received">
                        <div class="message">Okayy this is a new thing!🥳<br>I didn't know this</div>
                        <div class="timestamp">2:20 PM</div> </div>
                      <div class="message-container received">
                        <div class="message">First of all thanks for the Compliment......blah blah 😄😄</div>
                        <div class="timestamp">2:20 PM</div> </div>
                     <div class="message-container sent">
                        <div class="message">blah blah blah blah blah blah</div>
                        <div class="timestamp">2:21 PM</div> </div>
                     <div class="message-container received">
                        <div class="message">blah blah.</div>
                        <div class="timestamp">2:22 PM</div> </div>
                         <div class="message-container sent">
                        <div class="message">blah blah blah blah blah blah</div>
                        <div class="timestamp">2:21 PM</div> </div>
                        <div class="message">Hi BUJIMAAAA🫠<br> From here to our endless conversation from only weekendchats too gradually to even weekdays (But it doesnt count ,You dont text me back properly)Then to calls ,hearing your sweet voice in late night calls.<br><br>Sharing about my life to you which I have not done with anyone and also getting to know you not even 10% as you said<br>Even that 10% was more than enough for me ,TO fall for you like anything<br><br>I dont know how you are with others ,you have been really kind too me ,Even during my non-sense at peak times<br><br>Really god knows how we connected over online and I have already assumed you as my wife (Sorry, I know you Deserve far better than me) Really Dont know where this is Going to end ,Hope it ends GOOD<br><br>Lastly Wishing you a MANY MORE HAPPY RETURNS OF THE DAY ,HAVE A FABALOUS 23<br><br>MAY YOUR GOOD HEART FIND AND BE IN GOOD HANDS</div>
                </div>
                <div class="bottom-bar">
                     <span class="icon">📷</span> <div class="icon-container">
                        <span class="icon">🖼️</span> <span class="icon">🎤</span> </div>
                    <input type="text" placeholder="Message...">
                    <span class="like-icon">❤️</span> <span class="icon">➕</span> </div>
            </div>
        """, unsafe_allow_html=True)
