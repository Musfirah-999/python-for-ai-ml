info = {
    "key": "value",
    "name" : "Musfirah",
    "surname": "Zain",
    "subjects": ["DSA", "LA", "CN"],
    "topics": ("Dic", "Sets"),
    "age": 35,
    "is_adult" : True,
    "Marks": 98.0

}

# print(info)
# print(info["name"])
# print(info["topics"])
# print(info["subjects"])

# info["age"] = 20
# info["learning"]= "Python"
# print(info)

# null_dict= {}
# print(null_dict)


#nested dic
student = {
    "name": "Ali",
    "subjects":{
        "Chemisrty": 98,
        "Math": 100,
        "Physics": 91
    }
}
# # print(student)
# # print(student["subjects"])
# print(student["subjects"]["Math"])


#Methods
# print(list(student.keys()))
# print(len(student))
# print(list(student.values()))  #return list of values 
# print(student.items())   #return all key:value pair in the form of tuples
# pairs = list(student.items())
# print(pairs[0])  #tuple

# print(student["name"])   #may give error
# print(student.get("name"))  #return key acc to value
# student.update({"city":"Lahore"})

new_dic= {"city":"Lahore", "name": "Zain"}
student.update(new_dic)
print(student)




