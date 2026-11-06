
import streamlit as st
import time

# PAGE CONFIGURATION
st.set_page_config(
    page_title="The Locked Classroom",
    page_icon="🔒",
    layout="centered"
)

# DARK THEME DESIGN
st.markdown("""
<style>

.stApp {
    background-color: #10131C;
}

h1 {
    color: #D6B66F;
    text-align: center;
    font-size: 45px;
}

p {
    color: #E8EAF0;
    text-align: center;
    font-size: 17px;
}

.stButton > button {
    background-color: #B99A56;
    color: #171717;
    border-radius: 8px;
    border: none;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #D6B66F;
    color: black;
}

</style>
""", unsafe_allow_html=True)


# MAIN MENU
st.markdown("<br><br>", unsafe_allow_html=True)

st.title("THE LOCKED CLASSROOM")

st.markdown(
    "<p>Four rooms. Twelve challenges. One way out.</p>",
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.info(
    "Solve every Differential Calculus challenge "
    "and unlock the classroom exit before time runs out."
)

st.markdown("<br><br>", unsafe_allow_html=True)


# PLAY BUTTON
if st.button("▶ PLAY", use_container_width=True):
    st.session_state.page = "story"


st.markdown("<br>", unsafe_allow_html=True)


# HOW TO PLAY BUTTON
if st.button("HOW TO PLAY", use_container_width=True):
    st.session_state.page = "instructions"


# FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<p style='color:#7D879B; font-size:12px;'>"
    "A DIFFERENTIAL CALCULUS ESCAPE GAME"
    "</p>",
    unsafe_allow_html=True
)

