import sqlite3

def run_migration():
    conn = sqlite3.connect('data/attendance.db')
    c = conn.cursor()
    
    print("Running migration to update 'attendance' table check constraints...")
    
    # SQLite doesn't support ALTER TABLE ... DROP CONSTRAINT easily.
    # The safest way is to rename the old table, create the new one, copy data, and drop the old one.
    
    try:
        c.execute("BEGIN TRANSACTION")
        
        c.execute("ALTER TABLE attendance RENAME TO attendance_old")
        
        c.execute('''
            CREATE TABLE attendance (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT    NOT NULL REFERENCES students(reg_no),
                subject_id INTEGER NOT NULL REFERENCES subjects(id),
                teacher_id INTEGER NOT NULL REFERENCES users(id),
                date       TEXT    NOT NULL,
                period     INTEGER NOT NULL,
                status     TEXT    NOT NULL CHECK(status IN ('P','A','OD','L'))
            )
        ''')
        
        c.execute('''
            INSERT INTO attendance (id, student_id, subject_id, teacher_id, date, period, status)
            SELECT id, student_id, subject_id, teacher_id, date, period, status FROM attendance_old
        ''')
        
        c.execute("DROP TABLE attendance_old")
        
        c.execute("COMMIT")
        print("✅ Migration successful: Updated CHECK constraint to support OD and Leave.")
    except Exception as e:
        c.execute("ROLLBACK")
        print("❌ Migration failed:", str(e))
    finally:
        conn.close()

if __name__ == '__main__':
    run_migration()
