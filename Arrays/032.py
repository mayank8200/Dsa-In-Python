#Three way partitioning of an array around a given value
def threeWayPartition(array, a, b):
	ans=[]
	i=0
	end=n-1
	start=0
	while i<=end:
		if array[i]<a:
			array[i],array[start]=array[start],array[i]
			i+=1
			start+=1
		elif array[i]>b:
			array[i],array[end]=array[end],array[i]
			end-=1
		else:
			i+=1
	
	return array