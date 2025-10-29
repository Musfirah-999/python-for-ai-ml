# str1= "This is a string.\n We are creating it in python."
#   \n is escape sequence chharacter

#operations 

# 1. concatination
# str1 = "apna "
# str2= "college"
# final = str1 + str2
# print(final)

# 2. length
# len(str1)
# len(final)
# print(len(final))

# 3. Indexing
# str = "Apna College"
# str[0] = A
# ch = str[2]
# print(ch)

# 4. Slicing
# Accessing parts of a string
# str = "ApnaCollege"
# print(str[0:4])
# print(str[4:len(str)])
# print(str[4:])

# 5. Negative index slicing
# str = "Apple"
# print(str[-3:-1])
# print(str[-5:-2])

#Functions 
# 1. Endswith 
# str = "I am watching Apna College python tutorial. "
# print(str.endswith("l. "))

# 2. Capitalize
# str = "i am watching Apna College python tutorial. "
# str = str.capitalize()
# print(str) 

# 3. Replace
# print(str.replace("python", "C++"))
# print(str)

# # 4. find
# print(str.find("Apna"))


# print(str.count("Apna"))


#Practice 

# n = input("Enter your name: ")
# print("You entered: ",n)
# print("the length of your name is ", len(n))

# s = input("enter ")
# print(s.count("$"))

#Conditions

# marks = int(input("Enter yur marks: "))

# if(marks > 90):
#     grade = "A"
# elif(marks > 80 and marks <=90):
#     grade = "B"
# elif(marks > 70 and marks <=80):
#     grade = "C"
# elif(marks > 60 and marks <=70):
#     grade = "D"
# else:
#     grade = "F"
# print("Your grade: ", grade)
    

#practice

# n = int(input("ENter number:"))

# if(n%2 == 0):
#     print("Even")
# if(n%2 == 1):
#     print("Odd")

a = int(input("ENter number1:"))
b= int(input("ENter number2:"))
c = int(input("ENter number3:"))

if(a>b and a>c):
    print(a)
elif(c>b and c>a):
    print(c)
elif(b>c and b>a):
    print(b)