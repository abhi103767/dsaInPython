
# upper bound in binary Search


import math

def lowerBound(nums: list[int],target) -> int :
    left = 0
    right = len(nums) - 1
    while left < right :
        mid = math.floor((left+right)/2)
        if nums[mid] < target:
            left = mid +1
        else:
            right = mid
    return left

def upperBound(nums : list[int],target) -> int :
    left = 0
    right = len(nums) -1 
    while left < right:
        mid = math.floor((left+right)/2)
        if nums[mid] <= target:
            left = mid  + 1
        else :
            right = mid   
    return left

u:int = upperBound([1,1,1,1,1,2,3,3,3],3)
l:int = lowerBound([1,1,1,1,1,2,3,3,1],1)
print('lower',l)
print('upper',u)

    
    