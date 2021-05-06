#Trapping Rain water problem
def trappingWater(arr,n):
	r_max=l_max=ans=0
	left=0
	right=n-1
	while left<=right:
		if arr[left]<arr[right]:
			if arr[left]>l_max:
				l_max=arr[left]
			else:
				ans+=l_max-arr[left]
			left+=1
		else:
			if arr[right]>r_max:
				r_max=arr[right]
			else:
				ans+=r_max-arr[right]
			right-=1
	return ans