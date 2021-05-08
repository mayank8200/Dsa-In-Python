#Minimum swaps required to bring all elements less than or equal to k together
def minSwap (arr, n, k) : 
    (answer, count) = (n, 0)

    # Count elements less than or equal to k

    for i in range(n):
        if arr[i] <= k:
            count += 1

    currentMin = 0
    
    # Calculate minimum swaps for each window of size count and update answer

    for i in range(n):
        if arr[i] > k:
            currentMin += 1
        
        if i >= count and arr[i - count] > k:
            currentMin -= 1
            
        if i >= count - 1:
            answer = min(answer, currentMin)

    return answer