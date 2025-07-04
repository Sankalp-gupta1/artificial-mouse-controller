# 🖱️ Artificial Mouse Controller using Hand Gestures

A computer vision-based project that allows you to **control your mouse cursor with your hand gestures** in real-time using your webcam.  
This project is built using **OpenCV**, **MediaPipe**, and **PyAutoGUI**, enabling **gesture recognition** and **system-level cursor control**.

---

## 📖 What is this project?

In this project, your **index finger acts as a mouse pointer** and a **pinch gesture (thumb touching index finger)** simulates a mouse click.

It uses a webcam feed to track hand landmarks (like fingertips and joints), calculates distance between thumb and index finger, and maps your finger position to screen coordinates to move the mouse pointer.

---

## 🚀 Features

- ✅ Real-time **hand tracking** using webcam
- ✅ **Index finger controls** mouse cursor
- ✅ **Click action** triggered by pinch gesture
- ✅ Smooth & natural movement with landmark filtering
- ✅ Cross-platform (Windows tested, others with slight mods)
- ✅ No additional hardware required — just your **webcam**

---

## 🧠 How it works

1. **Webcam** captures your video.
2. **MediaPipe** detects your hand and identifies landmarks.
3. **Index finger's coordinates** are mapped to your screen.
4. If **thumb and index finger tips** come close (pinch), it registers a **mouse click**.
5. **PyAutoGUI** sends the mouse movement and click signals to your OS.

---

## 🧪 Technologies Used

| Technology | Purpose |
|------------|---------|
| `OpenCV`   | Webcam video stream and image processing |
| `MediaPipe` | Real-time hand tracking & landmark detection |
| `PyAutoGUI` | Simulate mouse movement and click events |
| `ctypes` / `comtypes` | System-level audio control (if extended for volume, optional) |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Sankalp-gupta1/artificial-mouse-controller.git

# Move into the directory
cd artificial-mouse-controller

# Install dependencies
pip install -r requirements.txt

