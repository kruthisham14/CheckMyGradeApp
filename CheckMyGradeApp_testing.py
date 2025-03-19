import unittest
import time
import CheckMyGradeApp 
import Student
import Course
import encdyc
import Grades
import LoginUser
import Professor
import Student_Linked_List
import Student_Node
import Student

class CheckMyGradeAppTesting(unittest.TestCase):

    def setUp(self):
        self.student_list = Student_Linked_List.Student_Linked_List()
        self.courses = []
        self.professors = []
        self.grades = []
        self.logins = []

    def test_load_students_from_csv(self):
        app = CheckMyGradeApp.CheckMyGradeApp()
        app.load_students("Student.csv")  # Assuming you have a load_students method
        print(f"Loaded {len(app.students.to_list())} students from CSV")
        self.assertGreater(len(app.students.to_list()), 0)  # Ensure that students were loaded

    def test_student_addition(self):
        student = Student.Student("Nitin", "Prasad", "nitinprasad@sjsu.edu", "DATA200", "A", "95")
        self.student_list.add_new_student(student)
        self.assertIsNotNone(self.student_list.search_student("nitinprasad@sjsu.edu"))

    def test_student_deletion(self):
        student = Student.Student("Prahalad", "Venkat", "prahalad@sjsu.edu", "DATA201", "B", "85")
        self.student_list.add_new_student(student)
        self.assertTrue(self.student_list.delete_new_student("prahalad@sjsu.edu"))
        self.assertIsNone(self.student_list.search_student("prahalad@sjsu.edu"))

    def test_student_modification(self):
        student = Student.Student("Shishir", "MN", "shishir@sjsu.edu", "DATA203", "C", "75")
        self.student_list.add_new_student(student)
        updated_student = Student.Student("Shishir", "MN", "shishir@sjsu.edu", "DATA203", "B", "85")
        self.assertTrue(self.student_list.update_student("shishir@sjsu.edu", updated_student))
        found_student = self.student_list.search_student("shishir@sjsu.edu")[0]
        self.assertEqual(found_student.grades, "B")
        self.assertEqual(found_student.marks, 85.0)

    def test_large_dataset_search(self):
        for i in range(1000):
            student = Student.Student(f"first_n{i}", f"last_n{i}", f"student{i}@sjsu.edu", f"DATA{i}", "A", "90")
            self.student_list.add_new_student(student)
        
        start_time = time.time()
        found_student = self.student_list.search_student("student325@sjsu.edu")
        end_time = time.time()
        
        self.assertIsNotNone(found_student)
        self.assertLess(end_time - start_time, 1.0)  

    def test_sorting_by_name(self):
        students = [
            Student.Student("Nitin", "Prasad", "nitinprasad@sjsu.edu", "DATA200", "A", "95"),
            Student.Student("Prahalad", "Venkat", "prahalad@sjsu.edu", "DATA201", "B", "85"),
            Student.Student("Shishir", "MN", "shishir@sjsu.edu", "DATA203", "C", "75")
        ]
        for student in students:
            self.student_list.add_new_student(student)
        
        sorted_students = self.student_list.to_list()
        sorted_students.sort(key=lambda s: (s.lastName.lower(), s.firstName.lower()))
        
        self.assertEqual(sorted_students[0].firstName, "Shishir")
        self.assertEqual(sorted_students[1].firstName, "Nitin")
        self.assertEqual(sorted_students[2].firstName, "Prahalad")

    def test_sorting_by_marks(self):
        students = [
            Student.Student("Nitin", "Prasad", "nitinprasad@sjsu.edu", "DATA200", "A", "95"),
            Student.Student("Prahalad", "Venkat", "prahalad@sjsu.edu", "DATA201", "B", "85"),
            Student.Student("Shishir", "MN", "shishir@sjsu.edu", "DATA203", "C", "75")
        ]
        for student in students:
            self.student_list.add_new_student(student)
        
        sorted_students = self.student_list.to_list()
        start_time = time.time()
        sorted_students.sort(key=lambda s: s.marks, reverse=True)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to sort students by marks: {time_taken:.5f} seconds")
        
        self.assertEqual(sorted_students[0].firstName, "Nitin")
        self.assertEqual(sorted_students[1].firstName, "Prahalad")
        self.assertEqual(sorted_students[2].firstName, "Shishir")

    def test_course_operations(self):
        course = Course.Course("DATA200", "3", "Introduction to Python Programming")
        self.courses.append(course)
        self.assertEqual(len(self.courses), 1)
        
        course.delete_new_course(self.courses)
        self.assertEqual(len(self.courses), 0)

    def test_professor_operations(self):
        professor = Professor.Professor("Krishna", "krishna@sjsu.edu", "Associate Professor", "DATA200")
        self.professors.append(professor)
        self.assertEqual(len(self.professors), 1)
        
        professor.modify_professor_details(rank="Full Professor")
        self.assertEqual(self.professors[0].rank, "Full Professor")

    def test_grade_operations(self):
        grade = Grades.Grades("G001", "A", "90-100")
        self.grades.append(grade)
        self.assertEqual(len(self.grades), 1)
        
        grade.modify_grade(marks_range="91-100")
        self.assertEqual(self.grades[0].marks_range, "91-100")

    def test_login_user(self):
        user = LoginUser.LoginUser("user@sjsu.edu", "password123", "student")
        self.logins.append(user)
        
        self.assertTrue(user.login("user@sjsu.edu", "password123"))
        self.assertFalse(user.login("user@sjsu.edu", "wrongpassword"))

if __name__ == '__main__':
    unittest.main()
    #python -m unittest CheckMyGradeApp_testing.py
