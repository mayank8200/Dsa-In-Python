#Chocolate Distribution problem
def findMinDiff(A,N,M):
	A.sort()
	i=1
	temp=0
	ans=A[M-1]-A[0]
	j=M
	while j<N:
		temp=A[j]-A[i]
		if ans>temp:
			ans=temp
		j+=1
		i+=1
	return ans