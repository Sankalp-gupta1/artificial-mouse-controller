# Artificial Mouse Controller

## Live browser demo

**https://artificial-mouse-controller.vercel.app/**

The desktop Python version can move the operating-system mouse pointer through PyAutoGUI. Browsers intentionally cannot take control of the real OS cursor, so the hosted version uses a **safe virtual cursor** inside the demo surface.

The web demo:

- uses the webcam
- tracks the index fingertip with MediaPipe
- maps fingertip coordinates to the virtual control surface
- detects a thumb-index pinch
- uses the pinch as a click gesture
- highlights the selected demo control

Processing happens in the browser.

---

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


## Run the web demo locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000` and allow camera access.
