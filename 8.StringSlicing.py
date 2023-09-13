#Length of a String
fruit = "Pineapple"
len1 = len(fruit)
print("Pineapple is a",len1,"letter word.")

#String as an Array
# String Slicing
print(fruit[0:4]) #Python will index as per given input
print(fruit[:4]) #blank will be automatically taken a 0
print(fruit[:]) #Will return the default length of the fruit


print(fruit[0:-3])#python counts from 0 then automatically subtracts as per given value
print(fruit[0:len(fruit)-3])#both are same,here pyton counts it according to the LENGTH OF THE STRING

# print(fruit[-1:-3]) WILL NOT EXECUTE 
print(fruit[-3:-1]) #Length of array(given string) 9-3:9-1 which is 6:8,now it will count from 6 to 8 in index form and will display letters of 6&7 excluding last index number that is 8.



