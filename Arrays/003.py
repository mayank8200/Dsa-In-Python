#Find the "Kth" max and min element of an array

def kthmaxmin(arr,k):
    arr.sort()
    print(arr[k-1])
    print(arr[-k])