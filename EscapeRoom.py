
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

h2, h3 {
    color: #D6B66F;
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


# PAGE NAVIGATION
if "page" not in st.session_state:
    st.session_state.page = "home"


# ==================================
# HOW TO PLAY SCREEN
# ==================================

if st.session_state.page == "instructions":

    st.markdown("<br>", unsafe_allow_html=True)

    st.title("HOW TO PLAY")

    st.markdown(
        "<p>Learn the rules before entering the classroom!</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("🎯 OBJECTIVE")
    st.write(
        "Escape the locked classroom by completing "
        "all 12 Differential Calculus challenges "
        "across four rooms."
    )

    st.markdown("---")

    st.subheader("🔑 GAME PROGRESSION")
    st.write("""
    1. Start in Room 1 and solve its three challenges.
    2. Complete all three challenges to earn a key.
    3. Use the key to unlock the next room.
    4. Complete all four rooms to escape.
    """)

    st.markdown("---")

    st.subheader("❤️ LIVES")
    st.write("""
    - You start with 3 lives.
    - Every incorrect answer costs 1 life.
    - Lose all 3 lives and the game ends.
    """)

    st.markdown("---")

    st.subheader("⏱️ TIMER")
    st.write("""
    - You have 10 minutes to escape.
    - Every incorrect answer deducts 5 seconds.
    - If the timer reaches zero, the game ends.
    """)

    st.markdown("---")

    st.subheader("💡 HINTS")
    st.write("""
    - You have 2 hints for the entire game.
    - Each hint reveals one step toward the solution.
    - Hints will not reveal the final answer.
    """)

    st.markdown("---")

    st.subheader("📌 IMPORTANT RULES")
    st.write("""
    - Complete challenges in the correct order.
    - Correct answers allow you to proceed.
    - Incorrect answers cost a life and 5 seconds.
    - You can retry a question after an incorrect answer.
    - Your lives, timer, and hints carry over between rooms.
    """)

    st.success(
        "YOUR MISSION: Solve all 12 challenges, "
        "collect all 3 keys, and escape before time runs out!"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("⬅ BACK TO MAIN MENU", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# ==================================
# STORY SCREEN
# ==================================

elif st.session_state.page == "story":

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.title("THE STORY")

    st.markdown("---")

    st.markdown("""
    You stayed late at school to finish your work.

    After spending hours solving problems, you finally
    decided it was time to go home.

    But when you reached the classroom door...

    **It was locked.**

    You tried opening it, but it wouldn't budge.
    You looked around and noticed something strange.

    The classroom was divided into four different areas.
    Each area contained puzzles, locked compartments,
    and mysterious challenges.

    A note on the teacher's desk caught your attention:

    *"To escape this classroom, you must prove your
    knowledge. Solve the challenges, collect the keys,
    and unlock the final exit."*

    You realized that the only way out was through
    Differential Calculus.

    The clock is ticking.

    **Can you solve all the challenges and escape
    before time runs out?**
    """)

    st.markdown("---")

    st.info(
        "Four rooms. Twelve challenges. One way out."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔒 START GAME", use_container_width=True):
        st.session_state.page = "room1"
        st.rerun()

    if st.button("⬅ BACK TO MAIN MENU", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# ==================================
# MAIN MENU SCREEN
# ==================================

elif st.session_state.page == "home":

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

    if st.button("▶ PLAY", use_container_width=True):
        st.session_state.page = "story"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("HOW TO PLAY", use_container_width=True):
        st.session_state.page = "instructions"
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        "<p style='color:#7D879B; font-size:12px;'>"
        "A DIFFERENTIAL CALCULUS ESCAPE GAME"
        "</p>",
        unsafe_allow_html=True
    )
