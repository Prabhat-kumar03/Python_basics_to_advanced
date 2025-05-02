#Day_12 Python_from_Scratch
# While Loop

print("Loops are repeatitions of the same task or work for desired number of times.")
print("So a loop is a repeatition of task for multiple times.Python has While and for loops.")
print("The \"While loop\" is used for iterating a task desired number of times.")
print("Syntax :\n\twhile (condition):\n\t    body of while loop/Task\n\t    iterator/updation")
print("For Example : To print Hello 5 times , we can use a while loop:")
print("while(number_of_times<=5):\n    print(\"Hello\")\n    number_of_times+=1\n will result as:")
number_of_times=1
while number_of_times<=5 :
    print("Hello")
    number_of_times+=1
print("Printing Pattern of Stars and numbers are best example of usin g Loops.")
print("Printing the patterns provides the crux of how loops work.")

# Patterns Using While Loop :
print("Here are few common known patterns :[Using While loop ]")
print("Half pyramid pattern:(height=5)")
print("a)Right Half Pyramid :")
height=5
i=0
while i<height :
    print("*"*(i+1))
    i+=1
print("\nb)Left Half Pyramid :")
i=0
while i<height :
    print(" "*(height-i-1)+"*"*(i+1))
    i+=1
print("\nc)Reverse left half Pyramid :")
i=0
while i<height :
    print(" "*i + "*"*(height-i))
    i+=1
print("\nd)Reverse right half Pyramid :")
i=0
while i<height :
    print("*"*(height-i))
    i+=1
print("\nFull or Complete Pyramid :")
i=0
while i<height :
    print(" "*(height-i-1)+"*"*(2*i+1))
    i+=1 
print("\nReverse Full Pyramid :")
i=0
while i<height :
    print(" "*i + "*"*(2*(height-i)-1))
    i+=1
print("\nThese patterns tells us about the functioning of While Loop.")