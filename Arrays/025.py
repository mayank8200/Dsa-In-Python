#Given an array of size n and a number k, find all elements that appear more than " n/k " times.

# Using Extra Space
def majorityElement(nums):
    n = len(nums)
    ans=[]
    if n==1:
        return nums
    d={}
    for i in nums:
        if i not in d:
            d[i]=0
        d[i]+=1
    for i in d.keys():
        if d[i]>(n/3):
            ans.append(i)
    return ans
    
#Without Using Extra Space(Using Moore’s Voting Algorithm)
def majorityElement(nums)
    if len(nums)==0:
        return []
    count1=count2=0
    candidate1=0
    candidate2=1
    for i in nums:
        if i==candidate1:
            count1+=1
        elif i==candidate2:
            count2+=1
        elif count1==0:
            candidate1=i
            count1=1
        elif count2==0:
            candidate2 = i
            count2=1
        else:
            count1-=1
            count2-=1
    return [i for i in (candidate1,candidate2) if nums.count(i)>len(nums)//3]