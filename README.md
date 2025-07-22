## 📸 Screenshot

![Game UI](https://private-user-images.githubusercontent.com/186318414/469172831-b513846c-1632-4a6c-9cae-bedcf9e170bb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTMxODU4MjUsIm5iZiI6MTc1MzE4NTUyNSwicGF0aCI6Ii8xODYzMTg0MTQvNDY5MTcyODMxLWI1MTM4NDZjLTE2MzItNGE2Yy05Y2FlLWJlZGNmOWUxNzBiYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcyMlQxMTU4NDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MDQ0OTEyNGM1ZDNlY2E3YjYxNjM3YzM3MWIzNmYxMzM2Zjk3ODUxYjFmYjQwY2I0ZTQ3MDg0ZGRlZDg1MmJiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.vAt-erWC-UgWy2NCDnmRurOK7U9Pph5rMbBhFeV3V0U)

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


