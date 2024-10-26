# Student Performance Tracker

#### This project is a Python-based system that allows teachers to input student scores, track performance across subjects, and calculate useful statistics like averages and passing status. It uses Object-Oriented Programming (OOP) concepts, loops, conditionals, and data structures like lists and dictionaries.

## Features:

- Add students and input their scores for multiple subjects.
- Calculate the average score for each student.
- Determine if students are passing based on their subject scores.
- Calculate the class average across all students.
- Display performance feedback (pass/fail) for each student.

## Installation Instructions

### Prerequisites:
Ensure you have Python installed on your machine. You can download Python from the official [Python website](https://www.python.org/downloads/). This project works with **Python 3.6+**.

### Step 1: Clone the Repository
To get started, clone this repository to your local machine using the following command:

## Git clone
 https://github.com/your-username/student-performance-tracker.git


## Student Performance Tracker

### How to Use
1. You will be prompted to enter a student’s name and their scores for 3 subjects: Math, Science, and English.
2. The program will ask you to input scores for each subject (ensure they are valid integers).
3. You can enter as many students as you like. To stop adding students, type 'done' when prompted for the student's name.
4. Once all students are entered, the program will display:
   - Each student's average score.
   - Whether the student is passing or needs improvement.
   - The overall class average.

### Example Output:
```yaml
Enter the student's name (or 'exit' to stop): Ali
Enter the Math score for Alice: 85
Enter the Science score for Alice: 90
Enter the English score for Alice: 78

Enter the student's name (or 'exit' to stop): Waheed
Enter the Math score for Bob: 35
Enter the Science score for Bob: 45
Enter the English score for Bob: 50

Enter the student's name (or 'exit' to stop): exit

Student Performance Summary:

Student: Ali | Average Score: 84.33 | Status: Passing
Student: Waheed   | Average Score: 43.33 | Status: Needs Improvement

Class Average: 63.83
```
### Project Structure

```yaml
├── student_performance_tracker.py   # Main Python script for the tracker
├── README.md                        # This file
└── requirements.txt                 # Dependency file (optional)

```
### Error Handling:
If a non-numeric value is entered for the scores, the program will prompt the user to re-enter the value.
The system gracefully handles cases where no students are entered.
### Future Improvements:
Add functionality to track additional subjects.
Implement a GUI for easier interaction.
Store student performance data in a database for persistent tracking.