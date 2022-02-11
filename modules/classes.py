# class is collection of attribute and methods
# variable:
# instance variable : any variable start with self
# static variable : class variable access using class name
# local variable : method variable

class Student:
    # static variable
    college = 'USC'

    # constructor: use to initialize instance variable
    # when class object is created this method call
    def __init__(self, name, rollNum, marks):
        self.name = name
        self.rollNumber = rollNum
        self.marks = marks
        # inside constructor
        # Student.college = 'USC'

    def __str__(self):
        return 'This is Student Class'

    # instance method: argument must start with self follow by other argument
    def displayStudentData(self):
        teacher = 'Dona'  # local variable
        print('Student Name:', self.name)
        print('Student RollNumber:', self.rollNumber)
        print('Student Marks', self.marks)
        print('Student Teacher', teacher)
        print('Student College', Student.college)


# create a reference object of student

# stdt = Student('Mike', 101, 87)
# stdt1 = Student('John', 102, 84)

# print('name', stdt.name)
# print('marks', stdt.marks)
# print(stdt.displayStudentData())
# print(stdt1.displayStudentData())

# insted of using multiple object created list of students
listStudents = [Student('Mike', 101, 87), Student(
    'John', 102, 84), Student('Andrew', 103, 91)]

for student in listStudents:
    student.displayStudentData()
