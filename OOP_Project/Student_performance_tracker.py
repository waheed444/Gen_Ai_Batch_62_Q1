
# WAHEED AHMAD (Roll no: PIAIC-245268)

class Student:
    def __init__(self, name, scores):
        """Initialize a student with their name and a list of scores."""
        self.name = name
        self.scores = scores

    def calculate_average(self):
        """Calculate and return the average score of the student."""
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0

    def is_passing(self, passing_score=40):
        """Determine if the student is passing based on all scores being above the passing score."""
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        """Initialize the tracker with an empty dictionary of students."""
        self.students = {}

    def add_student(self, name, scores):
        """Add a new student to the tracker."""
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        """Calculate and return the average score for the entire class."""
        if self.students:
            total_average = sum(student.calculate_average() for student in self.students.values())
            return total_average / len(self.students)
        return 0

    def display_student_performance(self):
        """Display the performance of all students in the tracker."""
        print("Student Performance Summary :")
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {student.name:10} | Average Score: {average:.2f} | Status: {status}")

    def display_class_average(self):
        """Display the overall class average score."""
        class_average = self.calculate_class_average()
        print("\nClass Average Score:")
        print(f"{class_average:.2f}")


def main():
    """Main function to run the student performance tracker."""
    tracker = PerformanceTracker()

    while True:
        name = input("Enter the student's name (or type 'exit' to finish): ").strip()
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
                    print("Invalid input. Please enter a valid integer.")

        tracker.add_student(name, scores)

    print()  # Blank line for better readability
    tracker.display_student_performance()
    print()  # Blank line for better readability
    tracker.display_class_average()


if __name__ == "__main__":
    main()


