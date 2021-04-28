# Find if there is any subarray with sum equal to 0
def subArrayExists(self,arr,n):
    sum_set = set()
    ans = 0
    for i in range(n):
        ans += arr[i]
        if ans == 0 or ans in s:
            return True
        s.add(ans)

    return False