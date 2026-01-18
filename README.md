## 📸 Face Recognition Based Attendance System
A real-time face recognition attendance system built using Python and Computer Vision that automatically identifies individuals and logs their attendance with date and time.
The system uses OpenCV for face detection, machine learning (KNN) for recognition, and a custom-designed UI for an intuitive experience.

## 👩‍💻 Author
### Ritika Jha<br>
#### Face Recognition & Computer Vision

## 🚀 Features

📷 Real-time face detection using Haar Cascade & OpenCV

🧠 Face recognition using KNN (scikit-learn)

🗂 Automatic attendance logging in CSV format with date & time

🎨 Custom modern UI template created using OpenCV

💾 Persistent face data storage using Pickle

🔊 Voice confirmation when attendance is marked

📊 Live attendance dashboard using Streamlit

## 🛠 Technologies Used

  * Python
  
  * OpenCV
  
  * NumPy
  
  * scikit-learn
  
  * Haar Cascade Classifier
  
  * Pickle
  
  * CSV
  
  * Streamlit

## 📂 Project Structure
    face-recognition-attendance-system/
    │
    ├── add_faces.py            # Capture and store face data
    ├── test.py                 # Face recognition & attendance marking
    ├── create_template.py      # Generates modern UI background
    ├── app.py                  # Streamlit attendance viewer
    │
    ├── data/
    │   ├── haarcascade_frontalface_default.xml
    │   ├── faces_data.pkl
    │   └── names.pkl
    │
    ├── Attendance/
    │   └── Attendance_DD-MM-YYYY.csv
    │
    ├── background.png
    └── README.md

## ⚙️ How the System Works
### 1️⃣ Register Faces

#### 📄 File: add_faces.py 

* User enters their name

* Camera captures 100 face samples

* Faces are resized, flattened, and stored

* Data is saved persistently in:

    * faces_data.pkl

    * names.pkl

### 2️⃣ Create UI Template

#### 📄 File: create_template.py 

* Generates a clean professional UI

* Includes:

    * Camera feed section

    * Instructions panel

    * Requirements panel

* Saves the UI as background.png

### 3️⃣ Recognize Faces & Mark Attendance

#### 📄 File: test.py 

* Loads stored face data

* Trains KNN classifier

* Detects and recognizes faces in real time

* Press O to mark attendance

### Attendance is saved as:<br>
     Attendance/Attendance_DD-MM-YYYY.csv

### 4️⃣ View Attendance Dashboard

#### 📄 File: app.py 

* Displays attendance records using Streamlit

* Auto-refreshes every few seconds

* Highlights important data visually

### 🔹Clone the Repository<br>
    git clone https://github.com/<your-username>/face-recognition-attendance-system.git
    cd face-recognition-attendance-system

### 🔹Install Dependencies
    pip install opencv-python numpy scikit-learn pandas streamlit pywin32

### 🔹Register Faces
    python add_faces.py

### 🔹Create UI Template
    python create_template.py

### 🔹Run Face Recognition & Attendance
    python test.py

### 🔹View Attendance Dashboard
    streamlit run app.py

## Attendance ScreenShot
<img width="1750" height="494" alt="Screenshot 2026-01-16 231106" src="https://github.com/user-attachments/assets/d498f0bf-ba70-4788-93cb-0b5505ab8680" />





