#practice

# i = 1
# while i <=100:
#     print(i)
#     i+=1

# i = 100
# while i >=1:
#     print(i)
#     i-=1

# n = int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(n, " * " , i , " = ", i*n)
#     i+=1

# i = 1
# list=[]
# while i <= 10:
#     list.append(i*i)
#     i+=1
# print(list)

# list = [1,4,16,25,36,49,64,81,100]
# n = len(list)-1
# idx =0
# while idx<=n:
#     print(list[idx])
#     idx+=1


# tuple = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the number you want to search:"))
# i = 0
# while i<len(tuple):
#     if (tuple[i]== x):
#         print("Found at idx ", i)
#         break
#     else:
#         print("Finding...")
#     i+=1

# str = "Musfirah"
# for i in str:
#     print(i)
 
# list = [1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)
    
# tuple = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the number you want to search:"))
# idx = 0
# for i in tuple:
#     if i == x:
#         print("Found at idx ", idx)
#         break
#     else:
#         print("Finding...")
        
#     idx+=1

# for i in range(2,51,2):    #print even numbers
#     print(i)


# for i in range(100, 0, -1):
#     print(i)

# n = int(input("Enter number:"))
# for i in range(1, 11):
#     print(n, " * ", i, " = " , n*i )


# n = int(input("Enter number:"))
# i = 1
# sum = 0
# while i <=n:
#   sum = sum + i
#   i+=1
# print(sum)

n = int(input("Enter number:"))
fact = 1
for i in range(n,1,-1):
    fact*=i
print(fact)