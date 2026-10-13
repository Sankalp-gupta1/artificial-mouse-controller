# Artificial Mouse Controller

A webcam-based hand/finger control project.

## Live demo

**https://artificial-mouse-sankalp.vercel.app/**

The live version uses MediaPipe Hands in the browser to control a **virtual cursor** inside the page.

## What the web demo does

- asks for webcam permission,
- detects one hand,
- tracks the index fingertip,
- maps the fingertip position to a virtual desktop,
- moves a visible cursor,
- detects a thumb-index pinch,
- uses the pinch as a click gesture.

Webcam frames stay in the browser.

## Why it uses a virtual cursor

Browsers are not allowed to take control of the operating-system mouse pointer.

So the deployed version demonstrates the interaction safely inside the web page.

The original Python version is still preserved for real desktop cursor control.

## Original Python version

File:

```text
artificialmouse.py
```

The original implementation uses:

- OpenCV
- contour-based foreground tracking
- camera-to-screen coordinate mapping
- PyAutoGUI-style desktop cursor movement

Run the desktop version in a local environment with webcam access.

## Run the web demo locally

```bash
cd web
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

Allow camera access.

## Tech stack

### Desktop
- Python
- OpenCV
- desktop mouse automation

### Web
- HTML
- CSS
- JavaScript
- MediaPipe Hands
- browser camera APIs
- Vercel

## Limitations

- the hosted version controls only the virtual cursor,
- tracking quality depends on lighting and camera quality,
- a browser cannot move the real OS cursor.

## Author

**Sankalp Gupta**

- GitHub: https://github.com/Sankalp-gupta1
- LinkedIn: https://www.linkedin.com/in/sankalp-gupta-rishi-8617302b0/
