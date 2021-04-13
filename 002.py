#Find the maximum and minimum element in an array
#Without Inbuilt Functions
def findminmax(arr)
    max = arr[0]
    min = arr[0]
    for i in arr
        if i>max
            max=i
        if i<min
            min=i
    print(max)
    print(min)

#Using Inbuilt Function    
def findminmax1(arr)
    print(max(arr))
    print(min(arr))
    

    