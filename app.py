import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Only For You 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD (OPTIONAL) ----------------
PASSWORD = "hello"   # change or delete this section if not needed

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center;'>🔒 Private Surprise 🔒</h1>", unsafe_allow_html=True)
    pwd = st.text_input("Enter the secret word 💕", type="password")
    if st.button("Unlock 💖"):
        if pwd == PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Wrong secret 💔")
    st.stop()

# ---------------- CSS (COLORS + MOTION) ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #2b0036, #ff4b8b);
    overflow-x: hidden;
}
.main {
    color: #fff;
    font-family: 'Trebuchet MS', sans-serif;
    animation: fadeIn 1.5s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
.stButton>button {
    background: linear-gradient(90deg, #ff0080, #ff8c00);
    color: white;
    border-radius: 35px;
    padding: 14px;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0px 0px 20px #ff99cc;
    transition: transform 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
}
.ticket {
    background: linear-gradient(135deg, #3a1c71, #d76d77, #ffaf7b);
    border: 4px dashed gold;
    border-radius: 25px;
    padding: 35px;
    text-align: center;
    box-shadow: 0px 0px 35px gold;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { box-shadow: 0px 0px 15px gold; }
    to { box-shadow: 0px 0px 40px gold; }
}
.heart {
    position: fixed;
    bottom: -10%;
    animation: float 6s linear infinite;
    font-size: 24px;
}
@keyframes float {
    0% { transform: translateY(0); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(-120vh); opacity: 0; }
}
img {
    border-radius: 20px;
    box-shadow: 0px 0px 20px #ffb3d9;
    animation: fadeIn 1.2s ease-in;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING HEARTS ----------------
for _ in range(8):
    st.markdown(
        f"<div class='heart' style='left:{random.randint(0,100)}%; animation-duration:{random.randint(5,9)}s;'>💖</div>",
        unsafe_allow_html=True
    )

# ---------------- STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown("<h1>Hey You 💕</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Tap gently… magic is waiting ✨</h3>", unsafe_allow_html=True)

    if st.button("💖 Start the Surprise 💖"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown("<h2>Let’s remove the worries 🌸</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.button("🗑 Stress")
        st.button("🗑 Overthinking")
    with col2:
        st.button("🗑 Distance")
        st.button("🗑 Bad Days")

    time.sleep(0.5)

    if st.button("✨ I’m Ready ✨"):
        st.session_state.step = 3
        st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.balloons()

    st.markdown("""
    <div class="ticket">
        <h1>🎟 GOLDEN LOVE TICKET 🎟</h1>
        <h3>Issued Only For You 💖</h3>
        <hr>
        <h2>Unlimited  Love</h2>
        <h2>Unlimited Smiles</h2>
        <p>Valid Forever ♾</p>   
    </div> 
    """, unsafe_allow_html=True)

    if st.button("📸 See Our Memories"):
        st.session_state.step = 4
        st.rerun()

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.markdown("<h2>Our Beautiful Moments 📸</h2>", unsafe_allow_html=True)

    st.image("images/memory1.jpg", caption="A moment I’ll always keep 💕")
    st.image("images/memory2.jpg", caption="My favorite smile 😍")
    st.image("images/memory3.jpg", caption="Always us 🤍")

    if st.button("💌 Read My Letter"):
        st.session_state.step = 5
        st.rerun()

# ---------------- STEP 5 ----------------
elif st.session_state.step == 5:
    st.markdown("<h1>For My Favorite Person 🧸</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Happy New Year 2026 🎆</h3>", unsafe_allow_html=True)

    with st.spinner("Loading feelings 💖"):
        time.sleep(1.5)

    st.success("""
This year, I wish you peace in your heart,  
light in difficult days,  
and smiles that never fade.

No matter where life takes us,  
you’ll always have my care,  
my respect, and my love.

This surprise is small,  
but my feelings are endless 💕
    """)

    if st.button("🔁 Watch Again"):
        st.session_state.step = 1
        st.rerun()
