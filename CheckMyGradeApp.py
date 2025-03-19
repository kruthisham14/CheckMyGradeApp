import csv
import sys
import os
import time
import Course
import Grades
import LoginUser
import Professor
import Student_Linked_List
import Student_Node
import Student

class CheckMyGradeApp:
    def __init__(self):
        self.students = Student_Linked_List.Student_Linked_List()
        self.grades = []
        self.courses = []
        self.professors = []
        self.logins = []
        self.load_data()

    def load_data(self):
        self.load_students("Student.csv")
        self.load_courses("Course.csv")
        self.load_professors("Professor.csv")
        self.load_logins("Login.csv")
        #self.load_grades("Grades.csv") #Can enable loading the csv if needed
        # Instead of loading from CSV, we load grades from a dictionary
        grades_data = {
            "G001": {"grade": "A", "marks_range": "90-100"},
            "G002": {"grade": "B", "marks_range": "80-89"},
            "G003": {"grade": "C", "marks_range": "70-79"},
            "G004": {"grade": "D", "marks_range": "60-69"},
            "G005": {"grade": "F", "marks_range": "0-59"}
        }
        self.load_grades_from_dict(grades_data)

    def save_data(self):
        self.save_students("Student.csv")
        self.save_courses("Course.csv")
        self.save_professors("Professor.csv")
        self.save_logins("Login.csv")
        #self.save_grades("Grades.csv")
        print("All data successfully saved")

    def load_students(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student.Student(
                        row.get('firstname', ''),
                        row.get('lastname', ''),
                        row.get('email', ''),
                        row.get('courseId', ''),
                        row.get('grades', ''),
                        row.get('marks', '0')
                    )
                    self.students.add_new_student(student)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty student list.")
        except PermissionError:
            print(f"Permission denied: Cannot access {filename}.")
        except Exception as e:
            print(f"An error occurred while loading {filename}: {e}")

    def save_students(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['email', 'firstname', 'lastname', 'courseId', 'grades', 'marks']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            current = self.students.head
            while current:
                s = current.student
                writer.writerow({
                    'email': s.email_address,
                    'firstname': s.firstName,
                    'lastname': s.lastName,
                    'courseId': s.course_id,
                    'grades': s.grades,
                    'marks': s.marks
                })
                current = current.next

    def load_courses(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    course = Course.Course(
                        row.get('courseId', ''),
                        row.get('Credits', ''),
                        row.get('Course_Name', '')
                    )
                    self.courses.append(course)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty course list.")

    def save_courses(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['courseId', 'Credits', 'Course_Name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for c in self.courses:
                writer.writerow({
                    'courseId': c.course_id,
                    'Credits': c.credits,
                    'Course_Name': c.course_name
                })

    def load_professors(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    professor = Professor.Professor(
                        row.get('Professor_Name', ''),
                        row.get('Professor_id', ''),
                        row.get('Rank', ''),
                        row.get('courseID', '')
                    )
                    self.professors.append(professor)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty professor list.")

    def save_professors(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['Professor_id', 'Professor_Name', 'Rank', 'courseID']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.professors:
                writer.writerow({
                    'Professor_id': p.email_address,
                    'Professor_Name': p.name,
                    'Rank': p.rank,
                    'courseID': p.course_id
                })

    def load_logins(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = LoginUser.LoginUser(
                        row.get('User_id', ''),
                        row.get('Password', ''),
                        row.get('Role', ''),
                        encrypted=True
                    )
                    #user.password = row.get('Password', '') 
                    self.logins.append(user)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty login list.")

    def save_logins(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['User_id', 'Password', 'Role']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for u in self.logins:
                    writer.writerow({
                        'User_id': u.email_id,
                        'Password': u.password,
                        'Role': u.role
                    })
            print(f"Logins saved successfully to {filename}.")
        except PermissionError:
            print(f"Permission denied: Unable to save {filename}. Please close the file if it's open in another program.")

    def load_grades(self, filename):
        try:
            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grade = Grades.Grades(
                        row.get('grade_id', ''),
                        row.get('grade', ''),
                        row.get('marks_range', '')
                    )
                    self.grades.append(grade)
        except FileNotFoundError:
            print(f"{filename} not found. Starting with empty grades list.")

    def save_grades(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['grade_id', 'grade', 'marks_range']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for g in self.grades:
                writer.writerow({
                    'grade_id': g.grade_id,
                    'grade': g.grade,
                    'marks_range': g.marks_range
                })

    def load_grades_from_dict(self, grades_data):
        #This function load grades dynamically from dict instead of csv file
        Grades.Grades.load_grades_from_dict(grades_data, self.grades)

    def menu(self):
        print("-------------------------\n")
        print("CheckMyGrade Main Menu\n")
        print("-------------------------\n")
        print("a. Login Operations")
        print("b. Student Operations")
        print("c. Professor Operations")
        print("d. Course Operations")
        print("e. Grades Operations")
        print("f. Reports & Stats")
        print("g. Exit")

    def run_app(self):
        try:
            while True:
                self.menu()
                choice = input("Enter your choice: ").strip()
                if choice == "a":
                    self.login_operations()
                elif choice == "b":
                    self.student_operations()
                elif choice == "c":
                    self.professor_operations()
                elif choice == "d":
                    self.course_operations()
                elif choice == "e":
                    self.grades_operations()
                elif choice == "f":
                    self.reports_and_stats_menu()
                elif choice == "g":
                    print("Saving data before exiting...")
                    self.save_data()
                    print("Data saved successfully")
                    print("Exiting CheckMyGrade Application.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nSaving data before exit...")
            self.save_data()
            print("Data saved successfully")
            sys.exit(0)

    def login_operations_menu(self):
        print("\n--- Login Operations ---")
        print("a. Login")
        print("b. Change Password")
        print("c. Signup (New user)")
        print("d. Return to Main Menu")

    def login_operations(self):
        while True:
            self.login_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                email = input("Email: ")
                password = input("Password: ")
                user_found = next((u for u in self.logins if u.email_id.lower() == email.lower()), None)
                if user_found:
                    if user_found.login(email, password):
                        break
                else:
                    print("User not found.")
            elif ch == 'b':
                email = input("Email: ")
                user_found = next((u for u in self.logins if u.email_id.lower() == email.lower()), None)
                if user_found:
                    new_pass = input("New Password: ")
                    user_found.change_password(new_pass)
                else:
                    print("User not found.")
            elif ch == 'c':
                email = input("Email: ")
                if any(u.email_id.lower() == email.lower() for u in self.logins):
                    print("User already exists with this email. Please try logging in")
                    continue
                password = input("Password: ")
                is_valid, message = self.validate_password(password)
                if not is_valid:
                    print(message)
                    continue
                role = input("Role: ")
                new_user = LoginUser.LoginUser(email, password, role)
                self.logins.append(new_user)
                print("New user added.")
            elif ch == 'd':
                break
            else:
                print("Invalid option.")

    def validate_password(self, password):
        if len(password) < 6:
            return False, "Password must be at least 6 characters long."
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit."
        if not any(char.isalpha() for char in password):
            return False, "Password must contain at least one letter."
        return True, "Password is valid."

    def student_operations_menu(self):
        print("\n--- Student Operations ---")
        print("a. Display All Students")
        print("b. Search Student Record")
        print("c. Add New Student")
        print("d. Delete Student")
        print("e. Update Student Record")
        print("f. Check Grades")
        print("g. Check Marks")
        print("h. Return to Main Menu")

    def student_operations(self):
        while True:
            self.student_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                self.students.display_all_students()
            elif ch == 'b':
                email = input("Enter student's email: ")
                students = self.students.search_student(email)
                if students:
                    for student in students:
                        student.display_records()
            elif ch == 'c':
                firstName = input("Enter first name: ").strip()
                lastName = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                if not email or "@" not in email:
                    print("Invalid email. Please try again.")
                    continue
                course_id = input("Enter course ID: ").strip()
                grades = input("Enter grades: ").strip().upper()
                marks = input("Enter marks: ").strip()
                try:
                    marks = float(marks)
                    if not (0 <= marks <=100):
                        print("Marks must be between 0 and 100")
                        continue
                except ValueError:
                    print("Invalid marks. Please enter a numeric value.")
                    continue
                new_student = Student.Student(firstName, lastName, email, course_id, grades, marks)
                self.students.add_new_student(new_student)
            elif ch == 'd':
                email = input("Enter student's email to delete: ")
                self.students.delete_new_student(email)
            elif ch == 'e':
                email = input("Enter student's current email to update: ")
                student = self.students.search_student(email)
                if student:
                    print("Enter new details (leave blank to keep current)")
                    firstName = input("First name: ") or student.firstName
                    lastName = input("Last name: ") or student.lastName
                    email_new = input("Email: ") or student.email_address
                    course_id = input("Course ID: ") or student.course_id
                    grades = input("Grades: ") or student.grades
                    marks = input("Marks: ") or str(student.marks)
                    updated_student = Student.Student(firstName, lastName, email_new, course_id, grades, marks)
                    self.students.update_student(email, updated_student)
            elif ch == 'f':
                email = input("Enter student's email to check grades: ")
                students = self.students.search_student(email)
                if students:
                    for student in students:
                        student.check_my_grades()
            elif ch == 'g':
                email = input("Enter student's email to check marks: ")
                students = self.students.search_student(email)
                if students:
                    for student in students:
                        student.check_my_marks()
            elif ch == 'h':
                break
            else:
                print("Invalid option.")

    def professor_operations_menu(self):
        print("\n--- Professor Operations ---")
        print("a. Display All Professors")
        print("b. Add New Professor")
        print("c. Delete Professor")
        print("d. Modify Professor Details")
        print("e. Show Professor's Course Details")
        print("f. Return to Main Menu")

    def professor_operations(self):
        while True:
            self.professor_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.professors:
                    print("No professor records available.")
                else:
                    for p in self.professors:
                        p.professors_details()
            elif ch == 'b':
                name = input("Name: ")
                email = input("Email: ")
                rank = input("Rank: ")
                course_id = input("Course ID: ")
                course_match = next((c for c in self.courses if c.course_id.lower() == course_id.lower()), None)
                if course_match:
                    print(f"Found Course: {course_match.course_name} | Credits: {course_match.credits}")
                else:
                    print("Warning: Course not found in Course.csv. Please add the course first.")
                new_prof = Professor.Professor(name, email, rank, course_id)
                new_prof.add_new_professor(self.professors)
            elif ch == 'c':
                email = input("Enter professor's email to delete: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    prof_found.delete_professore(self.professors)
                else:
                    print("Professor not found.")
            elif ch == 'd':
                email = input("Enter professor's email to modify: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    print("Enter new details (leave blank to keep current):")
                    name = input("Name: ") or prof_found.name
                    email_new = input("Email: ") or prof_found.email_address
                    rank = input("Rank: ") or prof_found.rank
                    course_id = input("Course ID: ") or prof_found.course_id
                    prof_found.modify_professor_details(name, email_new, rank, course_id)
                else:
                    print("Professor not found.")
            elif ch == 'e':
                email = input("Enter professor's email to view course details: ")
                prof_found = next((p for p in self.professors if p.email_address.lower() == email.lower()), None)
                if prof_found:
                    prof_found.show_course_details_by_professor(self.courses)
                else:
                    print("Professor not found.")
            elif ch == 'f':
                break
            else:
                print("Invalid option.")

    def course_operations_menu(self):
        print("\n--- Course Operations ---")
        print("a. Display All Courses")
        print("b. Add New Course")
        print("c. Delete Course")
        print("d. Return to Main Menu")

    def course_operations(self):
        while True:
            self.course_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.courses:
                    print("No course records available.")
                else:
                    for c in self.courses:
                        c.display_courses()
            elif ch == 'b':
                course_id = input("Course ID: ")
                credits = input("Credits: ")
                course_name = input("Course Name: ")
                new_course = Course.Course(course_id, credits, course_name)
                new_course.add_new_course(self.courses)
            elif ch == 'c':
                course_id = input("Enter Course ID to delete: ")
                course_found = next((co for co in self.courses if co.course_id.lower() == course_id.lower()), None)
                if course_found:
                    course_found.delete_new_course(self.courses)
                else:
                    print("Course not found.")
            elif ch == 'd':
                break
            else:
                print("Invalid option.")

    def grades_operations_menu(self):
        print("\n--- Grades Operations ---")
        print("a. Display Grade Reports")
        print("b. Add New Grade")
        print("c. Delete Grade")
        print("d. Modify Grade")
        print("e. Return to Main Menu")

    def grades_operations(self):
        while True:
            self.grades_operations_menu()
            ch = input("Choose an option: ").strip().lower()
            if ch == 'a':
                if not self.grades:
                    print("No grade records available.")
                else:
                    for g in self.grades:
                        g.display_grade_report()
            elif ch == 'b':
                grade_id = input("Grade ID: ")
                grade_val = input("Grade (A, B, C, etc.): ")
                marks_range = input("Marks Range (e.g., 90-100): ")
                new_grade = Grades.Grades(grade_id, grade_val, marks_range)
                new_grade.add_grade(self.grades)
            elif ch == 'c':
                grade_id = input("Grade ID to delete: ")
                found = next((g for g in self.grades if g.grade_id.lower() == grade_id.lower()), None)
                if found:
                    found.delete_grade(self.grades)
                else:
                    print("Grade not found.")
            elif ch == 'd':
                grade_id = input("Grade ID to modify: ")
                found = next((g for g in self.grades if g.grade_id.lower() == grade_id.lower()), None)
                if found:
                    new_grade_id = input("New Grade ID (blank to keep current): ")
                    new_grade_val = input("New Grade (blank to keep current): ")
                    new_marks_range = input("New Marks Range (blank to keep current): ")
                    found.modify_grade(new_grade_id, new_grade_val, new_marks_range)
                else:
                    print("Grade not found.")
            elif ch == 'e':
                break
            else:
                print("Invalid option.")

    def reports_and_stats_menu(self):
        while True:
            print("\n--- Reports & Stats Menu ---")
            print("a. Sort Students by Name")
            print("b. Sort Students by Marks (Descending)")
            print("c. Sort Students by Marks (Ascending)")
            print("d. Average Marks (All or by Course)")
            print("e. Median Marks (All or by Course)")
            print("f. Course-wise Report (Which students?)")
            print("g. Professor-wise Report (Which students?)")
            print("h. Student-wise Report (All courses/grades?)")
            print("i. Return to Main Menu")
            choice = input("Choose an option: ").strip().lower()
            if choice == 'a':
                self.students.display_sorted_by_name()
            elif choice == 'b':
                self.students.display_sorted_by_marks_desc()
            elif choice == 'c':
                self.students.display_sorted_by_marks_asce()
            elif choice == 'd':
                c_id = input("Enter course ID (or leave blank for ALL): ").strip()
                if c_id == "":
                    self.students.average_marks()
                else:
                    self.students.average_marks(c_id)
            elif choice == 'e':
                c_id = input("Enter course ID (or leave blank for ALL): ").strip()
                if c_id == "":
                    self.students.median_marks()
                else:
                    self.students.median_marks(c_id)
            elif choice == 'f':
                c_id = input("Enter course ID: ")
                self.report_course(c_id)
            elif choice == 'g':
                email = input("Enter professor's email: ")
                self.report_professor(email)
            elif choice == 'h':
                email = input("Enter student's email: ")
                self.report_student(email)
            elif choice == 'i':
                break
            else:
                print("Invalid option.")

    def report_course(self, course_id):
        course_id = course_id.strip().lower()
        found_any = False
        current = self.students.head
        print(f"\n--- Course-wise Report for Course ID: {course_id} ---")
        while current:
            if current.student.course_id.lower() == course_id:
                current.student.display_records()
                found_any = True
            current = current.next
        if not found_any:
            print("No students found for that course.")

    def report_professor(self, prof_email):
        prof_email = prof_email.strip().lower()
        professor_found = None
        for p in self.professors:
            if p.email_address.lower() == prof_email:
                professor_found = p
                break
        if not professor_found:
            print("Professor not found.")
            return
        prof_course_id = professor_found.course_id.lower()
        print(f"\n--- Professor wise Report for: {professor_found.name}, Course: {prof_course_id} ---")
        current = self.students.head
        found_any = False
        while current:
            if current.student.course_id.lower() == prof_course_id:
                current.student.display_records()
                found_any = True
            current = current.next
        if not found_any:
            print("No students found for that professor's course.")

    def report_student(self, student_email):
        students = self.students.search_student(student_email)
        if students:
            print("\n--- Student wise Report ---")
            for student in students:
                student.display_records()
        else:
            print("Student not found.")

if __name__ == "__main__":
    app = CheckMyGradeApp()
    app.run_app()