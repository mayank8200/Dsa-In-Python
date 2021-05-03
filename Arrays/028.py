# Find the triplet that sum to a given value
def find3Numbers(A, n, X):
    A.sort()
    for i in range(n-2):
        l=i+1
        r=n-1
        while l<r:
            if A[l]+A[r]+A[i]==X:
                return True
            elif A[l]+A[r]+A[i]<X:
                l+=1
            else:
                r-=1
    return False