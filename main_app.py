import streamlit as st
import game, front



if 'page' not in st.session_state:
    st.session_state['page'] = 'front'

if st.session_state['page'] == 'front':
    front.get_inp()
elif st.session_state['page'] == 'game':
    game.game()
