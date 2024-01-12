from insertionSort import insertionSort

'''
Quick Sort is a divide-and-conquer sorting algorithm. It picks a pivot element around which to partition the given array. The main work is done by a helper function, partition(). Partition aims to do the following: given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

Key characteristics:
    - In place (if not considering the recursive call stack used in recursive sorting)

Time complexity:
    Best case: O(n log n)
    Worst case: O(n^2) -> average case
Space complexity: O(1)
'''

def partition(nums, start, end):
    '''
    This is a helper function for quickSort which sorts the given array by picking a pivot and partitioning the array around the chosen pivot
    @param1: input array
    @param2: start index
    @param3: end index
    '''
    pivot = nums[end]                               # use last element as pivot
    i = start - 1                                   # use i as the previous element to the start index
    for j in range(start, end):                     # iterate over given range
        if nums[j] < pivot:                         # if pivot is greater than current element
            i += 1                                  # increment left bounds
            nums[i], nums[j] = nums[j], nums[i]     # swap elements in left and right fringe
    i += 1
    nums[i], nums[end] = nums[end], nums[i]         # after loop ends, swap last element (chosen as pivot) with left bounds (i.e. i)
    return i                                        # return pivot in correct position


def quickSort(nums, start, end):
    '''
    This function performs Quick Sort utilising helper function partition()
    @param1: input array
    @param2: start index
    @param3: end index
    '''
    if start < end:                                 # ensure bounds are feasible
        pivot = partition(nums, start, end)         # find pivot which is in correct relative position (all left are smaller, all right are larger)
        quickSort(nums, start, pivot-1)             # recursively quickSort the left subportion (smaller)
        quickSort(nums, pivot+1, end)               # recursively quickSort the right subportion (larger)

def quickSort_optimized(nums, start, end, minSize):
    '''
    This function is an optimized version of Quick Sort which calls insertionSort() for smaller subproblems according to given minimum size
    @param1: input array
    @param2: start index
    @param3: end index
    @param3: minimum length of array for which to use insertion sort
    '''
    # base case -> performs the optimization
    if len(nums) > 1 and len(nums) <= minSize:
        insertionSort(nums)
        # insertionSort_withBounds(nums, 0, len(nums)-1)

    if start < end:
        pivot = partition(nums, start, end)
        quickSort_optimized(nums, start, pivot-1, minSize)
        quickSort_optimized(nums, pivot+1, end, minSize)


# "randomised" non-ascending input array
nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

# perform Quick Sort
quickSort_optimized(nums, 0, len(nums)-1, 3)

#print results
print(nums)
