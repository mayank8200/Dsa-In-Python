# Find whether an array is a subset of another array
def isSubset(a1, a2):
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            return "No"
    return "Yes"