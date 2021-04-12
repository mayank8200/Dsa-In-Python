#Reverse the array

#Sample Array 
array = [4,5,1,7,28,5]

#Code Without Inbuilt Functions
def reverseArray(array,n):
    i = 0
    j = n-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1
    return array

#Using List comprehension
def reverseArray1(array):
    return array[::-1]

#Using Inbuilt Function
def reverseArray2(array):
    return list(reversed(array))


n = int(input("Enter the size of array:"))
array = [int(x) for x in input().split()]
print(reverseArray(array,n))
print(reverseArray1(array))
print(reverseArray2(array))