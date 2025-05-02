#Day_15 Python_from_Scratch
# Dictionaries :

print("\t\t\t Dictionaries :")
print("Dictionaries are datatypes used to store key-value type of data, where a unique key defines a value.")
print("It is ordered, and mutable.Dictionaries are written with curly brackets, and have keys and values.")
print("For example :\nDict_1={1:\"a\",2:\"b\",3:\"c\"}\nprint(Dict_1)")
print("Output:")
Dict_1 = {1:"a",2:"b",3:"c"}
print(Dict_1)

#Accessing the Keys and Values :

print("Accessing the Elements:")
print("1) We can access values using Keys:")
print("For Example:\nprint(Dict_1[2])\nOutput:",Dict_1[2])
print("\n2) We can also access value using get method as dict.get(key) will return value.")
print("for Example :Dict_1.get(3)\nOutput :",Dict_1.get(3))
print("\n3) We can get a List of Key pairs using keys method as dict.keys()")
print("For Example : print(Dict_1.keys())\nOutput :",Dict_1.keys())
print("\n4) We can get a List of value pairs using keys method as dict.values()")
print("For Example : print(Dict_1.values())\nOutput :",Dict_1.values())
print("\n5) We can get a List of items using keys method as dict.values()")
print("For Example : print(Dict_1.items())\nOutput :",Dict_1.items())

# Modifying items in a dictionary :

print("1) We can update a value using its key as dict[key]=\"new value\".")
print("For example :Dict_1[3]=\"C\"\nprint(Dict_1)\nOutput :")
Dict_1[3]="C"
print(Dict_1)
print("2) We can also add Values using new Keys and value as dict[new_key]= newValue")
print("For Example:\nDict_1[4]=\"D\"\nprint(Dict_1)\nOutput :")
Dict_1[4]="D"
print(Dict_1)
print("3) We can also add or update Values using new Keys and value using update method as dict.update({key : Value})")
print("For Example:\nDict_1.update({5:\"E\"})\nprint(Dict_1)\nOutput :")
Dict_1.update({5:"E"})
print(Dict_1)
print("Also we can update a dictionary with the values of another dictionary using this function.")
Dict_2={"Sunday":"D_1","Monday":"D_2","Tuesday":"D_3"}
print(Dict_2)
print("Updating Dict_1 with Dict_2 , as Dict_1.update(Dict_2)\nprint(Dict_1)")
Dict_1.update(Dict_2)
print(Dict_1)

# removing items from a dictionary :

print("1) We can remove a key-value using pop method as dict.pop(key)")
print("For example :Dict_1.pop(3)\nprint(Dict_1)\nOutput :")
Dict_1.pop(3)
print(Dict_1)
print("2) We can Also remove a key-value using del method as del dict[key]")
print("For example : del Dict_1[4]\nprint(Dict_1)\nOutput :")
del Dict_1[4]
print(Dict_1)
print("3) Clear method is used to clear all the items in a dictionary.")
Dict_1.clear()

# Updating a dictionary with multiple dictionaries : 

Dict_3={}
print("Say there's a dictionary Dict_3 and we have to add all the elements from Dict_1 and Dict_2 :")
print("for groups in (Dict_1,Dict_2) : Dict_3.update(groups)")
for groups in (Dict_1,Dict_2) : Dict_3.update(groups)
print("Dict_3 =",Dict_3)
# The unpacking method
print("Another way to update a dictionary with items of other dictionaries is unpacking method :")
print("var_dict = {**dict_1,**dict_2,....}")
