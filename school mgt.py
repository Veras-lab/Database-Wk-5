
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict
import random

"""
School Management System
-----------------------
A comprehensive system for managing students, teachers, and administrators
in a school environment. Demonstrates polymorphism through the Person class hierarchy.
"""

class Person(ABC):
    """
    Abstract base class for all persons in the school system.
    Implements common attributes and enforces implementation of role-specific methods.
    """
    def __init__(self, id: int, name: str, age: int, contact: str):
        self.id = id
        self.name = name
        self.age = age
        self.contact = contact
        self.date_joined = datetime.now()
    
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    @abstractmethod
    def get_details(self) -> str:
        pass

class Student(Person):
    """
    Student class representing a school student.
    Manages course enrollment, grades, and attendance.
    """
    def __init__(self, id: int, name: str, age: int, contact: str, grade: str):
        super().__init__(id, name, age, contact)
        self.grade = grade
        self.courses: List['Course'] = []
        self.attendance: Dict[str, bool] = {}
        self.grades: Dict[str, float] = {}
        self.extracurricular: List[str] = []
    
    def get_role(self) -> str:
        return "Student"
    
    def get_details(self) -> str:
        return f"Student: {self.name} (Grade {self.grade}) - GPA: {self.calculate_gpa():.2f}"
    
    def add_extracurricular(self, activity: str) -> str:
        self.extracurricular.append(activity)
        return f"{self.name} has joined {activity}"
    
    def calculate_gpa(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class Teacher(Person):
    """
    Teacher class representing a school teacher.
    Manages courses taught and student assessments.
    """
    def __init__(self, id: int, name: str, age: int, contact: str, subject: str):
        super().__init__(id, name, age, contact)
        self.subject = subject
        self.courses: List['Course'] = []
        self.specializations: List[str] = []
    
    def get_role(self) -> str:
        return "Teacher"
    
    def get_details(self) -> str:
        return f"Teacher: {self.name} (Subject: {self.subject})"
    
    def grade_student(self, student: Student, course_name: str, grade: float) -> str:
        student.grades[course_name] = grade
        return f"Graded {student.name} with {grade} in {course_name}"

class Course:
    """
    Course class representing an academic course.
    Manages course content, students, and assignments.
    """
    def __init__(self, id: int, name: str, max_students: int):
        self.id = id
        self.name = name
        self.max_students = max_students
        self.students: List[Student] = []
        self.teacher: Teacher = None
        self.assignments: List[str] = []
        self.schedule: Dict[str, str] = {}  # day: time_slot

    def add_student(self, student: Student) -> str:
        if len(self.students) < self.max_students:
            self.students.append(student)
            student.courses.append(self)
            return f"{student.name} enrolled in {self.name}"
        return f"Course {self.name} is full"

class School:
    """
    School class representing the main school entity.
    Manages all persons and courses in the school system.
    """
    def __init__(self, name: str):
        self.name = name
        self.people: List[Person] = []
        self.courses: List[Course] = []
        self.events: List[str] = []

# Example usage with realistic data
if __name__ == "__main__":
    # Initialize school
    school = School("Highland Secondary School")

    # Create students with realistic data
    students = [
        Student(1, "Ian Matthews", 15, "ian.m@email.com", "10th"),
        Student(2, "Sarah Connor", 16, "sarah.c@email.com", "11th"),
        Student(3, "Michael Chen", 15, "mike.c@email.com", "10th"),
        Student(4, "Jessica Williams", 17, "jess.w@email.com", "12th"),
        Student(5, "Joseph Rodriguez", 16, "joe.r@email.com", "11th")
    ]

    # Create teachers
    teachers = [
        Teacher(101, "Dr. James Wilson", 45, "j.wilson@highland.edu", "Physics"),
        Teacher(102, "Ms. Emily Parker", 38, "e.parker@highland.edu", "Mathematics"),
        Teacher(103, "Mr. Robert Brown", 42, "r.brown@highland.edu", "Literature")
    ]

    # Create courses with realistic names
    courses = [
        Course(1, "Advanced Physics", 30),
        Course(2, "Calculus 101", 25),
        Course(3, "World Literature", 35)
    ]

    # Add extracurricular activities
    activities = ["Basketball Team", "Chess Club", "Debate Society", "Science Club"]
    for student in students:
        activity = random.choice(activities)
        print(student.add_extracurricular(activity))

    # Enroll students in courses and assign grades
    for student in students:
        school.people.append(student)
        for course in courses:
            if random.random() > 0.3:  # 70% chance of enrollment
                print(course.add_student(student))
                # Assign random grades
                grade = random.uniform(65.0, 98.0)
                print(f"Grade for {student.name}: {grade:.2f}")
                student.grades[course.name] = grade

    # Print school statistics
    print("\n=== Highland Secondary School Statistics ===")
    print(f"Total Students: {len([p for p in school.people if isinstance(p, Student)])}")
    print(f"Total Teachers: {len([p for p in school.people if isinstance(p, Teacher)])}")
    print("\n=== Student GPAs ===")
    for student in students:
        print(f"{student.name}: {student.calculate_gpa():.2f}")