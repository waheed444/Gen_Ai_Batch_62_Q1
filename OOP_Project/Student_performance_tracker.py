
#WAHEED AHMAD  (Roll no: PIAIC-245268)
class Student:
    def __init__(self, name, scores):
        # Initialize student with name and their scores
        self.name = name
        self.scores = scores
    def calculate_average(self):
        # Return average score of the student
        return sum(self.scores) / len(self.scores) if self.scores else 0
    def is_passing(self, passing_score=40):
        # Determine if student passed based on all scores being above passing_score
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        # Initialize tracker with an empty list of students
        self.students = {}
    def add_student(self, name, scores):
        # Add new student to the tracker
        self.students[name] = Student(name, scores)
    def calculate_class_average(self):
        # Calculate average score for all students in the class
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students) if self.students else 0
    def display_student_performance(self):
        # Display formatted student performance summary
        print("\n" + "-" * 100)
        print(" " * 5 + "Student Performance Summary".center(60))
        print("-" * 100)
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            # Format each row to display "Student", "Average Score", and "Status" without '|'
            print(f"  Student   :  {student.name.ljust(25)}   Average Score  :  {str(round(average, 2)).ljust(10)}   Status   :  {status.ljust(8)}")
    def display_class_average(self):
        # Display overall class average
        class_average = self.calculate_class_average()
        print("-" * 100)
        print(f"  Class Average Score :  {str(round(class_average, 2)).ljust(10)}")
        print("-" * 100)
def main():
    tracker = PerformanceTracker()
    while True:
        name = input("Enter the student's name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        scores = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    score = int(input(f"Enter {subject} score for {name} (0-100): "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Error: Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        tracker.add_student(name, scores)
    tracker.display_student_performance()
    tracker.display_class_average()
if __name__ == "__main__":
    main()

