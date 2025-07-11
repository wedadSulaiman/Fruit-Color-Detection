# Fruit Color Detection

This project performs **color-based fruit detection** in a video using Python and OpenCV.  
It is designed to identify the following fruits based on their dominant colors:

- Red Apple  
- Orange  
- Lemon  

The video used must have a black background to minimize noise and improve detection accuracy.

---

## Project Overview

The script processes each video frame using the HSV (Hue, Saturation, Value) color space and matches the color of the fruit to pre-defined HSV color ranges.  
It displays the detected fruit name on the video in real-time.

---

## Technologies Used

- Python 3.10 using vs-code on Anaconda IDE 
- OpenCV  
- NumPy  

---

## Supported Colors

| Fruit       | HSV Hue Range                |
|-------------|------------------------------|
| Red Apple   | H: 0–10 and 160–179          |
| Orange      | H: 10–25                     |
| Lemon       | H: 25–35                     |

---



## Output Video

A recorded video demonstrating the fruit color detection will be added after running the script.


https://github.com/user-attachments/assets/502fc536-953d-4f0c-b7fb-993a2f1a01e6



