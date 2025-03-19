import csv
import sys
import os
import time

class Student_Node:
    def __init__(self, student):
        self.student = student
        self.next = None