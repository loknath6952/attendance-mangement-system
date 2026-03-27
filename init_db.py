import sqlite3, os
from werkzeug.security import generate_password_hash

def setup():
    if not os.path.exists('data'):
        os.makedirs('data')
    conn = sqlite3.connect('data/attendance.db')
    c = conn.cursor()

    c.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            username TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL,
            role     TEXT    NOT NULL CHECK(role IN ('admin','teacher','student')),
            status   TEXT    NOT NULL DEFAULT 'active' CHECK(status IN ('active','inactive'))
        );

        CREATE TABLE IF NOT EXISTS students (
            reg_no   TEXT PRIMARY KEY,
            name     TEXT NOT NULL,
            year     INTEGER NOT NULL,
            semester INTEGER NOT NULL DEFAULT 1,
            section  TEXT NOT NULL,
            shift    TEXT NOT NULL CHECK(shift IN ('FN','AF')),
            contact  TEXT,
            email    TEXT
        );

        CREATE TABLE IF NOT EXISTS subjects (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT    NOT NULL,
            year     INTEGER NOT NULL,
            semester INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS timetable (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            day        TEXT    NOT NULL,
            period     INTEGER NOT NULL,
            shift      TEXT    NOT NULL,
            year       INTEGER NOT NULL,
            section    TEXT    NOT NULL,
            teacher_id INTEGER NOT NULL REFERENCES users(id),
            subject_id INTEGER NOT NULL REFERENCES subjects(id)
        );

        CREATE TABLE IF NOT EXISTS attendance (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT    NOT NULL REFERENCES students(reg_no),
            subject_id INTEGER NOT NULL REFERENCES subjects(id),
            teacher_id INTEGER NOT NULL REFERENCES users(id),
            date       TEXT    NOT NULL,
            period     INTEGER NOT NULL,
            status     TEXT    NOT NULL CHECK(status IN ('P','A','OD','L'))
        );
    ''')

    # ── Admin check ───────────────────────────────────────────────────────
    admin_exists = c.execute("SELECT 1 FROM users WHERE username='ADMIN'").fetchone()
    if not admin_exists:
        c.execute(
            "INSERT INTO users (name,username,password,role,status) VALUES (?,?,?,'admin','active')",
            ('System Admin', 'ADMIN', generate_password_hash('Admin12345'))
        )

    # ── BCA Subjects check ────────────────────────────────────────────────
    subjects_count = c.execute("SELECT COUNT(*) FROM subjects").fetchone()[0]
    if subjects_count == 0:
        subjects = [
            # Year 1
            (1, 1, 'Fundamentals of Computers'),
            (1, 1, 'Programming in C'),
            (1, 1, 'Mathematics I'),
            (1, 1, 'Digital Electronics'),
            (1, 1, 'Communication Skills / English'),
            (1, 2, 'Data Structures'),
            (1, 2, 'Computer Organization'),
            (1, 2, 'Discrete Mathematics'),
            (1, 2, 'Operating Systems (Basics)'),
            (1, 2, 'Environmental Studies'),
            # Year 2
            (2, 3, 'Object-Oriented Programming (C++ / Java)'),
            (2, 3, 'Database Management Systems'),
            (2, 3, 'Software Engineering'),
            (2, 3, 'Web Technologies'),
            (2, 3, 'Computer Networks'),
            (2, 4, 'Java Programming'),
            (2, 4, 'Python Programming'),
            (2, 4, 'Operating Systems (Advanced)'),
            (2, 4, 'Data Communication'),
            (2, 4, 'Numerical Methods / Statistics'),
            # Year 3
            (3, 5, 'Web Development (Advanced)'),
            (3, 5, 'Mobile Application Development'),
            (3, 5, 'Cloud Computing'),
            (3, 5, 'Artificial Intelligence / Machine Learning'),
            (3, 5, 'Cyber Security'),
            (3, 6, 'Big Data / Data Analytics'),
            (3, 6, 'Internet of Things (IoT)'),
            (3, 6, 'Project Work / Internship'),
            (3, 6, 'Software Testing'),
            (3, 6, 'Elective Subjects'),
        ]
        c.executemany(
            "INSERT INTO subjects (year, semester, name) VALUES (?,?,?)",
            subjects
        )

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully! (Existing data preserved)")
    if not admin_exists:
        print("   Admin  → Username: ADMIN   | Password: Admin12345")

if __name__ == '__main__':
    setup()