# Day_4 Python_from_Scratch
# Strings

print("Strings - ")
print("So Basically , A string is a collection of Characters.\nPython doesn't have char datatype.")
print("So whatever is written in between Single quotes(\'\') and double quotes(\"\") is a string.")
print("A string is immutable , i.e we cannot modify a string in itself.")
str="Hey , This is Day_4 of python."
print("Here the Variable str stores the String",str)
print("Also , triple quotes are use to store String:")
str_1='''Hi Everyone , I'm Prabhat , Learning python from "Scrimba".'''
print("The triple quotes is generally  used when the string has multiple quote statements , it don't requires escape Statements :\n",str_1)
print("Also , Triple quotes allows to write in multiple Lines.")
str_2='''HI !
        Everyone 
        This is Python.'''
print("eg. : ",str_2)

# Indexing in Python

print("\nPython Strings supports Indexing starting from 0 till length of \(String -1.\)")
print("Also , the last Char of string has an index of -1 and rest in decreasing order towards left like -2 -3 ...")
print("Example :")
str_3="Python"
print("In string str_3 i.e :",str_3)
print("Has index like \n\t\t P\t y\t t\t h\t o\t n")
print("\t\t 0\t 1\t 2\t 3\t 4\t 5")
print("\t\t-6\t-5\t-4\t-3\t-2\t-1")
print("Acessing characters by index : ")
print("We can access characters by their indexes using String[index] , eg. in str_3- str_3[0] is :",str_3[0])
print("also , str_3[-1] is :",str_3[-1])

# String Slicing in Python.

print("\nString Slicing :")
print("String Slicing is used to access substrings of a given string.")
print("We us colon \':\' to slice the string.Done as string[starting index : ending index]")
print("For example : in str_3 the str_3[0:3] is -",str_3[0:3])
print("Also , str[-3:-1] is -",str_3[-3:-1])
print("if any index is null in slicing , it means terminal index of that side.")
print("For example - str_3[:3] is-",str_3[:3],"and str[3:] is-",str_3[3:])
print("We can also reverse a string using slicing method as String[::-1] \neg. str_3[::-1] is ",str_3[ : :-1])
print(" del can be used to delete a String. as - del string.")

# String methods in Python 

print("\n\n\t\t\tString Methods :\n")
print("String methods are predefined functions that makes tasks easy. Some commonly used methods are :")
print("\ta) The len() method rteurn the length of the String. Eg. len(String)")
str_4 = "Strings in Python"
print("\tThe length of str_4 i.e :",str_4,"is :",len(str_4),"\n")
print("\tb) The lower() and upper() methods are used to convert the string in lowercase and uppercase respectively.")
print("\tEg. str_4.lower() is :",str_4.lower(),"\n\t    str_4.upper() is :",str_4.upper(),"\n")
print("\tc)The title() method is used to capitalize the first letter of each sentence.")
print("\tEg. str_4.title() is :",str_4.title(),"\n")
print("\td)The count(arg_1) function is used to count number of substrings in a string.")
print("\tEg.  No. of \'t\' in str_4 is str_4.count(\"t\") i.e :",str_4.count("t"),"\n")
print("\te)The swapcase() method is used to swap the case of each letter of the string.")
print("\tEg.  Swapping the case of letter in str_4 is str_4.swapcase():",str_4.swapcase(),"\n")
print("\tf)The find(arg) method is used to find a substring in given string and it returns the first index of the substring.")
print("\tEg.  Finding the substring \"Python\" in str_4 is :",str_4.find("Python"),"\n")
print("\tg)The replace(arg1,arg2) method is used to replace a substring  by another substring in given string.")
print("\tEg.  Replacing the substring \"Python\" by \"Java\" in str_4 as str_4.replace(\"Python\",\"java\") :",str_4.replace("Python","Java"),"\n")

# String Formmating in Python.
print("String formatting in python :")
print("format(arg_1,arg_2,....) method is used to format the string. There are multiple ways to format a string :")
print("{} braces are used to format a string , it is replaced by the arguements of the format in order it is provided.")
print("For example : {} am a good boy".format("I"),"Here I is formatted using {} and .format(\"I\")")
print("\"{} is the {} {}\".format(\"Honesty\",\"best\",\"Policy\") is interpreted as -")
print("{} is the {} {}".format("Honesty","best","Policy"))
print("\nAlso we can reorder the agruements position by indexing the format specifier.")
print("\"{1} is the {2} {0}\".format(\"Honesty\",\"best\",\"Policy\") is interpreted as -")
print("{1} is the {2} {0}".format("Honesty","best","Policy"))
print("\nThere we can also use variables to store the substrings.The variables are placed in format specifiers and are replaced by corresponding arguements.")
print("For example - \"{l} is {k} \".format(k=\"Impossible\",l=\"Nothing\") is interpreted as -")
print("{l} is {k} ".format(k="Impossible",l="Nothing"))
print("\nFormat method is also used to convert different numbers in different forms like Binary , hexa etc.")
print("For example - \"{0:b}\".format(16) is interpreted as -")
print("{0:b}".format(16))
