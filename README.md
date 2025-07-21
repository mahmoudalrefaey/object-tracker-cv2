# Real-Time Object Tracking – Practical Assessment

This repository contains a Python script (`traking_system.py`) developed as part of a technical assessment. The script demonstrates real-time object tracking using a webcam and OpenCV.

The main idea is simple: open the webcam, manually select an object in the first frame, and let the script handle tracking that object live as it moves.

## What It Does

- Opens a live webcam feed
- Select an object to track by drawing a rectangle
- Tracks the selected object in real time using OpenCV’s CSRT tracker
- Provides visual feedback of the tracking process
- Allows exit at any time by pressing the ESC key

## How to Set It Up

1. Clone or download this repository.
2. Install the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run It

in your terminal or command prompt, simply run:

```bash
python tracker.py
```

Here’s what to expect:

1. The webcam feed will open.
2. You’ll be asked to select the object to track by drawing a box with your mouse.
3. The script will begin tracking the object and display the live tracking updates.
4. Press the ESC key at any time to exit the program.

## About the Tracker

The script uses OpenCV’s CSRT tracking algorithm.
## Demo

A sample demo video (`demo.mp4`), [click here]() to perview the tracking in action.

## Notes

- Ensure your webcam is connected and not being used by another application.
- If you encounter an error opening the camera, check device permissions or try restarting the script.
- This script was implemented as part of a practical task to demonstrate real-time tracking, not as a production-ready tool.
