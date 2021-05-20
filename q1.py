#Take user input, create a Python list, find a value in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
n = int(input("Enter number of elements to be in list: "))
list1= list(map(int,input("\nEnter the numbers of list: ").strip().split()))[ :n]
print("\nList is: ", list1)
no = int(input("\nEnter the number you want to find: "))
index = list1.index(no)
list1[index] = 200
print("\nNew list is: ", list1)

