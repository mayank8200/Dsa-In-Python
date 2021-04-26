#Find the Union and Intersection of the two sorted arrays.
#Using Inbuilt Functions
def doUnion(a,b):
        a = set(a)
        b = set(b)
        print(a | b)
        print(a & b)

def doUnion(a,b):
        a=list(set(a))
        b=list(set(b))
        union=a[:]
        for i in b:
            if i not in a:
                union.append(i)
        print(union)
        inter=[]
        for i in a:
            if i in b:
                inter.append(i)
        print(inter)
		
