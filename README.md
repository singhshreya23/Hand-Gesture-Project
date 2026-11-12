# Hand Gesture Detection with Arduino Serial Output

Real-time hand detection from a webcam using MediaPipe and OpenCV. The script tells an Arduino Uno over serial whether a hand is in view. It is part of an AI-based gesture mimicking robotic hand, built during a research internship at MANIT Bhopal (June 2026).

## What it does

- Captures live video from the default webcam with OpenCV.
- Detects one hand at a time (minimum detection confidence 0.7) and draws its 21 landmarks and connections with MediaPipe Hands.
- Shows **Hand Detected!** or **No Hand** on the video window.
- Sends `1` (hand detected) or `0` (no hand) to the Arduino over a 9600-baud serial connection.
- Still runs if no Arduino is connected, with the serial output switched off.
- Press **Esc** to quit.

## How it works

```
Webcam -> OpenCV frame -> MediaPipe Hands (21 landmarks) -> detected? -> PySerial -> Arduino Uno
```

## Requirements

- Python 3
- A webcam
- An Arduino Uno connected by USB (optional, for the serial output)

Install the libraries:

```bash
pip install opencv-python mediapipe pyserial
```

## Usage

1. Connect the Arduino and find its serial port (for example `COM4` on Windows).
2. If your port is not `COM4`, change it in `gesture.py`:
   ```python
   arduino = serial.Serial('COM4', 9600, timeout=1)
   ```
3. Run the script:
   ```bash
   python gesture.py
   ```
4. Hold your hand in front of the webcam. Press **Esc** to exit.

## Arduino side

The Arduino receives one byte per frame: `1` when a hand is detected and `0` when it is not. The Arduino sketch that reads this signal is not included in this repository yet.

## Project structure

```
.
├── gesture.py   # webcam hand detection + serial output
└── README.md
```

## Limitations

- Detects the presence of a hand only; it does not yet measure individual finger positions.
- Tracks a single hand.
- The serial port is hardcoded to `COM4`.
- Detection quality drops in poor lighting or with a cluttered background.

## Next steps

- Compute a bend angle for each finger from the landmarks and send them to the Arduino.
- Map the angles to servo positions to mimic the hand's movement.
- Smooth the readings to reduce servo jitter.
- Support two hands and a wireless link.

## Built with

Python, OpenCV, MediaPipe, PySerial, Arduino Uno

## Author

Shreya Singh | [LinkedIn](https://www.linkedin.com/in/shreya-singh-87912537b)# Hand-Gesture-Project
