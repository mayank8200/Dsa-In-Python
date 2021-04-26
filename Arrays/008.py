#Find Largest sum contiguous Subarray [V. IMP]
def maxSubArraySum(a):
        temp=0
        maxSum=0
        for i in a:
            temp+=i
            if temp>maxSum:
                maxSum=temp
            if temp<0:
                temp=0
        return maxSum