# Automated-Student-Attendance-System
Face recognition-based attendance system using Python, OpenCV, and face_recognition.
# 📚 Automated Student Attendance System

An AI-powered student attendance system that automatically marks attendance using **Python**, **OpenCV**, and the **face_recognition** library. The system detects and recognizes faces in real time through a webcam and stores attendance records in a CSV file.

---

## 🚀 Features

- 📸 Real-time face detection using OpenCV.
- 😀 Face recognition using the `face_recognition` library.
- 📝 Automatically marks attendance with date and timestamp.
- 📂 Stores attendance records in a CSV file.
- ⚡ Prevents duplicate attendance entries during the same session.
- 🖥️ Displays the recognized student's name on the live video feed.

---

## 🛠️ Tech Stack

- Python
- OpenCV
- face_recognition
- NumPy
- CSV

---

## 📂 Project Structure

```
Automated-Student-Attendance-System/
│── students/
│   ├── Virat.jpg
│   ├── Rahul.jpg
│   └── ...
│
│── Attendance.csv
│── attendance.py
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yajatjangra/Automated-Student-Attendance-System.git
```

Move to the project directory:

```bash
cd Automated-Student-Attendance-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python face_recognition numpy
```

---

## ▶️ Usage

Run the application:

```bash
python attendance.py
```

---

## 📸 How It Works

1. Store student images inside the `students/` folder.
2. The filename of each image should be the student's name (e.g., `Virat.jpg`).
3. Start the application.
4. The webcam captures live video.
5. Faces are detected and encoded.
6. If a match is found:
   - The student's name is displayed.
   - Attendance is recorded with the current timestamp.
7. Attendance is saved to `Attendance.csv`.

---

## 📋 Sample Attendance Record

| Name | Time |
|------|------|
| Virat | 09:15:24 |
| Rahul | 09:16:41 |

---

## 🔮 Future Improvements

- Database integration (MySQL/PostgreSQL)
- GUI using Tkinter or PyQt
- Web dashboard
- Cloud deployment
- Multi-camera support
- Email notifications

---

## 👨‍💻 Author

**Yajat Jangra**

GitHub: https://github.com/yajatjangra
