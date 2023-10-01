l=[]
#we can use a precreated list too
#l=[11,12,13,14,15]

n = int(input("Enter number of elements:"))
for i in range(0,n):
  e = int(input("Enter element:"))
  l[i] = e
print("The list created is: ",l)

#appending
a = int(input("Enter the element to append in the list:"))
l=l.append(a)
print("The appended list :",l)
