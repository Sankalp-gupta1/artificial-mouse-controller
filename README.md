# Artificial Mouse Controller

A webcam-based hand / finger controller.

## Live browser demo

**https://artificial-mouse-sankalp.vercel.app/**

## Original Python version

`artificialmouse.py` uses OpenCV to detect a foreground contour and maps its position to the operating-system mouse cursor.

That version is still preserved in the repository for local desktop use.

## Deployed web version

The `web/` version uses MediaPipe Hands in the browser.

It:

- reads the webcam after permission,
- tracks the index fingertip,
- maps finger coordinates to a virtual desktop,
- moves a visible browser cursor,
- detects a thumb/index pinch,
- uses the pinch as a click on demo targets.

A normal website is not allowed to take over the real operating-system mouse cursor. The live version therefore demonstrates the interaction inside the page instead of pretending to control the OS.

Webcam frames stay in the browser.

## Run locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000`.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1
