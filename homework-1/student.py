"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id, tutor):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
        self.tutor = tutor


class CFGStudent:

    def __init__(self, full_name, specialisation, season, mark=True):
        self.full_name = full_name
        self.specialisation = specialisation
        self.season = season
        self.mark = 70 if mark else 50

    def add_subject(self):
        print(f"{self.full_name} completed the {self.specialisation} cohort and achieved {self.mark}%.")

    def remove_subject(self):
        print(f"{self.full_name} was removed from the {self.specialisation} cohort because she was only getting {self.mark} in all her homework!")

    # def view_all_subjects(self):

student_1 = CFGStudent("Lujein Nouelaty", "Software", "Autumn", True)
student_1.add_subject()
# for student_mark in sum(70):
#     student_1.remove_subject()


#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
