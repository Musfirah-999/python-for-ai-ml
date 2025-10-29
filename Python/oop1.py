# class Student:
#     college_name = "ABC College"
#     def __init__(self):   #default constructor
#         pass
        
#     def __init__(self, name, marks):    #parameterized constructor
#         self.name = name
#         self.marks = marks
#         print("Student object created") 
    
#     def welcome(self):
#         print("Welcome to", self.college_name)
        
#     def get_marks(self):
#         print(self.marks)
    
    
# s1 = Student("Ahmad", 85)
# s1.welcome()
# print(s1.name, s1.marks)
# print(s1.college_name)
# s1.get_marks()

# s2 =Student("Sara", 90)
# print(s2.name, s2.marks)
# print(s2.college_name)
# s2.get_marks()

# class Car:
#     color = "blue"
#     brand = "mercedes"

# c1 = Car()
# print(c1.brand)
# print(c1.color)



#practice

# class Students:
    
#     # marks = []
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Student object created")
        
#     def get_avg(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print("Hi ", self.name, "Your total marks are:", sum)
#         avg = sum/len(self.marks)
#         print("Your average marks are:", avg)
        
#     @staticmethod   #now no need to add self as parameter
#     def print_hello():   #decorator
#         print("Hello Students")


# s1 = Students("Ali", [85, 90, 78])
# s1.name = "Ahmed"   
# s1.get_avg()

# s2 = Students("Aisha", [98, 99, 97])      
# s2.get_avg()



