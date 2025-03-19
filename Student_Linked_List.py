import csv
import sys
import os
import time
import Student_Node

class Student_Linked_List:
    def __init__(self):
        self.head = None

    def add_new_student(self, student):
        new_node = Student_Node.Student_Node(student)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        #print(f"Adding Student {student.firstName} {student.lastName}.")
    
    def delete_new_student(self, email):
        students = self.search_student(email)
        if students and len(students) > 1:
            print(f"Multiple students found with email {email}. Please select which one to delete:")
            for idx, student in enumerate(students):
                print(f"{idx + 1}: {student.firstName} {student.lastName} | Course: {student.course_id}")
            choice = int(input("Enter the number of the student to delete: ")) - 1
            selected_student = students[choice]
        elif students and len(students) == 1:
            selected_student = students[0]
        else:
            print("No student found")
            return False
        current = self.head
        previous = None
        while current:
            if current.student == selected_student:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print("Selected student deleted.")
                return True
            previous = current
            current = current.next
    
    def update_student(self, old_email, updated_student):
        students = self.search_student(old_email)
        if students and len(students) > 1:
            print(f"Multiple students found with email {old_email}. Please select which one to update:")
            for idx, student in enumerate(students):
                print(f"{idx + 1}: {student.firstName} {student.lastName} | Course: {student.course_id}")
            choice = int(input("Enter the number of the student to update: ")) - 1
            selected_student = students[choice]
            current = self.head
            while current:
                if current.student == selected_student:
                    current.student = updated_student
                    print("Selected student updated.")
                    return True
                current = current.next
        elif students:
            current = self.head
            while current:
                if current.student.email_address.lower() == old_email.lower():
                    current.student = updated_student
                    print("Student record updated.")
                    return True
                current = current.next
        else:
            print("No student found.")


    def search_student(self, email):
        email = email.strip().lower()
        current = self.head
        results = []
        start_time = time.time()
        while current:
            if current.student.email_address.lower() == email:
                results.append(current.student)
            current = current.next
        elapsed = time.time() - start_time
        if results:
                print(f"Found {len(results)} record(s) for {email}. Time taken: {elapsed:.5f} seconds")
                return results
        else:
                print(f"No student found with email {email}. Time taken: {elapsed:.5f} seconds")
                return None
                print(f"Time taken for search {elapsed:.5f} seconds")
                #return current.student
            #current = current.next
        #elapsed = time.time() - start_time
        #print(f"Student you are looking not found. Time taken for search {elapsed:.5f} seconds")
        #return None

    def display_all_students(self):
        if not self.head:
            print("Student record unavailable")
            return
        current = self.head
        while current:
            current.student.display_records()
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.student)
            current = current.next
        return result

    def display_sorted_by_name(self):
        students_list = self.to_list()
        start_time = time.time()
        students_list.sort(key=lambda s: (s.lastName.lower(), s.firstName.lower()))
        elapsed = time.time() - start_time
        print(f"\n--- Students Sorted by Name (Last, First). Sorting took approximately {elapsed:.5f} seconds ---")
        for student in students_list:
            student.display_records()

    def display_sorted_by_marks_desc(self):
        students_list = self.to_list()
        start_time = time.time()
        students_list.sort(key=lambda s: s.marks, reverse=True) # Sort in descending order
        elapsed = time.time() - start_time
        print(f"\n--- Students Sorted by Marks (High to Low). Sorting took approximately {elapsed:.5f} seconds ---")
        for student in students_list:
            student.display_records()
    
    def display_sorted_by_marks_asce(self):
        students_list = self.to_list()
        start_time = time.time()
        students_list.sort(key=lambda s: s.marks, reverse=False)  # Sort in ascending order 
        elapsed = time.time() - start_time
        print(f"\n--- Students Sorted by Marks (Low to High). Sorting took approximately {elapsed:.5f} seconds ---")
        for student in students_list:
            student.display_records()


    def average_marks(self, course_id=None):
        students_list = self.to_list()
        if course_id:
            students_list = [s for s in students_list if s.course_id.lower() == course_id.lower()]
        if not students_list:
            print("No students found (or no matching course) to compute average.")
            return
        total = sum(s.marks for s in students_list)
        avg = total / len(students_list)
        if course_id:
            print(f"Average marks for course '{course_id}': {avg:.2f}")
        else:
            print(f"Average marks (All Courses): {avg:.2f}")

    def median_marks(self, course_id=None):
        students_list = self.to_list()
        if course_id:
            students_list = [s for s in students_list if s.course_id.lower() == course_id.lower()]
        if not students_list:
            print("No students found (or no matching course) to compute median.")
            return
        sorted_marks = sorted(s.marks for s in students_list)
        n = len(sorted_marks)
        mid = n // 2
        if n % 2 == 1:
            median_val = sorted_marks[mid]
        else:
            median_val = (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
        if course_id:
            print(f"Median marks for course '{course_id}': {median_val:.2f}")
        else:
            print(f"Median marks (All Courses): {median_val:.2f}")