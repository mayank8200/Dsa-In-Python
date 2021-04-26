def merge(arr1, arr2, n, m): 
        temp = arr2[0]
        for i in range(n):
            if arr1[i]>arr2[0]:
                arr1[i],arr2[0]=arr2[0],arr1[i]
                arr2.sort()