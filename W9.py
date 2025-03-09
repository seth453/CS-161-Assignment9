# Part 1: Student 

print("*************PART 1*************\n")

class Student:

  #Use init to declare attriubtes
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  #Print the attributes
  def student_data(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Grade: {self.grade}")

#represent students as lists
student1 = Student('Raj', 16, '11th\n')
student2 = Student('Sam', 14, '10th\n')

#Print students data
student1.student_data()
student2.student_data()

print("*************PART 2*************\n")

# Part 2: Staff -> Teacher
class Staff:

  def __init__(self, name, dept, role, salary):
    self.name = name
    self.dept = dept
    self.role = role
    self.salary = salary

  def staff_data(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.dept}")
    print(f"Role: {self.role}")
    print(f"Salary: {self.salary}")

#The teacher class inherits Teacher attributes from the Staff class
class Teacher(Staff):

  def __init__(self, name, dept, role, salary, age): #Teachers uniqely have an age
    super().__init__(name, dept, role, salary) # Here we use super to call a method from the Parent class, Staff
    self.age = age

  def teacher_data(self):
    print(f"Age: {self.age}")


teacher1 = Teacher('Raj', 'Math', 'Teacher', '50,000', '30\n')
teacher2 = Teacher('Sam', 'Science', 'Teacher', '60,000', '40\n')

teacher1.staff_data()
teacher1.teacher_data()

teacher2.staff_data()
teacher2.teacher_data()

print("*************PART 3*************\n")

#Part 3: Square
class Square: 
  #Only attribute to modify is the side length
  def __init__(self, side):
    self.side = side

  #Perimeter is all the 4 sides added
  def perimeter(self):
    return self.side * 4 

  #Area is the side squared
  def area(self): 
    return self.side ** 2

#initialize two squares with given sides, 5 and 10 units
square1 = Square(5) 
square2 = Square(10) 

#print perimeter and area of each square
print("Square 1 has a side lenth of 5 ")
print("The Perimeter of square 1 is: ", square1.perimeter()) 
print("The Area of square 1 is: ", square1.area(),"\n") 

print("Square 2 has a side lenth of 10 ")
print("The Perimeter of square 2 is: ", square2.perimeter())
print("The Area of square 2 is: ", square2.area(),"\n")

