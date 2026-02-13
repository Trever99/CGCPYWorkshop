arr=[1,2,3,4,5,6,7]
size=len(arr)

print(range(size))

for ele in arr:
    print(ele)

for i in range(size):
    print(f"index = {i}, Element = {arr[i]}" )

for i in range(size-1,0,-1):
    print(arr[i])
    
   
print("Second ========================================")
for i in range(1,size):
        print(f"index = {i}, Element = {arr[i]}" )
        
print("Third ========================================")
for i in range(1,size,2):
      print(f"index = {i}, Element = {arr[i]}" ) 
      
print("Fourth ========================================")
for i in range(size -1,-1,-1   ):
      print(f"index = {i}, Element = {arr[i]}")      
      
      
#While Loops
student = True
year = 0
while student:
    print("Go to class")
    year +=1
    
    if year ==3:
      student = False  
      print("You have graduated!")
        
        
        
   
         
   
    
      
        
    