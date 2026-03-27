# BCA Attendance Management System

A comprehensive, role-based Online Attendance Management System built specifically for the BCA department. It allows seamless tracking, visualization, and reporting of student attendance, utilizing a robust Python Flask backend and a modern UI.

---

## 🚀 Key Features

### Admin Portal
- **Dashboard Analytics:** Real-time metrics with Chart.js including daily Doughnut charts and 7-day Weekly Bar charts tracking Present, Absent, OD, and Leave statuses.
- **User Management:** Create, edit, and deactivate accounts for Teachers and Students.
- **Academic Setup:** Define Class Timetables, Subjects, and Batches dynamically.
- **Advanced Reporting:** Query attendance by Student, Subject, or custom **Date-Range**.
- **1-Click Export:** Export detailed official reports to **Excel** (color-coded) and **PDF** directly from the admin dashboard.

### Teacher Portal
- **Live Class Detection:** Auto-detects the active period and subject based on the configured timetable and system clock.
- **Quick Attendance Marking:** 4-state selection per student — **Present (P)**, **Absent (A)**, **On Duty (OD)**, or **Leave (L)**.
- **Color-Coded Feedback:** Interactive highlight rows verifying marked status before submission.
- **Submission History:** View recent class assignments and submission logs.

### Student Portal
- **Personalized Dashboard:** Track overall attendance against the requisite 75% threshold.
- **Low-Attendance Smart Warnings:** Proactively alerts the student if they drop below 75% in any subject, citing the *exact* number of consecutive classes needed to recover their standing.
- **Subject-Wise Breakdown:** See exactly how many times you were P, A, OD, or L per subject.
- **Official PDF Export:** Students can independently download their own personalized, stylised PDF attendance reports at any time.

---

## 📂 Project Structure

```text
AttendanceProject/
│
├── app.py                   # Main Flask Application & Route Definitions
├── init_db.py               # Safe Database Initialization (CREATE IF NOT EXISTS)
├── migrate_db.py            # SQLite Schema updates & Check Constraint Migrations
├── walkthrough.md           # Detailed technical overview of latest features
│
├── data/
│   └── attendance.db        # SQLite Database (Auto-generated on run)
│
├── static/
│   └── (CSS/JS assets if extracted from templates)
│
└── templates/               # Jinja2 HTML Templates
    ├── base.html            # Global layout, Sidebar Navigation, Flash styling
    ├── login.html           # Universal login portal
    ├── admin_dashboard.html # Admin analytics & Chart.js integration
    ├── manage_students.html # Admin CRUD interfaces...
    ├── manage_teachers.html 
    ├── manage_subjects.html 
    ├── manage_timetable.html
    ├── reports.html         # Date-range queries and Summary Tables
    ├── teacher_dashboard.html # Attendance marking form
    └── student_dashboard.html # Subject-wise tracking and Warnings
```

---

## 🛠️ Tech Stack
- **Backend:** Python 3, Flask, SQLite3
- **Frontend:** HTML5, CSS3 (Custom Variables & Flexbox/Grid), JavaScript, Jinja2
- **Data Visualization:** Chart.js
- **Export Libraries:** 
  - `openpyxl` (Excel generation with conditional formatting)
  - `reportlab` (PDF generation with custom tables)

---

## 💻 Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/bca-attendance-system.git
   cd bca-attendance-system
   ```

2. **Install Dependencies**
   Ensure Python 3 is installed, then run:
   ```bash
   pip install flask werkzeug openpyxl reportlab
   ```

3. **Initialize the Database**
   Creates the `data/attendance.db` file and populates the default `ADMIN` account without overwriting existing data.
   ```bash
   python init_db.py
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```
   *The server will start at `http://127.0.0.1:5000`*

**Default Credentials:**
- **Role:** Admin
- **Username:** `ADMIN`
- **Password:** `Admin12345`

---

## 💡 Future Ideas & Roadmap
- **Facial Recognition Integration:** Automate the teacher's roll call using webcam captures powered by OpenCV/face_recognition.
- **Parental Portal/SMS Alerts:** Integrate Twilio or an SMS gateway to automatically text parents when a student has missed 3 consecutive days.
- **QR Code Check-ins:** Generate dynamic QR codes securely on the Teacher's screen that students scan via their mobile phones.
- **Pagination & Caching:** Implement DataTables or backend pagination for handling 10,000+ attendance records seamlessly.
- **CSRF Tokens:** Upgrade `app.py` forms with `Flask-WTF` to prevent Cross-Site Request Forgery.
