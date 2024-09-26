def manage_student_database():
    # Initialize an empty list to store student tuples
    students = []
    student_id = 1  # Counter variable for generating student IDs

    while True:
        # Prompt the user to enter a student's name or "stop" to finish
        name = input("Please enter the student's name (or type 'stop' to finish): ")

        # Check if the user entered "stop" to exit the loop
        if name.lower() == 'stop':
            break

        # Check for duplicate names
        if name in [student[1] for student in students]:
            print("This name is already in the list.")
        else:
            # Add the student tuple (ID, name) to the list
            students.append((student_id, name))
            student_id += 1

    # Display the complete list of student tuples after all names are entered
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Calculate the total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")

    # Identify the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))

        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Call the function to run the program
manage_student_database()
