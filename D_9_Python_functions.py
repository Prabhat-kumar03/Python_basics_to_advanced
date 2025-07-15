# Day_9 Python_from_Scratch
# Function
print("Functions is a block of statements that return the specific task.")
print("Functions are created using def keyword followed by function name and its parameters as:")
print(" def function_name(parameters):")
print("Python is indentation oreinted language , so all the lines under a function with same indent is a body of Function.")
print("for eg.\ndef print_name():\n\tprint(\"Michael\")\n is a function.")
def print_name():
    print("Michael")
print("So , a function doesn't work until it ios called , i.e called function calling.")
print("Now a function have some parameters , not necessarily.")
print("parameters are the values which are replaced by the arguements passed by the user.")
print("def fun_name(parameter):\n\t{Body_Staements}")
print("\n Arguements -")
print("Python aruements are the values passed inside the parenthesis of the fubnction.")
print("I python functions arguements are defined as 4 types:")
print("1) Default Arguements\n2) Keyword Arguement\n3) Positional Arguement\n4) Arbitrary Arguement")
print("1) Default Arguement :")
print("\tassumes a default value if a value is not provided in the function call for that argument.")
print("\tFor example-\n\tdef myFun(x, y=50):\n\t\tprint(\"x: \", x)\n\t\tprint(\"y: \", y)\n\tmyFun(10) will return")
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)
print("2) Keyword Arguement :")
print("\tIt specifies the arguements with values so that order of funtion need not to be remebered.")
print("\tFor eg.\n\tdef fun_1(fname,lname):\n\t\tprint(fname,lname)\n\tfun_1(lname=\"Scrimba\",fname=\"Python\") will result as :")
def fun_1(fname, lname):
    print(fname, lname)
fun_1(lname="Scrimba",fname="Python")
print("3) Positional Arguements :")
print("\tThe values are passed coressponding to their order of arguement.")
print("\tFor eg. -\tdef fun_2(name,age):\n\t\tprint(\"Name :\",name,\"Age :\",age)")
print("\tHere , the first agruement to be passed is always name , and the second arguement passed is considered as be age.")
print("\t like - fun_2(\"Deepak\",28) is interpreted as -")
def fun_2(name,age):
    print("Name :",name,"Age :",age)
fun_2("Deepak",28)
print("\tWhereas fun_2(28,\"Deepak\") will result in -)")
fun_2(28,"Deepak")
print("4) Arbitrary Arguement :")
print("\tIt can pass a variable number of arguments to a function using special symbols.")
print("\tThese special symbols are *argvs and **kwargs.")
print("\t*argv is used to pass variable length of arguement.")
print("\tExample :\n\tdef fun_3(*argv):\n\t\tfor arg in argv:\n\t\t\tprint(arg)\n\tfun_3(\"Ayush\",\"Ankush\",\"Prabhat\") will result as -")
def fun_3(*argv):
    for arg in argv:
        print(arg)
fun_3("Ayush","Ankush","Prabhat")
print("\n\t**kwargs is used for passing variable length keyword arguements :")
print("\tFor Example -\n\tdef fun_4(**kwargs):\n\t    for key, value in kwargs.items():\n\t\tprint(\"%s == %s\" % (key, value))")
print("\tfun_4(first=\'Geeks\', mid=\'for\', last=\'Geeks\')\n\tThis is interepreted as -")
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')

#  Return Statements :
print("As python functions are blocks of code that perform specific task.")
print("In order to get an output , a return statement is required to get an output rether than print.")
print("The return statement is like -\nreturn Expression")
print("For example -\n\tdef product(x,y):\n\t    return x*y\n\tprint(product(2,3))")
print("The above function has a return statement that returns the value x*y.\nOutpupt is :")
def product(x,y):
    return x*y
print(product(2,3))