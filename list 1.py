#PROGRAM TO PRINT ALL POSITIVE INTEGERS IN A RANGE OF LIST

list=[]
n = int(input("Enter number of elements : "))

for i in range(0,n):
    a=int(input("Enter elements:"))
    list.append(a)
print("\n")    
print("List of numbers:",list)
print("\n")
print("The positive numbers in the list are:")
for num in list:
    if num>=0:
        print(num)
        
