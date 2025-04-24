
import streamlit as st
import datetime
import random

st.set_page_config(page_title="Pocket Option Signal Bot", layout="centered")
st.title("Pocket Option Signal Bot")

# Settings
pairs = ["AED/CNY", "AUD/CHF"]
strategy_name = "AI Trend Reversal"

# Signal generator (placeholder logic)
def generate_signal(pair):
    direction = random.choice(["Buy", "Sell"])
    strength = random.randint(60, 100)
    return f"{datetime.datetime.now().strftime('%H:%M:%S')} — {pair}: {direction} Signal ({strength}%)"

# Display signals
st.header("Live Signals")
for pair in pairs:
    st.write(generate_signal(pair))

st.caption("Strategy: AI Trend Reversal")
