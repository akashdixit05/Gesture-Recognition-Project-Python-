# 🖐️ Index Finger Swipe Gesture Controls

This project allows you to control your computer using **index finger swipe gestures** detected via webcam.  
It uses **MediaPipe** for hand tracking, **OpenCV** for video processing, and **PyAutoGUI** to simulate keyboard arrow key presses.  

👉 Note: Left/Right gestures are intentionally inverted (`left` swipe triggers the **Right Arrow Key**, `right` swipe triggers the **Left Arrow Key**).

---

## ✨ Features
- Detects **hand landmarks** using MediaPipe.
- Tracks the **index fingertip** to detect swipe gestures.
- Maps gestures to keyboard arrow keys:
  - 👈 Swipe Left → `←`
  - 👉 Swipe Right → `→`
  - 👆 Swipe Up → `↑`
  - 👇 Swipe Down → `↓`
- Includes **cooldown mechanism** to avoid repeated accidental triggers.
- Displays a live webcam feed with gesture visualization.

---

## ⚙️ Installation & Setup

### 1. Clone this repository
    ```bash
    git clone https://github.com/akashdixit05/Gesture-Recognition-Project-Python.git
    cd index-finger-swipe-controls
    

### 2. Install Dependencies -required libraries
    pip install opencv-python mediapipe

### 3. Run the Program 
    python gesture_recognition.py

### 4. Controls
    The webcam will open and detect hand gestures.

    Supported gestures include:

    ✊ Rock
    ✌️ Scissors
    ☝️ One Finger
    👍 Thumbs Up
    ✋ Open Palm
    🤘 Rock n Roll
    👌 OK
    🤙 Call Me

    Detected gesture name will appear on screen.

    Press q to exit.
