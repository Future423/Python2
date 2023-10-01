l=[]
n = int(input("Enter number of elements:"))
for i in range(0,n):
 e = int(input("Enter element:"))
 l.append(e) 
print("The list created is: ",l)

#appending
a = int(input("Enter the element to append in the list:"))
l.append(a)
print("The appended list :",l)
