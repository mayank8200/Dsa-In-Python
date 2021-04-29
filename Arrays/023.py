#find maximum product subarray
def maxProduct(self,arr, n):
	currMax=arr[0]
    currMin=arr[0]
    allMax=arr[0]
    for i in arr[1:]:
        temp=currMax
        currMax=max(i,i*currMax,i*currMin)
        currMin=min(i,i*temp,i*currMin)
        allMax=max(currMax,allMax) 
    return allMax