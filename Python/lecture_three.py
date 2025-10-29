# marks = [89, 90, 54, 67, 86]
# print(type(marks))
# print(len(marks))

# # students = ["Ali", 50, 10, "Ahmad", 60, 10]
# # students[2] = 11
# # print(students)
# mark = marks[1:3]
# mark = marks[:3]
# print(mark)
# mark = marks[-4:-1]
# print(mark)
# marks.append(89)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)


# list = [2,4,1,5,7,3,9]
# # list.reverse()
# list.insert(1,5)    #(index, value)
# list.pop(3)
# print(list)


# ==========TUPLE============

# tup = (1,4,7,3,2,8,6)
# tup = ()
# tup = (1, )
# print(type(tup))
# print(tup)
# print(tup.count(1))
# print(tup.index(1))
# print(tup.index(1))
# print(tup[1:3])


#=========PRACTICE=========
# movies = []
# for i in range(3):
#     m= input("Enter your fav movie:")
#     movies.append(m)
# print("Yor fav movies are ",movies)

list = [1,2,3,5,2,1]

copy = list.copy()
copy.reverse()
if(copy == list):
    print("List is palindrome")
else:
    print("List is not palindrome")
