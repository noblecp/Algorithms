def binarySearch(nums: list[int], low: int, high: int, target: int) -> bool:
    '''
    Binary Search works by constantly cutting down on half the search space, but the input array to be sorted

    Time complexity: O(log n)
    Space complexity: O(1)
    '''
    nums.sort()
    
    if len(nums) <= 0:
        return False
    
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        
        elif target > nums[mid]:
            return binarySearch(nums, mid+1, len(nums)-1, target)
        else:
            return binarySearch(nums, 0, mid-1, target)
    return False

nums = [5, 2, 7, 3, 8, 9, 3, 10, 1, 6, 4]

target = 3 # True
print(binarySearch(nums, 0, len(nums)-1, target))

target = 11 # False
print(binarySearch(nums, 0, len(nums)-1, target))