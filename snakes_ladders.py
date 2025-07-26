

import streamlit as st
import random

# Tuples for snakes and ladders 
snakes = ((16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78))
ladders = ((1, 38), (4, 14), (9, 21), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100))

if 'player_pos' not in st.session_state:
    st.session_state.player_pos = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("🐍 Snake and Ladders")

def check_snakes_ladders(position):
    # Check snakes
    for snake_start, snake_end in snakes:
        if position == snake_start:
            return snake_end, "snake"
    
    # Check ladders
    for ladder_start, ladder_end in ladders:
        if position == ladder_start:
            return ladder_end, "ladder"
    
    return position, "normal"

st.write(f"Your position: {st.session_state.player_pos}")

if not st.session_state.game_over:
    if st.button("🎲 Roll Dice"):
        dice = random.randint(1, 6)
        st.write(f"You rolled: {dice}")
        
        # Move player
        new_pos = st.session_state.player_pos + dice
        
        if new_pos <= 100:
            st.session_state.player_pos = new_pos
            
            # Check for snakes or ladders
            final_pos, type_found = check_snakes_ladders(new_pos)
            
            if type_found == "snake":
                st.session_state.player_pos = final_pos
                st.error(f"🐍 Snake! You slide down to {final_pos}")
            elif type_found == "ladder":
                st.session_state.player_pos = final_pos
                st.success(f"🪜 Ladder! You climb up to {final_pos}")
            
            # Check win
            if st.session_state.player_pos >= 100:
                st.session_state.game_over = True
                st.balloons()
                st.success("🏆 You Win!")
        else:
            st.write("Too high! Try again.")

if st.button("🔄 New Game"):
    st.session_state.player_pos = 0
    st.session_state.game_over = False
    st.rerun()
