#Next Permutation
def nextPermutation(nums):
        length = len(nums)
        if length==1:
            return
        if length==2:
            return nums.reverse()
        ptr=length-2
        while ptr>=0 and nums[ptr]>=nums[ptr+1]:
            ptr-=1
        if ptr==-1:
            return nums.reverse()
        for i in range(length-1,ptr,-1):
            if nums[i]>nums[ptr]:
                nums[i],nums[ptr]=nums[ptr],nums[i]
                break
        nums[ptr+1:]=reversed(nums[ptr+1:])