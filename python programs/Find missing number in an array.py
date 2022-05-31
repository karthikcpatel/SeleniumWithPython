def missing_number_in_array():
    n = arr[-1]
    total = n*(n+1)//2
    newsum=sum(arr)
    x = total-newsum
    print("The missing number is:", +x)

arr = [5,2,4,3,6,7,8,9]
missing_number_in_array()