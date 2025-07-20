import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
import tensorflow as tf
import random




@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model.h5')

def evaluate(a,b):
    if a=='Paper':
        if b=='Rock':
            st.session_state['score'][st.session_state['name']]+=1
        elif b=='Scissors':
            st.session_state['score']['Bot']+=1
    if a=='Rock':
        if b=='Scissors':
            st.session_state['score'][st.session_state['name']]+=1
        elif b=='Paper':
            st.session_state['score']['Bot']+=1
    if a=='Scissors':
        if b=='Paper':
            st.session_state['score'][st.session_state['name']]+=1
        elif b=='Rock':
            st.session_state['score']['Bot']+=1


    # Labels (ensure same order as training)
class_names = ["Rock", "Paper", "Scissors"]

def bot():
    return random.choice(class_names)

def crop_hand(image):
    hand=mp.solutions.hands
    hands=hand.Hands(static_image_mode=True,max_num_hands=1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = image.shape
            x_coords = [lm.x for lm in hand_landmarks.landmark]
            y_coords = [lm.y for lm in hand_landmarks.landmark]
            x_min = max(int(min(x_coords) * w) - 20, 0)
            y_min = max(int(min(y_coords) * h) - 20, 0)
            x_max = min(int(max(x_coords) * w) + 20, w)
            y_max = min(int(max(y_coords) * h) + 20, h)
            hand_crop = image[y_min:y_max, x_min:x_max]
            return hand_crop
    hands.close()
    return None

def game():
    model = load_model()
    if 'score' not in st.session_state:
        st.session_state['score']={st.session_state['name']:0,'Bot':0}

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
            .stcamera_input {
                background-color: black;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to the (Rock/Paper/Scissors)\nGame!!")
    col1, col2, col3 = st.columns([11, 15, 11])
    
    if st.session_state.get('round', 1) == 0:
        with col2:
            st.image("game_over.gif")

            player_name = st.session_state.get('name', 'Player')
            scores = st.session_state.get('score', {player_name: 0, 'Bot': 0})
            
            player_score = scores.get(player_name, 0)
            bot_score = scores.get('Bot', 0)

            if player_score > bot_score:
                st.success("You Won!!")
            elif player_score < bot_score:
                st.success("You Lost!!")
            else:
                st.success("Draw!!")

    else:
        with col1:
            uploaded_file = st.camera_input(f"{st.session_state['name']}")

            if uploaded_file:
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)  # BGR

                hand = crop_hand(image)
                if hand is not None:
                    hand_rgb = cv2.cvtColor(hand, cv2.COLOR_BGR2RGB)
                    resized = cv2.resize(hand_rgb, (224, 224))
                    normalized = resized.astype('float32') / 255.0
                    input_img = np.expand_dims(normalized, axis=0)

                    # Inference
                    prediction = model.predict(input_img, verbose=0)[0]
                    class_idx = np.argmax(prediction)
                    confidence = prediction[class_idx]

                    st.success(f"User: {class_names[class_idx]}")
                else:
                    st.warning("⚠️ No hand detected in the image. Please try again.")
            else:
                st.info("📤 Please capture an image to classify.")

        with col3:
            st.image("bot.gif")
            if uploaded_file and hand is not None:
                bot_move = bot()
                st.success(f"Bot: {bot_move}")
                evaluate(class_names[class_idx], bot_move)
                st.session_state['round'] -= 1
            else:
                st.success("---")

    st.dataframe(st.session_state['score'])

    if st.button(label='Home'):
        st.session_state['page'] = 'front'
    if st.session_state['round']==0:
        st.stop()
