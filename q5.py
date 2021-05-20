
import math
n = int(input("Enter number of elements to be in list: "))
list1 = list(map(int,input("\nEnter the numbers of list1: ").strip().split()))[ :n]
list2 = list(map(int,input("\nEnter the numbers of list2: ").strip().split()))[ :n]
list3 = list(map(int,input("\nEnter the numbers of list3: ").strip().split()))[ :n]
print("\nList1 is: ", list1)
print("\nList2 is: ", list2)
print("\nList3 is: ", list3)
list1.sort()
print("\nLargest element in list1 is:", list1[-1])
list2.sort()
print("Largest element in list2 is:", list2[-1])
list3.sort()
print("Largest element in list3 is:", list3[-1])

#addition of elements in each list
total1 = sum(list1)
total2 = sum(list2)
total3 = sum(list3)
print("\nSum of elements in list1: " ,total1)
print("Sum of elements in list2: " ,total2)
print("Sum of elements in list3: " ,total3)

#addition of 3 lists 
ziplist = zip(list1, list2, list3)
sum = [x+y+z for (x, y, z) in ziplist]
print("\nList After Addition is: " +str(sum))


#multiplication of elements of each list

res1 = math.prod(list1)
res2 = math.prod(list2)
res3 = math.prod(list3)
print("\nProduct of elements in list1: " ,res1)
print("Product of elements in list2: " ,res2)
print("Product of elements in list3: " ,res3)




