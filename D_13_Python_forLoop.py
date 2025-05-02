#Day_13 Python_from_Scratch
# For Loop

print("For loop is also an easy way for repeating a task. This is more adequate than While loops.")
print("For loop is used to iterate different types of sequences like List, tuples, sets, strings etc.")
print("Syntax is quite easy as \nfor variable in Iterator:\n____[Body]")
print("Example:\nfor x in \"Python\":\n    print(x)")
print("The output is as :")
for x in "Python" :
    print(x)
print("Similarly , we can traverse and perform operations on other sequence data type.")
print("break statement is used to break out or quit the loop.")
print("For Example:\nfor i in [\"a\",\"b\",\"c\"]:\n    if(i==\"b\"):\n\tbreak\n    print(i)")
print("This will result in :")
for i in ["a","b","c"] :
    if(i=="b"):
        break
    print(i)
print("Continue is used to skip a part, in case the part of body is not executed and continued to the next loop.")
print("The range function range() is used to pass through a range of integers.")
print("if a Single arguement is passed , then range is from 0 to arguement - 1.")
print("If two arguements are passed ,then !st number is starting and 2nd number is Ending range.(Ending is always excluded).")
print("If three numbers are passed , then it 1st no . is Starting , 2nd is ending and 3rd is interval or gap number.")
print("For Example :\nfor i in range(5):\n    print(i)")
print("this will result in :")
for i in range(5):
    print(i)
print("for i in range(5,10):\n    print(i)")
print("this will result in :")
for i in range(5,10):
    print(i)
print("for i in range(5,10,2):\n    print(i)")
print("this will result in :")
for i in range(5,10,2):
    print(i)