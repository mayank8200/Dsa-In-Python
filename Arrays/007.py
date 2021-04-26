#Write a program to cyclically rotate an array by one.
def rotate(arr):
    return arr[-1:]+arr[:-1]
	
def rotate(arr, n):
    ele = arr[-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=ele
    print(arr)