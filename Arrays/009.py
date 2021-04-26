#Minimise the maximum difference between heights [V.IMP]
def getMinDiff(arr,k):
    if len(arr)<2:
        return
    arr.sort()
    ans = arr[-1]-arr[0]
    small = arr[0]+k
    big = arr[-1]-k
    i=1
    while i<len(arr)-1:
        subtract = arr[i]-k
        add = arr[i]+k
        if subtract>=small or add<=big:
            i+=1
            continue
        if big-subtract<=add-small:
            small = subtract
        else:
            big = add
        i+=1
    return big-small