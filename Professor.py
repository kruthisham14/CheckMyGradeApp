import csv
import sys
import os
import time

class Professor:
    def __init__(self, name, email_address, rank, course_id):
        self.name = name.strip()
        self.email_address = email_address.strip()
        self.rank = rank.strip()
        self.course_id = course_id.strip()

    def professors_details(self):
        print(f"Professor: {self.name} | Email: {self.email_address} | Rank: {self.rank} | Course: {self.course_id}")

    def add_new_professor(self, professor_list):
        professor_list.append(self)
        print(f"Professor {self.name} added.")

    def delete_professore(self, professor_list):
        if self in professor_list:
            professor_list.remove(self)
            print(f"Professor {self.name} deleted.")
        else:
            print("Professor not found.")

    def modify_professor_details(self, name=None, email_address=None, rank=None, course_id=None):
        if name:
            self.name = name.strip()
        if email_address:
            self.email_address = email_address.strip()
        if rank:
            self.rank = rank.strip()
        if course_id:
            self.course_id = course_id.strip()
        print("Professor details modified.")

    def show_course_details_by_professor(self, course_list):
        matches = [c for c in course_list if c.course_id.lower() == self.course_id.lower()]
        if matches:
            print(f"{self.name} teaches:")
            for course in matches:
                course.display_courses()
        else:
            print("No matching course found.")