import streamlit as st
from ultralytics import YOLO
from PIL import Image

@st.cache_resource
def load_model ():
    mod = YOLO("best.pt")
    return mod

st.set_page_config(layout="wide")

st.title("Trophy Guesser")

tab1, tab2, tab3, tab4 = st.tabs(["Trophy Guesser 🏆", "About 🤔", "Survey 📃", "Contact Me 📩📞"])
with tab1:
    img = st.file_uploader("Upload a picture with a football trophy: ", accept_multiple_files=False, type=["jpg", "png", "jpeg"])
    if img is not None:
        img = Image.open(img)
        st.image(img)
        mod1 = load_model()
        res = mod1.predict(img)
        pred = res[0].probs.top5
        st.write(res[0].names[0])
    st.markdown("""
                <style>
                    .stApp {
                        background-image: url("https://www.sportspromedia.com/wp-content/uploads/2023/09/San-Siro-1.jpg");
                        background-size: cover;
                        }
                </style>""", unsafe_allow_html=True)
with tab2:
    st.title("this is the second page")
    st.markdown("""
                <i><u><b><p style = "color: cyan">Have some balloons! 🎈</p></i></u></b>
                """, unsafe_allow_html=True)
    if st.button("BALLOONS"): 
        st.balloons()
with tab3:
    st.markdown("""
                <style>
                    body {
                        background-image: url("data:image/png;base64,%s");
                        background-size: cover;
                        }
                </style>""", unsafe_allow_html=True)
    st.title("this is the third page")
    inp = st.text_input("Enter your name")
    button = st.button("Click", on_click=st.write(inp))