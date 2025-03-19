import csv
import sys
import os
import time

class Course:
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id.strip()
        self.credits = credits.strip()
        self.course_name = course_name.strip()

    def display_courses(self):
        print(f"Course ID: {self.course_id} | Credits: {self.credits} | Course Name: {self.course_name}")

    def add_new_course(self, course_list):
        course_list.append(self)
        print(f"Course {self.course_id} added.")
    
    def delete_new_course(self, course_list):
        matches = [course for course in course_list if course.course_name == self.course_name]
        if len(matches) > 1:
            print("Multiple courses found. Please select which one to delete:")
            for idx, course in enumerate(matches):
                print(f"{idx + 1}: {course.course_name} | ID: {course.course_id}")
            choice = int(input("Enter the number of the course to delete: ")) - 1
            course_list.remove(matches[choice])
            print(f"Course {matches[choice].course_name} deleted.")
        elif matches:
            course_list.remove(matches[0])
            print(f"Course {matches[0].course_name} deleted.")
        else:
            print("Course not found.")
