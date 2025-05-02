# Day_3 Python_from_Scratch
#Data types 
print("Data types in python :\n")
print("In python there  are various data types in python :\n")
print("1. Numeric\nThis data type is used to store different types of numbers.")
print("\ta)Integers : All the whole numbers and integers.")
a=10
print("\t a =",a,"belongs to data type class ",(type(a)),"\n")
print("\tb)Float : All the floating or decimal numbers")
b=10.45
print("\t b =",b,"belongs to data type class ",(type(b)),"\n")
print("\tc)Float : All the complex or imaginary")
c= 4 + 5j
print("\t c =",c,"belongs to data type class ",(type(c)),'\n')
print("2.Dictionary\nThis data type is used to store key value pairs.Represented in a {} braces")
dict={1:"Prabhat",2:"Ayush",3:"Ankush",4:"Vivek",5:"Monu"}
print("dictionary : ",dict," has a data type ",type(dict),'\n')
print("3.Boolean\nThis data type is used to store True/False values.")
bool = True;
print("bool -",bool,"has a data type of",type(bool),"\n")
print("4.Set\nThis data type is used to store unordered collection has nop duplicate items.[Mutable]")
set={"Hi","Hello","HI","hi","Hi","HellO"}
print("Set \'set\' is-",set,"has a data type of",type(set),"\n")
print("5.Sequence\nThis data type is used to store iterable items in a variable.")
print("\ta)String : used to store sequence of characters.[Immutable]")
str = "Welcome to Day_3 of Python."
print("\t Uses Single or double quotes to store the string.\n\tHere the string Str is :\'",str,"\' have a data type:",(type(str)),"\n")
print("\tb)Tuple : used to store sequence of items of different data types.() braces are used to store and values are seperated using ,.[Immutable]")
tup=("A","B",1,2,3)
print("\t Tuple tup :",tup,"have a data type:",(type(tup)),"\n")
print("\tc)List : used to store sequence of items of different data types.[] braces are used to store and values are seperated using ,.[Mutable]")
List=["Sohan","Mohan",4,5,6]
print("\t List \'List\' :",List,"have a data type:",(type(List)))