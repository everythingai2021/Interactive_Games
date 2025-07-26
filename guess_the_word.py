import streamlit as st
import random

# Word list
words = ["APPLE", "BANANA", "TIGER", "HOUSE", "HAPPY", "MAGIC"]

if 'secret_word' not in st.session_state:
    st.session_state.secret_word = random.choice(words)
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = []
if 'display_word' not in st.session_state:
    st.session_state.display_word = ["_" for _ in st.session_state.secret_word]

st.title("🔤 Guess the Word")

st.write("Guess the secret word!")


st.subheader(" ".join(st.session_state.display_word))


letter = st.text_input("Guess a letter:", max_chars=1).upper()

if st.button("Guess") and letter:
    if letter in st.session_state.guessed_letters:
        st.warning("You already guessed that letter!")
    else:
        st.session_state.guessed_letters.append(letter)
        
        if letter in st.session_state.secret_word:
            st.success(f"Good! '{letter}' is in the word!")
            
            for i, word_letter in enumerate(st.session_state.secret_word):
                if word_letter == letter:
                    st.session_state.display_word[i] = letter
        else:
            st.error(f"Sorry! '{letter}' is not in the word.")
        
        st.rerun()


if st.session_state.guessed_letters:
    st.write(f"Letters you guessed: {', '.join(st.session_state.guessed_letters)}")


if "_" not in st.session_state.display_word:
    st.balloons()
    st.success(f"🏆 You won! The word was {st.session_state.secret_word}")


if st.button("🔄 New Word"):
    st.session_state.secret_word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.display_word = ["_" for _ in st.session_state.secret_word]
    st.rerun()

