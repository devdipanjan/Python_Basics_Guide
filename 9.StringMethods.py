a="Dev"
print(len(a))
# Concept of Immutability(can't be changed inplace)
# STRINGS ARE IMMUTABLE
# upper():
#isupper():
print(a.upper())

# lower():
print(a.lower())

# rstrip():
b="dev!!!!!!!!!!!!!!!!!"
print(b.rstrip("!"))#Strips the ! 

# replace():
print(a.replace("Dev","Zoro"))

# split():
c="Luffy Zoro Sanji Nami Ussop"
print(c.split(" "))#Lists accordingly

# capitilize():
#first letter of a sentence will be in block
blogHead = "introduction to python"
print(blogHead.capitalize())

# center():
# moves the description to the center

str1 = "Welcome to the Console"
print(len(str1))
print(len(str1.center(50)))

# count():
#counts number of times string occurs
print(a.count("Dev"))

# endswith():
str2 = "Dev !!!"
print(str2.endswith("!!!"))
print(str1.endswith("to",4,10))

#startswith():
print(str2.startswith("Dev"))



# find():
str3 = "he's name is dan.He is an honest man"
print(str3.find("is"))#Will find according to index and stop when 10 appears

# Index():
#Raises an exception
print(str1.find("ishh"))#returns -1 coz there's no ishh
#print(str1.index("ishh"))

# isalnum():
 #Checks alpha numerical (A-Z,a-z,0-9) else false
str4 = "WelcomeToTheConsole"
print(str4.isalnum())

# isalpha():
# same as alnum if only its consists A-Z,a-z then true
str5 = "Welcome555"
print(str5.isalpha())

# islower():
str6 = "Hello World"
print(str6.islower())

#isprintable():
str7 = "I am a cat\n"
print(str7)
print(str7.isprintable())#false coz \n can't be executed

# isspace():
str8 = "       "#using space
print(str8.isspace())
str9 = "        "#using tab
print(str9.isspace())

# istitile():
str10 = "To kill a Mocking Bird"
print(str10.istitle())#false

# swapcase():
str13 = "Python is an Interpretted Language"
print(str13.swapcase())#swaps lower to upper and vice versa

# title():
print(str13.title())#all first characters become capital
