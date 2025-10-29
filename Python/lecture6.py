# def cal_len(list):
#     print(len(list))
    
# list = ["Ali", "Ahmad", "Aslam", "Tariq"]
# list2 = ["Lahore", "Isl", "Multan"]

# # cal_len(list)
# # cal_len(list2)

# def print_list(list):
#    for item in list:
#        print(item, end= " ")

# print_list(list)

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# n = int(input("Number:"))
# fact = cal_fact(n)
# print(fact)

# def caonvertor(usd_val):
#     pkr_val = usd_val * 83
#     print(usd_val, "USD = " , pkr_val, "Pkr ")

# caonvertor(104)
    

#Recursion

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
    
# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(3))
# print(fact(4))
# print(fact(5))


#practice
# def calc_sum(n):
#     if(n==0):
#         return n
#     else:
#         return n + calc_sum(n-1)

# print(calc_sum(5))

# def print_list(list,idx=0):
#     if(idx == len(list)):
#         return
#     else:
#         print(list[idx])
#         print_list(list, idx+1)
        
# list = [1,2,3,4,5]
# print_list(list)