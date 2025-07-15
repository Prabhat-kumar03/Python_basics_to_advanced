# Day_8 Python_from_Scratch
# Sets
print("\t\t\t Sets :")
print("Sets are unordered collection(No Indexing) of elements. Represented by var_name={} , and similar to list and tuples , each element is seperated by comma.")
print("It is much faster than List and Tuples.It is semi-immutable i.e we can,t change values , it can be only added or deleted.")
print("It is unordered i.e the items stored in sets don't have an order.")
set_1={"A","B","C","D"}
print("Let say if there's a Set set_1={\"A\",\"B\",\"C\",\"D\"} is shown as -\nset_1=",set_1)
print("Also set can store heterogeneous elements.")
set_2={"E","w","x","y","z"}
print("set_2 =",set_2)
print("An empty set is created as - var=set() not by \'var={}\'.")

# methods in Sets -

print("Sets are faster than list or tuples as it supports various methods :")
print("\t1) set.add() method is used to insert element to a Set.")
set_1.add("E")
print("\t   For example - set_1.add(\"E\") will return the set as -",set_1,"\n")
print("\t2) set.union(arg) method is used to obtain union of two or more sets.")
print("\t   Also the | operator is used for performing union operation")
print("\t   For example - set_1.union(set_2) will return the set as -",set_1.union(set_2))
print("\t   Also , set_1 | set_2 will return the same as :",(set_1|set_2),"\n")
print("\t3) set.intersection(arg) method is used to obtain intersection of two or more sets.")
print("\t   Also the & operator is used for performing intersection operation")
print("\t   For example - set_1.intersection(set_2) will return the set as -",set_1.intersection(set_2))
print("\t   Also , set_1 & set_2 will return the same as :",(set_1&set_2),"\n")
print("\t4) set.difference(arg) method is used to obtain difference of two or more sets.")
print("\t   Also the - operator is used for performing difference operation")
print("\t   For example - set_1.difference(set_2) will return the set as -",set_1.difference(set_2))
print("\t   Also , set_1 - set_2 will return the same as :",(set_1 - set_2),"\n")
print("\t5) set.symmetric_difference(arg) method is used to obtain symmetric_difference of two or more sets.")
print("\t   Also the ^ operator is used for performing symmetric_difference operation")
print("\t   For example - set_1.symmetric_difference(set_2) will return the set as -",set_1.symmetric_difference(set_2))
print("\t   Also , set_1 ^ set_2 will return the same as :",(set_1 ^ set_2),"\n")
print("\t6) set.clear() method is used to insert element to a Set.")
set_1.clear()
print("\t   For example - set_1.clear() will return the set_1 as -",set_1,"\n")