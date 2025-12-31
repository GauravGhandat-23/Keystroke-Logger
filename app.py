import streamlit as st
import logger
import time

st.set_page_config(
    page_title="Keystroke Logger",
    page_icon="⌨️",
    layout="centered"
)

st.title("⌨️ Keystroke Logger")
st.warning("⚠️ For educational and ethical use only")

# Session state
if "logging" not in st.session_state:
    st.session_state.logging = False

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start Logging"):
        logger.start_logging()
        st.session_state.logging = True
        st.success("Keystroke logging started")

with col2:
    if st.button("⏹ Stop Logging"):
        logger.stop_logging()
        st.session_state.logging = False
        st.info("Keystroke logging stopped")

with col3:
    if st.button("🧹 Clear Logs"):
        logger.logged_keys.clear()
        st.warning("Logs cleared")

st.divider()

# Status
if st.session_state.logging:
    st.info("⌨️ Logging active... Type anywhere on the system")
    time.sleep(0.3)

# Display logs
logs = logger.get_logs()

st.subheader("📄 Captured Keystrokes")
st.text_area(
    label="Logged Keys",
    value=logs,
    height=250
)

# Optional explanation (for examiner)
st.caption(
    "Note: This application captures OS-level keystrokes using pynput. "
    "Typing inside this browser does not represent real keylogging behavior."
)
