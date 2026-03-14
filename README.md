# 📊 Student Grade Tracker
**Python console application for tracking and analysing student grades.**

Built by Damian Ciumacenco — Software Engineering student at Maynooth University.

---

## 📌 Overview
A Python OOP project that lets you manage multiple students and their grades through a menu-driven terminal interface. Grades are automatically saved to a JSON file so your data persists between sessions — no data lost when you close the program.

---

## ✨ Features
- Add and delete students
- Record multiple grades per student (0–100 validation)
- View individual student summaries — average, letter grade, highest & lowest
- View all students at a glance with averages
- Full class statistics — total students, class average, highest and lowest grade
- Automatic save and load via JSON — data persists between sessions

---

## 🛠️ Built With
- Python 3
- Object-Oriented Programming (Classes, Methods, Encapsulation)
- JSON for persistent data storage
- File I/O (`json`, `os` modules)

---

## 🚀 How to Run

**Requirements:** Python 3 installed

```bash
python grade_tracker.py
```

No external libraries needed — runs straight out of the box.

---

## 📸 Preview

```
==================================================
         STUDENT GRADE TRACKER
==================================================

MAIN MENU:
1. Add Student
2. Add Grade
3. View Student Summary
4. View All Students
5. Class Statistics
6. Delete Student
7. Exit
--------------------------------------------------

STUDENT SUMMARY: Damian
==================================================
Grades: [85.0, 91.0, 78.0, 95.0]
Average: 87.2
Letter Grade: B
Highest: 95.0
Lowest: 78.0
Total Grades: 4
==================================================
```

---

## 📁 Project Structure

```
├── grade_tracker.py    # Main application — GradeTracker class and menu loop
├── grades_data.json    # Auto-generated — stores all student data persistently
```

---

## 📝 Grade Scale

| Average | Letter Grade |
|---------|-------------|
| 90–100  | A           |
| 80–89   | B           |
| 70–79   | C           |
| 60–69   | D           |
| Below 60| F           |

---

## 👨‍💻 Author
**Damian Ciumacenco** — [GitHub](https://github.com/DamianCiumacenco) · [LinkedIn](https://www.linkedin.com/in/damian-ciumacenco-71b15a283/)
