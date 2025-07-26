import streamlit as st
import random


if 'powers' not in st.session_state:
    st.session_state.powers = []
if 'hero' not in st.session_state:
    st.session_state.hero = {"name": "", "level": 1}

st.title("🦸‍♂️ Build Your Super Hero")

# Get hero name
if not st.session_state.hero["name"]:
    name = st.text_input("What's your hero name?")
    if st.button("Create Hero"):
        st.session_state.hero["name"] = name
        st.rerun()

if st.session_state.hero["name"]:
    st.write(f"Hero: {st.session_state.hero['name']}")
    st.write(f"Level: {st.session_state.hero['level']}")
    
    # Power choices
    all_powers = ["Flying", "Super Speed", "Invisible", "Fire Power", "Ice Power"]
    
    st.subheader("Choose a Power:")
    for power in all_powers:
        if st.button(power):
            if power not in st.session_state.powers:
                st.session_state.powers.append(power)  
                st.session_state.hero["level"] += 1    
                st.success(f"You got {power}!")
            st.rerun()
    
    # Show hero info
    st.subheader("Your Hero:")
    st.write(f"Name: {st.session_state.hero['name']}")
    st.write(f"Level: {st.session_state.hero['level']}")
    st.write(f"Powers: {st.session_state.powers}")
    
    if len(st.session_state.powers) >= 3:
        st.balloons()
        st.success("Amazing! You're a Super Hero!")

