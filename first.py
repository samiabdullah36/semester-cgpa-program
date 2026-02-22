# Program to calculate CGPA and show semester details

# Ask for semester number
semester = int(input("Please enter semester number (1-8): "))

# Check if semester number is valid
if semester < 1 or semester > 8:
    print("Invalid input! Please enter semester number within 1 to 8.")
else:
    # Ask for number of subjects
    subjects = int(input("Enter number of subjects (maximum 6): "))

    # Check if subject number is valid
    if subjects < 1 or subjects > 6:
        print("Invalid number of subjects! Please enter up to 6 subjects only.")
    else:
        total_grade_points = 0

        # Loop to take grades of each subject
        for i in range(1, subjects + 1):
            grade = float(input(f"Enter grade points for subject {i} (out of 5): "))

            # Check if grade is valid
            if grade < 0 or grade > 4:
                print("Invalid grade! Please enter grade between 0 and 4.")
                exit()

            total_grade_points += grade

        # Calculate CGPA
        cgpa = total_grade_points / subjects

        # Display results
        print("\n----- RESULT -----")
        print("Semester Number:", semester)
        print("Number of Subjects:", subjects)
        print("CGPA:", round(cgpa, 2))