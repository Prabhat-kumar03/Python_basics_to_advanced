# Day_10 Python_from_Scratch
# Compare and Booleans 

print("Python also supports operators relational operators.")
print("These operators are used to compare between entities.The result of comparison generally is a boolean value i.e True or False.")
print("These are as follows :")
print("1. Equal operator (==)")
print("\tThis operator is used to compare if two entities(value) are equal or not.")
a=10
b=10
print("\tEg. if a=10 , b=10 then a==b will return :",a==b)
print("2. Not Equal Operator (!=)")
print("\tThis operator is used to check if two entities are not Equal.")
print("\tEg. if a=10 , b=10 then a!=b will return :",a!=b,"as a equal to b.")
print("3. Greater than operator (>)")
print("\tThis opereator is used to check whether the entity at L.H.S is greater than the entity at R.H.S.")
c=23
print("\tEg. c=23 and a=10 , so c>a will return :",c>a,"\n\twhereas a>c will return :",a>c)
print("4. Less than operator (<)")
print("\tThis opereator is used to check whether the entity at L.H.S is less than the entity at R.H.S.")
print("\tEg. c=23 and a=10 , so c<a will return :",c<a,"\n\twhereas a<c will return :",a<c)
print("5. Greater than or equal to operator (>=)")
print("\tThis opereator is used to check whether the entity at L.H.S is greater than or equal to the entity at R.H.S.")
print("\tEg. b=10 and a=10 , so b>=a will return :",b>=a,"\n\twhereas a>=c will return :",a>=c)
print("6. Less than or equal to operator (<=)")
print("\tThis opereator is used to check whether the entity at L.H.S is less than or equal to the entity at R.H.S.")
print("\tEg. b=10 and a=10 , so b<=a will return :",b<=a,"\n\twhereas c<=a will return :",c<=a)

# is and is not operators 

print("is and is not operators in Python are used to check if the objects are same. The objects have same id in memory.")
print(" id() method is used to check the location in memory.")
num_1 = 10
num_2 = 10
print("Here two numbers assigned with same values num_1 = 10 and num_2 = 10 have adresses in memory as :")
print("id(num_1) =",id(num_1),"\nid(num_2) =",id(num_2))
print("is operator : Tells us about if the object is same.")
print("\tEg. Here a is b will return :",(a is b));
list_1 = []
list_2 = []
list_3 = list_1
print("Here list_1 and list_2 are two empty list created seperately and another variable list_3 is assigned with list_1.")
print("then,\n\tlist_1 is list_2 :",list_1 is list_2)
print("\tlist_3 is list_1 :",list_3 is list_1)
print("is not operator : Tells us about if the object is different.")
print("\tEg. Here a is not b will return :",(a is not b));
tup_1=("Hi","Hello")
tup_2=("Hello","Hi")
tup_3=tup_1
print("Here tuples \ntup_1 =",tup_1,"\ntup_2",tup_2,"\ntup_3 = tup_1")
print("id(tup_1) =",id(tup_1),"\nid(tup_2) =",id(tup_2),"\nid(tup_3) =",id(tup_3))
print("tup_1 == tup_2 : ",tup_1==tup_2)
print("tup_1 is tup_2 : ",tup_1 is tup_2)
print("tup_1 is not tup_2 : ",tup_1 is not tup_2)
print("tup_1 is tup_3 : ",tup_1 is tup_3)
