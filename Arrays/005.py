#Move all the negative elements to one side of the array
#With Inbuilt Function
def moveneg(arr):
    ind=0
    i=0
    while i<len(arr):
        if arr[i]<0:
            arr.insert(ind,arr[i])
            ind+=1
            arr.pop(i+1)
        i+=1
arr = [-1, 2, -3, 4, 5, 6, -7, 8, -9 ]
moveneg(arr)
print(arr)

#Without Inbuilt Function            
def moveneg(arr):
    j=0
    i=0
    while i<len(arr):
        if arr[i]<0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
        i+=1