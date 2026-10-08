# Artificial Mouse Controller

A webcam-based computer vision prototype that maps the detected position of a finger-like foreground contour to the system mouse cursor.

## Overview

The project captures frames from the webcam, isolates a foreground contour using grayscale conversion, Gaussian blur, Otsu thresholding, and morphological filtering, then maps the contour centroid from camera coordinates to screen coordinates.

The current implementation focuses on **cursor movement**.

## Features

- Real-time webcam capture
- Grayscale preprocessing
- Gaussian blur for noise reduction
- Otsu thresholding
- Morphological opening
- Largest-contour detection
- Contour centroid calculation
- Camera-to-screen coordinate mapping
- Mouse movement through PyAutoGUI

## How It Works

```text
Webcam frame
    │
    ▼
Grayscale conversion
    │
    ▼
Gaussian blur
    │
    ▼
Otsu thresholding
    │
    ▼
Morphological cleanup
    │
    ▼
Largest valid contour
    │
    ▼
Contour centroid
    │
    ▼
Map to screen coordinates
    │
    ▼
PyAutoGUI cursor movement
```

## Tech Stack

- Python
- OpenCV
- NumPy
- PyAutoGUI

## Installation

Clone the repository:

```bash
git clone https://github.com/Sankalp-gupta1/artificial-mouse-controller.git
cd artificial-mouse-controller
```

Install dependencies:

```bash
pip install opencv-python numpy pyautogui
```

## Run

```bash
python artificialmouse.py
```

Press `q` in the OpenCV window to exit.

## Notes

This implementation uses contour-based tracking rather than a dedicated hand-landmark model. Results can therefore depend heavily on lighting, background contrast, camera quality, and how clearly the target finger/hand is separated from the background.

The current source moves the mouse pointer; click gestures are not implemented in this version.

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
