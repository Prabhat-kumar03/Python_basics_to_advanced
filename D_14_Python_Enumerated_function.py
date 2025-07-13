#Day_14 Python_from_Scratch
# Enumerated Function

print("There's a function enumerated that is used to mark or number elements inside a iterable like List, tuple, set etc.")
print("enumerate(arguement) is the syntax form to enumerate any iterative data type.")
print("For example , if we want to numerate the elements of a list , we can use :")
num=0
list_1=["a","b","c"]
print("for i in list:\n    print(num,i)\n    num+=1")
for i in list_1:
    print(num,i)
    num+=1
print("or using the enumerator method , we get :")
print("for item in enumerate(list_1):\n    print(item)")
for item in enumerate(list_1):
    print(item)
print("Also ,enumerating a sequence item with desired number , we can mention number in Arguements of Enumerate function :")
print("for example :\nfor item in enumerate(list_1,21):\n    print(item)\nwilll result in enumerating the items with an index of given input.")
for item in enumerate(list_1,21):
    print(item)
print("Also :\nfor index,item in enumerate(list_1):\n    print(index,item)\nOutput :")
for index,item in enumerate(list_1):
    print(index,item)