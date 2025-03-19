import csv
import sys
import os
import time

class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id.strip()
        self.grade = grade.strip()
        self.marks_range = marks_range.strip()

    def display_grade_report(self):
        print(f"Grade ID: {self.grade_id} | Grade: {self.grade} | Marks Range: {self.marks_range}")

    def add_grade(self, grades_list):
        grades_list.append(self)
        #print(f"Grade {self.grade_id} added.")

    def delete_grade(self, grades_list):
        if self in grades_list:
            grades_list.remove(self)
            print(f"Grade {self.grade_id} deleted.")
        else:
            print("Grade not found.")

    def modify_grade(self, grade_id=None, grade=None, marks_range=None):
        if grade_id:
            self.grade_id = grade_id.strip()
        if grade:
            self.grade = grade.strip()
        if marks_range:
            self.marks_range = marks_range.strip()
        print(f"Grade {self.grade_id} modified.")

    def load_grades_from_dict(input_dict, grades_list):
        #Load grades dynamically from a dictionary if we arent using csv file
        for grade_id, grade_info in input_dict.items():
            grade = grade_info.get("grade", "").strip()
            marks_range = grade_info.get("marks_range", "").strip()
            grade_obj = Grades(grade_id, grade, marks_range)
            grade_obj.add_grade(grades_list)