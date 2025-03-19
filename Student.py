import csv
import sys
import os
import time

class Student:
    def __init__(self, firstName, lastName, email_address, course_id, grades, marks):
        self.firstName = firstName.strip()
        self.lastName = lastName.strip()
        self.email_address = email_address.strip()
        self.course_id = course_id.strip()
        self.grades = grades.strip()
        self.marks = float(marks) if marks else 0.0

    def display_records(self):
        print(f"{self.firstName} {self.lastName} ({self.email_address}) | Course: {self.course_id} | Grades: {self.grades} | Marks: {self.marks}")

    #def add_new_student():

    #def delete_new_student():
    
    def check_my_grades(self):
        print(f"{self.firstName} {self.lastName}'s Grades: {self.grades}")

    def update_student_record(self, firstName=None, lastName=None, email_address=None, course_id=None, grades=None, marks=None):
        if firstName:
            self.firstName = firstName.strip()
        if lastName:
            self.lastName = lastName.strip()
        if email_address:
            self.email_address = email_address.strip()
        if course_id:
            self.course_id = course_id.strip()
        if grades:
            self.grades = grades.strip()
        if marks:
            self.marks = float(marks)
        print("Student record got updated")

    def check_my_marks(self):
        print(f"{self.firstName} {self.lastName}'s Marks: {self.marks}")

    