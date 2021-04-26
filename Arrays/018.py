#find common elements In 3 sorted arrays
#One Liner Solution 
def commonElements (A, B, C):
    return sorted(list(set(A) & set(B) & set(C)))

#Naive Solution
def commonElements (self,A, B, C, n1, n2, n3):
    i=0
    j=0
    k=0
    ans=[]
    while i<n1 and j<n2 and k<n3:
        if A[i]==B[j] and B[j]==C[k]:
            ans.append(A[i])
            i+=1
            j+=1
            k+=1
        elif A[i]<B[j]:
            i+=1
        elif B[j]<C[k]:
            j+=1
        else:
            k+=1
    return sorted(list(set(ans)))