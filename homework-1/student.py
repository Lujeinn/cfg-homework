"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()



class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation):
        super(CFGStudent, self).__init__(name, age, id)
        self.specialisation = specialisation

    def add_subject(self, new_subject, grade):
        self.subjects.update({new_subject: grade})
        print(f"{self.name} has enrolled in the {new_subject} subject. Her new grade is {grade}.")

    def remove_subject(self, old_subject):
        self.subjects.pop(old_subject)
        print(f"{self.name} has been removed from the {old_subject} subject.")

    def view_all_subjects(self):
        print(f"{self.name} is taking the following subjects:")
        for subject in self.subjects:
            print(subject)

    def overall_grade(self):
        total_grade = sum(self.subjects.values())
        number_of_subjects = len(self.subjects)
        average_grade = total_grade / number_of_subjects
        return average_grade


#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

my_student = CFGStudent("Lujein Nouelaty", 32, 4567, "Software")
my_student.add_subject("Python", 52)
my_student.add_subject("SQL", 68)
my_student.remove_subject("SQL")
my_student.view_all_subjects()
print(my_student.overall_grade())
