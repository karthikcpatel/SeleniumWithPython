def getMinMax(a, n):
    min = a[0]
    max = a[0]
    for i in range(0, n):

        if a[i] < min:
            min = a[i]
    for i in range(0, n):

        if a[i] > max:
            max = a[i]
    return min, max

a = [55,22,11,66,33,99]
n = len(a)
print("Minimum element of array:", getMinMax(a,n))