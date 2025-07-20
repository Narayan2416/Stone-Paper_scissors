import streamlit as st

# App layout
def get_inp():
    st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: deeppink;
    }
    .stApp {
        background-color: black;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: deeppink !important;
    }
    .stTextInput > div > div > input,
    .stNumberInput input {
        background-color: black;
        color: deeppink;
        border: 1px solid deeppink;
    }
    .stTextInput > label, .stNumberInput > label {
        color: deeppink !important;
    }
    .stButton button {
        background-color: black;
        color: deeppink;
        border: 1px solid deeppink;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
    }
    img {
        border: 2px solid deeppink;
    }
    .bottom-left {
        position: fixed;
        bottom: 20px;
        left: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True)

    # Centered subheader using HTML
    st.markdown(
        "<h2 style='text-align: center; color: deeppink;'>🎮 Welcome to the Game!!</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("gaming.gif")
        name = st.text_input("Enter your User Name")
        rounds = st.number_input("Enter total number of rounds to be played", min_value=5, step=1)

    # Submit button in bottom-left
    with st.container():
        st.markdown('<div class="bottom-left">', unsafe_allow_html=True)
        vali = st.button(label='Submit')
        st.markdown('</div>', unsafe_allow_html=True)

        if vali and name and rounds:
            st.session_state['name'] = name
            st.session_state['round'] = rounds
            st.session_state['page']='game'
        else:
            st.error("Fill the Columns")

