import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Only For You 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD PROTECTION ----------------
PASSWORD = "cutiepie"   # change this secret

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center;'>🔒 Only For You 🔒</h1>", unsafe_allow_html=True)
    pwd = st.text_input("Enter the secret word 💕", type="password")
    if st.button("Unlock 💖"):
        if pwd == PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Wrong secret 💔")
    st.stop()

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #2b0036, #ff4b8b, #6a1b9a, #ffd700);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.main {
    color: white;
    font-family: 'Trebuchet MS', sans-serif;
    animation: fadeIn 1.2s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 0 25px rgba(255,255,255,0.2);
    margin-bottom: 25px;
}
.stButton>button {
    background: linear-gradient(90deg, #ff4b8b, #ffd700);
    color: white;
    border-radius: 30px;
    padding: 14px;
    font-size: 17px;
    font-weight: bold;
    box-shadow: 0 0 15px rgba(255,215,0,0.6);
    transition: transform 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
}
.heart {
    position: fixed;
    bottom: -10%;
    font-size: 22px;
    opacity: 0.6;
    animation: float 9s linear infinite;
}
@keyframes float {
    0% {transform: translateY(0); opacity: 0;}
    50% {opacity: 1;}
    100% {transform: translateY(-120vh); opacity: 0;}
}
img {
    border-radius: 18px;
    box-shadow: 0 0 20px rgba(255,255,255,0.4);
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
for _ in range(8):
    st.markdown(
        f"<div class='heart' style='left:{random.randint(0,100)}%; animation-duration:{random.randint(7,11)}s;'>💖</div>",
        unsafe_allow_html=True
    )

# ---------------- STEP STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown("""
    <div class="card">
        <h1>Hey You 💕</h1>
        <h3>Tap gently… this page was made only for you ✨</h3>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💖 Begin"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown("""
    <div class="card">
        <h2>Let’s leave the worries behind 🌸</h2>
        <p>Just for this moment… nothing else matters.</p>
    </div>
    """, unsafe_allow_html=True)

    st.button("🗑 Stress")
    st.button("🗑 Overthinking")
    st.button("🗑 Bad Days")

    if st.button("✨ Continue"):
        st.session_state.step = 3
        st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.balloons()
    st.markdown("""
    <div class="card">
        <h1>🎟 Golden Love Ticket 🎟</h1>
        <h3>Issued only for you</h3>
        <hr>
        <h2>Unlimited Love</h2>
        <h2>Unlimited Smiles</h2>
        <p>Valid forever ♾</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📸 Memories"):
        st.session_state.step = 4
        st.rerun()

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.markdown("""
    <div class="card">
        <h2>Moments I treasure 📸</h2>
    </div>
    """, unsafe_allow_html=True)

    st.image("images/memory1.jpg", caption="A moment I still smile about 💕")
    st.image("images/memory2.jpg", caption="Where time felt slower 🤍")
    st.image("images/memory3.jpg", caption="One of my favorite memories ✨")


    if st.button("💌 Read My Letter"):
        st.session_state.step = 5
        st.rerun()

# ---------------- STEP 5 (LETTER) ----------------
elif st.session_state.step == 5:
    st.markdown("""
    <div class="card">
        <h1>For You 🤍</h1>

        <p>
            This page was not made to impress you,<br>
            it was made to remind you.
        </p>

        <p>
            Remind you that you matter,<br>
            that your presence makes things lighter,<br>
            and that your smile means more than you realize.
        </p>

        <p>
            I hope this year gives you calm mornings,<br>
            peaceful nights,<br>
            and moments where you feel truly understood.
        </p>

        <p>
            No matter what changes around us,<br>
            I hope you always feel valued,<br>
            supported,<br>
            and deeply cared for.
        </p>

        <p>
            This surprise is small,<br>
            but the thought behind it is endless 💖
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 Start Again"):
        st.session_state.step = 1
        st.rerun()

