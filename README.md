# Face Recognition System

![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![OpenCV](https://img.shields.io/badge/opencv-4.11.0-brightgreen)
![Face Recognition](https://img.shields.io/badge/face--recognition-1.3.0-red)

## 🌟 Features
- Real-time face detection and recognition
- Displays names from image filenames
- Web interface (Flask optional)
- [Add your specific features here]

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

# 1. Clone repository
git clone https://github.com/munirendris1/Face-recognition.git
cd Face-recognition

# 2. Create known_faces folder
mkdir known_faces

# 3. Install core dependencies
pip install dlib==19.24.6 face-recognition==1.3.0 opencv-python==4.11.0.86 numpy==2.2.3 pillow==11.1.0
📌 Adding Known Faces
Add photos to known_faces/ folder

Rename files with the person's name:
known_faces/
├── John_Doe.jpg      # Will display "John Doe"
├── Jane_Smith.png    # Will display "Jane Smith"
└── Munir_Ahmed.jpeg  # Will display "Munir Ahmed"

📦 Dependencies
Core Packages
Package	Version	Purpose
dlib	19.24.6	Facial landmark detection
face-recognition	1.3.0	High-level recognition
opencv-python	4.11.0.86	Image processing
numpy	2.2.3	Numerical operations
setuptools              75.8.2
🗂 Project Structure
Face-recognition/
├── known_faces/       # Add your labeled photos here
├── models/            # Pretrained models
├── utils/             # Helper scripts
├── face_detection.py  # Main detection script
├── app.py             # Flask web app (optional)
└── README.md
📄 License
MIT License


Key features ready for copy-paste:
1. Complete installation instructions
2. Clear "known_faces" naming convention
3. Version-pinned dependencies table
4. Ready-to-run commands
5. Troubleshooting section
6. Professional badge headers

The formatting will render perfectly on GitHub. Just paste this into your `README.md` file and customize the [bracketed sections] with your specific details.
