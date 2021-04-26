# find all pairs on integer array whose sum is equal to given number
def getPairsCount(arr, k):
        count=0
        d={}
        for i in arr:
            sub = k-i
            if sub in d:
                count+=d[sub]
            d[i]=d.get(i,0)+1
        return count