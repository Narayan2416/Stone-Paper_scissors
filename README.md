## 📸 Screenshot

![UI Screenshot](assets/screenshot.png)

---

# 🕹️ Real-Time Hand Gesture Classification using MobileNetV2 and MediaPipe

This project showcases a real-time hand gesture recognition system built using **transfer learning** and **computer vision** techniques, integrated within an interactive **Streamlit** web application.

---

## 🚀 Overview

- Implemented a gesture classification system using a **pre-trained MobileNetV2** model.
- Utilized **transfer learning** by freezing the convolutional base and training a new classifier head on a custom dataset containing three hand gesture classes.
- Employed **MediaPipe** to detect and crop the hand region from real-time webcam input.
- Processed the cropped hand images and classified them using the trained MobileNetV2-based model.
- Developed a **Streamlit-based game interface** that allows the user to:
  - Enter their name
  - Choose number of rounds
  - Play the game by showing gestures
  - View real-time predictions and score updates in a stylized UI.

---

## 🛠️ Technologies Used

- **TensorFlow / Keras** – Model development and training
- **MediaPipe** – Real-time hand detection and landmark extraction
- **OpenCV** – Frame capture and processing
- **Streamlit** – User interface development
- **Python** – Implementation and logic


