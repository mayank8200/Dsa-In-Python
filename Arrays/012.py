#Merge 2 sorted arrays without using Extra space.
def merge(n1, n2, m, n):
        i = m-1
        j = 0
        while i>=0 and j<n:
            if n1[i]>n2[j]:
                n1[i],n2[j]=n2[j],n1[i]
            i-=1
            j+=1
        n1.sort()
        n2.sort()