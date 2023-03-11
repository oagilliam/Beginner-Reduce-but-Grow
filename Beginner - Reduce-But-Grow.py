# DESCRIPTION:
# Given a non-empty array of integers, return the result of multiplying the values together in order. 
# Example: [1,2,3,4]  -> 1*2*3*4 = 24


# My Solution
def grow(arr):
    prod = 1
    for num in arr:
        prod *= num
    return prod
    
print(grow([1,2,3,4]))
