#TYPE ERROR : The function requires the specific datatypes , if not it gives the type error
# len(12345) throws error because len needs string not integer
print(len("Hello"))

#TYPE CHECKING : To check which data type does it have or is of
print(type("Hello"))
print(type("123456"))
print(type(12345))
print(type(5.12365))
print(type(True))

# TYPE CONVERSION : To convert one datatype in to another

string_name = "123" #this is string type
int_type = int(string_name)
print(type(int_type))

#TASK : print("Number of letters in your name: " + len(input("Enter Your Name"))) : Correct this code.
print("Number of letters in your name: " + str(len(input("Enter Your Name: "))))
