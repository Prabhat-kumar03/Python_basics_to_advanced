# Day_6 Python_from_Scratch
# Split and Joins
print("Split and joins are methods to split and join iterative items.")
msg="This is DAY_6 of python."
print("The split(arg) method splits the sequence data types into List of elements.")
print("msg =",msg)
print("if nothing is passed the a single whitespace is default agrguement for this method.")
print("For example -\nmsg.split() returns :",msg.split())
print("otherwise , the split will configure the arguement to seperate the elements in a list.")
print("For example -\nmsg.split(' ') returns :",msg.split(' '))
csv='Eric,Lorem,John,Terry,Graham'
print("csv =",csv)
print("csv.split(\',\') is :",csv.split(','))
print("\njoin(arg) method is used to join elements of a iterative List")
List_1=["a","b","c"]
print("List_1 =",List_1)
print("\'-\'.join(List_1) is :",'-'.join(List_1))
print("Joining and splitting the dataset.:")
statement = "Sneha has completed her course"
print("For example , the String Statement is :",statement)
print('-'.join(statement.split()))