class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__grades = []

    def add_grades(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added for {self.name}")
        else:
            print("\nInvalid Grade.Grade should be between 0 to 100\n")

    def get_average(self):
        if len(self.__grades) > 0:
            avg = sum(self.__grades) / len(self.__grades)
            return avg
        else:
            return 0

    def display_info(self):
        print(f"-------Student Information----")
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age}")
        print(f"\tGrades: {self.__grades}")
        print(f"\tAverage: {self.get_average()}")


student1 = Student("John", 25)
student1.display_info()
student1.add_grades(15)
student1.add_grades(100)
# student1.__grades.append(-100)
# student1.__grades.append(20)
student1.display_info()

