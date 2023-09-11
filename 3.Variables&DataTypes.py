# variable : is like a container that holds data.

#INTEGER DATATYPE
number=7
print(number)#a is like a container and 1 is the content inside it

#STRING DATATYPE
name="dev"
print(name)

#BOOLEAN DATATYPE
human=True
print(human)

# NONE DATATYPE
clone=None
print(clone)

#---------------------------------------------------------------------

# Data Type : specifies the type of value that a variable holds.

a=13
print(a)
a1=234
print(a+a1)

#To check the datatype use---type()
print("The type of a is",type(a))
print(type(clone))
print(type(human))

# ---------------------------------------------------------------------

#Python Built-in Data types
# 1
b=complex(8-7)
print(b)

#2 Lists and tuple(explained ahead)
# List-colletion of different datatypes in order
list1=[8,2.3,[-4,5],["apple","banana"]]
print(list1)

# tuple- same thing,but cannot be changed,its IMMUTABLE
#TIPS:-
# Diff btn mutable and immutable,and which can be changed-
# think of mutable as mutation as a change,evolution and immutable cannot be changed
tuple1=(("parrot","Sparrow"),("lion","tiger"))
print(tuple1)


#DICTIONARY
# collection of key value pairs(ex-marks,student,age etc)
dict1={"Name":"Dev","age":20,"canDrive":True}
print(dict1)