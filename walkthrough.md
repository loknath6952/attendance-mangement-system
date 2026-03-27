# BCA Attendance Management System — Walkthrough

This document outlines the recent enhancements, features, and critical bug fixes implemented in the BCA Attendance Management System to prepare it for production use and GitHub deployment.

## 🌟 1. Leave & OD (On Duty) Tracking Integration
The system has been fundamentally upgraded to support true 4-state attendance tracking instead of just binary Present/Absent.
* **Database Updates:** The `attendance` table's CHECK constraint was upgraded (`migrate_db.py`) to `CHECK(status IN ('P','A','OD','L'))`.
* **Calculation Logic:** The core `calc_percentage()` metric was updated in `app.py`. **OD and Leave are excluded from the denominator.** They do not penalize a student's attendance percentage.
* **Teacher Dashboard:** Updated `teacher_dashboard.html` to include color-coded custom radio buttons for all 4 states (Present = Green, Absent = Red, OD = Blue, Leave = Purple).

## 📊 2. Chart.js Admin Dashboard Trends
The administrator dashboard was visually enhanced to provide better analytical insights:
* **Weekly Bar Chart:** Replaced the static HTML table with a responsive **Chart.js Grouped Bar Chart** showing the precise count of Present, Absent, OD, and L statuses over the last 7 days.
* **Doughnut Chart:** The daily overview doughnut chart was updated to dynamically split between all 4 statuses instead of just 2.
* **Stat Cards:** New metric cards were added to the admin header showing today's exact OD and Leave counts.

## 📅 3. Multi-Faceted Date Range Filtering
The `/reports` portal was upgraded to handle historical slice reporting.
* **Date Pickers:** Replaced the static report view with dynamic `date_from` and `date_to` filters in `reports.html`.
* **Dynamic Queries:** The backend queries in `app.py` conditionally apply date bounds to the student summary table, ensuring admins can view exactly how attendance looked during a specific month or week.

## ⚠️ 4. Smart Low-Attendance Warning System
Students are now proactively warned about their attendance standing to prevent dropouts or exam disqualification.
* **Algorithmic Forecasting:** Created a `classes_needed_for_75(present, total)` function that runs a simulation `while` loop to find the *exact* number of consecutive future classes a student must attend to hit the 75% threshold.
* **Student Dashboard UI:** If a student drops below 75% in *any* subject, a yellow/red warning banner appears on `student_dashboard.html` itemizing the at-risk subjects and stating exactly how many classes they need to attend to recover.

## 📄 5. Student & Admin PDF/Excel Exports
Exporting functionality was completely polished across the board to act as official record-keeping:
* **Student-level PDF Generation:** Built a new `/student/export_pdf` route utilizing `reportlab`. A student can now click **"Download Report"** (added to `base.html` sidebar and `student_dashboard.html`) to instantly download a personalized, stylised PDF report of their subject-wise attendance (including OD/L records).
* **Admin-level PDF Logic Fix:** Corrected a critical logic flaw where the Admin PDF was counting `OD` and `L` as absent days. The formula was corrected to calculate `pct` only out of `P` and `A` totals.
* **Admin-level Excel Polish:** Updated `openpyxl` logic in `app.py` to highlight exported Excel rows with distinct colors (Green for Present, Red for Absent, Blue for OD, Purple for Leave) instead of treating OD/L as Absent.

## 💾 6. Database Persistence / Anti-Wipe Protection
Resolving the critical data-loss issue:
* **`init_db.py` Rewrite:** The initialization script was rewritten to strictly use `CREATE TABLE IF NOT EXISTS` and check for the existence of `ADMIN` and `subjects` before inserting. 
* You can now safely restart the server or re-run the `setup()` function without accidentally dropping all live student/attendance tables. All progressing data is completely persistent.
