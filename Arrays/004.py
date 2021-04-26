#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
def sort012(self,arr,n):
        i=0
        j=0
        k=n-1
        while j<=k:
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j+=1
            elif arr[j]==1:
                j+=1
            else:
                arr[k],arr[j]=arr[j],arr[k]
                k-=1