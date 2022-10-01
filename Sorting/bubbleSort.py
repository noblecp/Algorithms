'''
Bubble Sort is the simplest sorting algorithm, working by repeatedly swapping the adjacent elements if they are in th wrong order

Time complexity: O(n^2)
Space complexity: O(1) -- in place
'''

def bubbleSort(nums):
    '''
    This function performs naive bubble sort in place
    @param1: list to be sorted
    '''
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

def bubbleSort_optimised(nums):
    '''
    This function optimises bubbleSort by stopping the inner loop in the case that there was no swap (i.e. the current expanding list is sorted by this i^th iteration)
    @param1: list to be sorted
    '''
    n = len(nums)
    hasSwapped = False
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                hasSwapped = True
        if not hasSwapped:
            break


def bubbleSort_recursive(nums, n):
    '''
    This function performs bubbleSort recursively
    @param1: list to be sorted
    '''
    # base case length of nums is <= 1
    if n - 1 <= 1:
        return
    for i in range(n-1):
        if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return bubbleSort_recursive(nums, n-1)
    
# "randomised" non-ascending input array
nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
print("Before:\t", nums)

# perform Bubble Sort and print results
# bubbleSort(nums)
bubbleSort_optimised(nums)
# bubbleSort_recursive(nums, len(nums))

print("After:\t", nums)