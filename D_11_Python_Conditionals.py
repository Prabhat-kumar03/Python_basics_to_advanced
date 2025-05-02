# Day_11 Python_from_Scratch
# Conditonal : If Elif Else 

print("Conditional statements :\n\tThese are statements where decisions are required to perform task.")
print("\t In python , there are If , Else and Elif statements used for decision making.")
print("if statement is given with an expression , if the expression is true , the if body is executed.")
print("else statement is the complementary of the if statement , i.e if expression is false , else statement is executed.")
print("elif comes when there are multiple conditons , the elif are the other conditions of the expression , if it does true , then elif is executed.")
print("\nSee an example :\nif(age < 18 ):\n    print(\"Underage\")")
print("else :\n    print(\"Eligible to vote\")")
print("So if age is less than 18 , it will print Underage otherwise it will print Eligble to Vote.\n Say age = 16 :")
age =16
if(age<18):
    print("Underage")
else:
    print("Eligible to Vote")
print("If there's only a single if statement , so if the expression is true , the body of if is executed otherwise it is skipped.")
print("Elif statement :")
print("When there are multiple conditions , then elif is used.")
print("For example ,Classify Classes as Primary,Secondary,Higher Secondary as class level 1-5 , 6-8 , 9-10 :")
print("if(class<=5):\n    print(\"Primary\")\nelif(class<9 and class>5):\n    print(\"Seconadry\")\nelse:\n    print(\"Higher Secondary\")")
Class = int(input("Enter the class level student belong : "))
if(Class<=5):
    print("Primary")
elif(Class>5 and Class<9):
    print("Secondary")
else :
    print("Higher Secondary")

# Nested if :

print("In case of multiple cases or subcases in a decision statement , then Nested if is used.")
print("Nested if is nothing but an if or condtional statement under an if or conditional Statement.")
print("For ex. ")