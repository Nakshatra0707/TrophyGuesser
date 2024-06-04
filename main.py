import streamlit as st
from ultralytics import YOLO
from PIL import Image

@st.cache_resource
def load_model ():
    mod = YOLO("best.pt")
    return mod

st.set_page_config(layout="wide")

st.markdown("""
            <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
            </head>
            """, unsafe_allow_html=True)

st.markdown('<div class="title-container"><div class="title">Trophy Guesser 🏆</div></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([":green[About 🤔]",":violet[Trophy Guesser 🏆]" , ":blue[Survey 📃]", ":red[Contact Me 📩📞]"])
with tab2:
    img = st.file_uploader("Upload a picture with a football trophy: ", accept_multiple_files=False, type=["jpg", "png", "jpeg"])
    if img is not None:
        img = Image.open(img)
        st.image(img)
        mod1 = load_model()
        res = mod1(img)
        ans = ""
        id = 0
        for r in res:
            id = r.probs.top1
            ans = r.names[id]
        guess = st.text_input(label="",placeholder="Write which trophy you think it is")
        z = 0
        x = 0
        if st.button("Enter"):
            if guess.lower() == ans.lower():
                st.write("Correct!")
                st.balloons()
            else: st.write(f"That's incorrect. The correct answer was: {ans}")

    st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.sportspromedia.com/wp-content/uploads/2023/09/San-Siro-1.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .title-container {
            background: rgba(0, 0, 100, 0.7);
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        .title {
            font-size: 2.5em;
            color: white;
        }
        .stTabs [role="tab"] {
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            margin: 0 5px;
            padding: 5px 10px;
            color: white;
            font-size: 1.2em;
        }
        .stTabs [role="tab"]:focus {
            outline: none;
            box-shadow: none;
        }
    </style>
    """, unsafe_allow_html=True)

with tab1:
    st.markdown("""
                <p id = "intro">My name is Nakshatra Dubey. My greatest passion since childhood has always been football. Playing football, watching football or even playing a football video game is extremely fun for me. I have won trophies in various football competition. Trust me, there is no better feeling than that. So, I decided to create an app which encapsulates winning a football trophy with a fun minigame. I trained Ultralytics' YOLO ML model to classify different football trophies and have the user guess which trophy can be seen in the photo they upload. Then I integrated it into streamlit which I used to create the interface and front end of the web app. I had an amazing time creating this web app and hope that you enjoy using it!</p>
                """, unsafe_allow_html=True)
    st.markdown('''
            <style>
            #intro {
                background: rgba(0, 100, 0, 0.7);
                border-radius: 10px;
                margin: 0 5px;
                padding: 5px 10px;
                color: white;
                font-family: "Comic Neue", cursive;
                font-weight: 400;
                font-style: normal;
            </style>
            </div>
            ''', unsafe_allow_html=True)
with tab3:
    st.markdown('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdLb4J9_xmt4y4AxkhCjO7t37gFP9my8ZvPjuWEWipOdY6euw/viewform?embedded=true" width="640" height="872" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)

with tab4:
    st.markdown("""
                <p id = 'email'>If you have anything you would like to tell me or if you want to have a conversation with me, feel free to send me an email!
                <br><br>
                <b>My Email Address: nakshatra.dubey@gmail.com</b></p>
                <style>
                    #email {
                        background: rgba(150, 0, 0, 0.7);
                        border-radius: 10px;
                        margin: 0 5px;
                        padding: 5px 10px;
                        color: white;
                        font-family: "Comic Neue", cursive;
                        font-weight: 400;
                        font-style: normal;
                </style>
                """, unsafe_allow_html=True)