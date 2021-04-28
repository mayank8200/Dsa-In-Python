# Find factorial of a large number
def factorial(self, N):
    if N==1 or N==0:
        return "1"
    ans=1
    for i in range(2,N+1):
        ans*=i
    return str(ans)