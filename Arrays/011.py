#Find the Duplicate Number. There is only one repeated number
def findDuplicate(nums):
    d={}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            return i
nums=[1,5,7,8,1]
print(findDuplicate(nums))