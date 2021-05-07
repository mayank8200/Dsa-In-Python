#Smallest Subarray with sum greater than a given value
def sb(a, n, x):
	start=0
	ans=0
	min_length=n+1
	for end in range(n):
		ans+=a[end]
		while ans>x:
			min_length=min(min_length,end-start+1)
			ans-=a[start]
			start+=1
		# If no such subarray exists
		else:
			return 0
	return min_length