import math

#datatypes
#int = 1,2,3,4
#float = 1.0, 2.0, 3.0
#string = "hello", 'world'




#Data structures 
#list = [1,2,3,4]
#tuple = (1,2,3,4)
#dictionary = {"key1": "value1", "key2": "value2"}
#set = {1,2,3,4}


# first = 4
# r = 5
# square_first = first * first
# area = math.pi * r * r

# radii = input("Enter the radius: ")
# area = math.pi * float(radii) * float(radii)
# print(f"The area of the circle is: {area:.2f}")



#Using data structures )(List) to store information about a person
Emma_Data = ["Emmanuel", "CGC", 20, "Computer Science"]
print(f"Before Change {Emma_Data}") 

Emma_Data.append(99)
print(f"After Change {Emma_Data}")

#using data structures (Dictionary) to store information about a person
Emma_Data_Dict = {"first_Name": "Emmanuel", "Second_Name": "Simba", "Age": "21"}
print(f"First name = {Emma_Data_Dict['first_Name']  }")
print(Emma_Data_Dict.get("Age"))