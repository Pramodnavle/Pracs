import sys
A=[]
p=int(input("Enter number of elements :   "))
n=p
while(n>0):
    x=int(input("Enter element :   "))
    A.append(x)
    n=n-1
    
# Traverse through all array elements
for i in range(len(A)):
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] =A[min_idx], A[i]
     

            # Swap the found minimum element with
            # the first element
    
print("Smallest element : %d" %int(A[0]))
print("Largest element : %d" %int(A[p-1]))
print ("Sorted array in Ascending Order: ",A) 
