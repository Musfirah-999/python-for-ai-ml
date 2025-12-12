# f = open("practice.txt", "w+")
# f.write("Hi everyone \nwe are learning File I/O\n using java \nI like programming in Java")
# f.close()

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone....")

# with open("practice.txt", "r") as f:
#    data= f.read()
# new_data = data.replace("Java", "Python")  
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#            print("Not found")

# def check_for_line():
#     word = "pyq"
#     data = True
#     line_no = 1
#     with open ("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                print(line_no) 
#             line_no +=1
#             return
#     return -1

# print(check_for_line())


count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
    
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num+=data[i]
    
    
    nums = data.split(",")
    print(nums)
    
    for val in nums:
        if(int(val)%2 == 0):
            count +=1
print(count)
        
        