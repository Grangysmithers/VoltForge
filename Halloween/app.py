import streamlit as st
from effects import witch_effect, monster_effect

# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------

st.set_page_config(
    page_title="HauntWave",
    page_icon="🎃",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CUSTOM HALLOWEEN DESIGN
# --------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(circle at 50% -20%, #35104d 0%, #16091f 35%, #08090d 75%);
    color: white;
}

/* Hide Streamlit header decoration */
[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    visibility: hidden;
}

/* Main page width */
.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* Main title */
.booth-title {
    text-align: center;
    font-size: 3.4rem;
    font-weight: 900;
    letter-spacing: 3px;
    margin-bottom: 0px;

    background: linear-gradient(90deg, #ff7a18, #ffb347, #b55cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    filter: drop-shadow(0px 0px 18px rgba(180, 70, 255, 0.35));
}

/* Subtitle */
.booth-subtitle {
    text-align: center;
    color: #c8b8d8;
    font-size: 1.1rem;
    letter-spacing: 2px;
    margin-top: 5px;
    margin-bottom: 35px;
}

/* Intro box */
.intro-box {
    text-align: center;
    padding: 18px;
    margin-bottom: 28px;

    border: 1px solid rgba(179, 92, 255, 0.30);
    border-radius: 16px;

    background: rgba(23, 13, 32, 0.65);

    box-shadow:
        0px 0px 30px rgba(116, 36, 170, 0.12);
}

.intro-main {
    font-size: 1.15rem;
    font-weight: 700;
    color: #ffffff;
}

.intro-small {
    color: #9d91aa;
    margin-top: 4px;
}

/* Section title */
.section-title {
    text-align: center;
    color: #ffb45c;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-top: 30px;
    margin-bottom: 12px;
}

/* Buttons */
.stButton > button {
    height: 75px;
    border-radius: 15px;
    border: 1px solid #733aa3;

    background:
        linear-gradient(
            135deg,
            rgba(74, 25, 102, 0.9),
            rgba(29, 14, 41, 0.95)
        );

    color: white;
    font-size: 1.05rem;
    font-weight: 800;
    letter-spacing: 1px;

    transition: 0.25s ease;

    box-shadow:
        0px 0px 18px rgba(136, 50, 200, 0.12);
}

.stButton > button:hover {
    border-color: #d173ff;

    background:
        linear-gradient(
            135deg,
            #702b99,
            #321044
        );

    color: white;

    transform: translateY(-2px);

    box-shadow:
        0px 0px 28px rgba(179, 73, 255, 0.32);
}

/* Audio recorder */
[data-testid="stAudioInput"] {
    padding: 15px;
    border-radius: 15px;

    background: rgba(17, 12, 24, 0.72);

    border: 1px solid rgba(160, 91, 205, 0.25);
}

/* Success message */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Divider */
hr {
    border-color: rgba(170, 100, 220, 0.20);
}

/* Result card */
.result-card {
    text-align: center;

    padding: 24px;
    margin-top: 15px;
    margin-bottom: 18px;

    border-radius: 18px;

    border: 1px solid rgba(255, 137, 50, 0.35);

    background:
        linear-gradient(
            135deg,
            rgba(52, 20, 65, 0.85),
            rgba(20, 12, 27, 0.9)
        );

    box-shadow:
        0px 0px 35px rgba(165, 61, 220, 0.15);
}

.result-title {
    color: #ffad52;
    font-size: 1.4rem;
    font-weight: 900;
    letter-spacing: 2px;
}

.result-text {
    color: #d8cce1;
    margin-top: 7px;
}

/* Footer */
.footer {
    text-align: center;
    color: #62576d;
    font-size: 0.75rem;
    letter-spacing: 2px;
    margin-top: 45px;
}

/* Cleaner transformation buttons */
.stButton > button {
    height: 82px;
    white-space: pre-line;
    line-height: 1.65;
}

/* Less unnecessary vertical space */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Halloween capture confirmation */
.capture-status {
    text-align: center;
    padding: 14px;
    margin-top: 12px;
    margin-bottom: 5px;

    border-radius: 12px;
    border: 1px solid rgba(177, 83, 255, 0.30);

    background: rgba(67, 24, 87, 0.35);

    color: #dca9ff;
    font-weight: 700;
    letter-spacing: 1px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="booth-title">🎃 HauntWave</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="booth-subtitle">ENTER IF YOU DARE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="intro-box"><div class="intro-main">Your voice won\'t leave the same way it entered.</div><div class="intro-small">Record your voice. Choose your curse. Hear what you\'ve become.</div></div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# RECORDER STATE
# --------------------------------------------------

if "recorder_key" not in st.session_state:
    st.session_state["recorder_key"] = 0

# --------------------------------------------------
# RECORD
# --------------------------------------------------

st.markdown(
    '<div class="section-title">STEP 01 · CAPTURE YOUR VOICE</div>',
    unsafe_allow_html=True
)

audio = st.audio_input(
    "🎙️ Press the microphone and speak...",
    key=f"recorder_{st.session_state['recorder_key']}"
)


# --------------------------------------------------
# PROCESS RECORDING
# --------------------------------------------------

if audio is not None:

    audio_bytes = audio.getvalue()

    with open("booth_recording.wav", "wb") as file:
        file.write(audio_bytes)

    st.markdown(
    '<div class="capture-status">✦ VOICE CAPTURED &nbsp;·&nbsp; THE BOOTH IS READY ✦</div>',
    unsafe_allow_html=True
)
    if st.button(
        "↻  RECORD ANOTHER VOICE",
        key="record_again_early",
        use_container_width=True
    ):
        st.session_state.pop("result", None)
        st.session_state.pop("voice", None)
        st.session_state.pop("icon", None)

        st.session_state["recorder_key"] += 1
        st.rerun()

    st.markdown(
        '<div class="section-title">STEP 02 · CHOOSE YOUR CURSE</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="medium")

    # ---------------- WITCH ----------------

    with col1:

        if st.button(
           "🧙  WITCH\nEerie · Twisted",
            use_container_width=True
        ):

            with st.spinner(
                "🕯️ Casting the witch's curse..."
            ):

                witch_effect(
                    "booth_recording.wav",
                    "booth_witch.wav"
                )

            st.session_state["result"] = "booth_witch.wav"
            st.session_state["voice"] = "WITCH"
            st.session_state["icon"] = "🧙"

    # ---------------- MONSTER ----------------

    with col2:

        if st.button(
            "👹  MONSTER\nDeep · Ferocious",
            use_container_width=True
        ):

            with st.spinner(
                "🔥 Awakening the monster..."
            ):

                monster_effect(
                    "booth_recording.wav",
                    "booth_monster.wav"
                )

            st.session_state["result"] = "booth_monster.wav"
            st.session_state["voice"] = "MONSTER"
            st.session_state["icon"] = "👹"


# --------------------------------------------------
# RESULT
# --------------------------------------------------

if "result" in st.session_state:

    st.markdown("---")

    voice = st.session_state["voice"]
    icon = st.session_state["icon"]

    st.markdown(
    f'<div class="result-card"><div style="font-size:3rem;">{icon}</div><div class="result-title">TRANSFORMATION COMPLETE</div><div class="result-text">Your human voice is gone.<br>You have become a <b>{voice}</b>.</div></div>',
    unsafe_allow_html=True
)

    st.audio(
        st.session_state["result"],
        format="audio/wav"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "↻  RECORD ANOTHER VOICE",
        use_container_width=True
    ):
        st.session_state.pop("result", None)
        st.session_state.pop("voice", None)
        st.session_state.pop("icon", None)

        # Reset the audio recorder
        st.session_state["recorder_key"] += 1

        st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">VOICE-DISGUISE VOCODER · HALLOWEEN EDITION</div>',
    unsafe_allow_html=True
)