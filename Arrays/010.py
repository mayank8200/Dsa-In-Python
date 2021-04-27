#Minimum no. of Jumps to reach end of an array
def minJumps(nums):
	    if len(nums)==1: return 0
        
        reachableIndex = 0
        previousReachableIndex = 0
        jump = 0

        for curr in range(len(nums)):
            reachableIndex = max(reachableIndex,curr+nums[curr])

            if curr == previousReachableIndex:
                jump += 1
                previousReachableIndex = reachableIndex
                if previousReachableIndex >= len(nums) - 1:
                    return jump
        return -1