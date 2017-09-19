import unittest
import numpy as np
from decimal import *

####################################################
# Problem 1: Classes
####################################################


class Course:
    def __init__(self, course_number):
        self.course_number = course_number
        self.roster = []

    def get_course_number(self):
        return self.course_number

    def add_student(self, student):
        self.roster.append(str(student))

    def drop_student(self, student_id):
        self.roster.remove(str(student_id))

    def get_roster(self):
        return sorted(self.roster)

####################################################
# Problem 2: Root Finding
####################################################


def find_roots(a, b, c):
    getcontext().prec = 100
    if a == 0 and b != 0:
        return [-c / b]
    elif b == 0 and a == 0:
        return []

    if b**2 - 4 * a * c < 0:
        return []

    if c == 0:
        d = b
    else:
        d = Decimal(b ** 2) - Decimal(4 * a * c)
        d = d.sqrt()

    r1 = (Decimal(-b) + Decimal(d)) / Decimal(2 * a)

    if d == 0:
        return [float(r1)]
    else:
        r2 = (Decimal(-b) - Decimal(d)) / Decimal(2 * a)
        return sorted([float(r1), float(r2)])
