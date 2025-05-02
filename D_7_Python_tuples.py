# Day_7 Python_from_Scratch
# Tuples
print("Tuples are immutable lists.As List is mutable , but tuples are immutable.")
print("Tuples are represented as Var_name=() and the values seperated by comma in the () braces are counted as a single element each.")
tup_1=("Pragati","Pratibha","Akanksha","Chitra")
print("Say the tuple named tup_1 =",tup_1)
print("The tuple also allows Indexing and slicing as Lists.")
print("An empty tuple is created as - var=() or var=tuple()")

# Indexing in tuple :

print("The indexing is done as :")
print("\t\tPragati\tPratibha\tAkanksha\tChitra")
print("\t\t   0   \t    1   \t    2   \t   3")
print("\t\t  -4   \t   -3   \t   -2   \t  -1")
print("Accessing Elements using Index as - ")
print("tup_1[0] is",tup_1[0],"\ntup_1[2] is",tup_1[2])
print("tup_1[-3] is",tup_1[-3],"\ntup_1[-1] is",tup_1[-1])

# Slicing in List -

print("Slicing in tuple is similar to slicing in Lists.")
print("We can access a part of Tuple using slicing using List-name[Starting Index : Ending index].\nThe ending index is excluded.")
print("For example -\ntup_1[0:2] is :",tup_1[0:2])
print("tup_1[-3:-1] is :",tup_1[-3:-1])
print("If any index is not available in slicing, the terminal value is default.")
print("tup_1[:3] is :",tup_1[:3])
print("tup_1[1:] is :",tup_1[1:])

# Methods of Tuples :
print("As tuples are immutable so functions that modify the values in tuples are not applicable.")
print("Functions like \n1) count(arg)\n2) index(arg)etc.\nWorks similar as Lists.")