📌 Face Detection System using OpenCV
🔹 Project Description
This project implements a real-time Face Detection System using OpenCV in Python.
The system captures live video from a webcam and detects human faces using the Haar Cascade Classifier.
🔹 Technologies Used
Python 3.11
OpenCV
Haar Cascade Classifier
VS Code
🔹 How It Works
The system uses a pre-trained Haar Cascade XML classifier provided by OpenCV.
The webcam captures live video frames.
Each frame is converted into grayscale.
The Haar Cascade classifier scans the image.
When facial features are detected, a bounding box is drawn around the face.
The system works in real-time.
🔹 Features
Real-time face detection
Multiple face detection support
Lightweight and fast execution
No external deep learning model required
🔹 How to Run the Project
Install OpenCV:
Copy code

pip install opencv-python
Run the program:
Copy code

python face_detect.py
Press ESC to exit.
🔹 Applications
Attendance monitoring systems
Security systems
Surveillance applications
Face-based access control systems
🔹 Future Enhancement
Add face recognition (identify person name)
Integrate with attendance database
Implement deep learning-based detection# dishap81-facedetect
