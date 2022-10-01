'''
Insertion Sort is a divide-and-conquer sorting algorithm that functions similar to hand-sorting a deck of cards. The algorithm functions by virtually splitting our input array into two parts, a sorted part and an unsorted part. We slowly increase the length of the sorted part by considering each new element in the unsorted part.

Key characteristics:
    - one of the simplest algorithms
    - fast for small inputs
    - in place -> input and output occupies the same memory space
    - stable -> the order of input elements is unchanged in the output

Time complexity:
    Best case: O(n)
    Worst case: O(n^2) -> average case
Space complexity: O(1)
'''

def insertionSort(nums):
    '''
    This function simply performs insertion sort on the given input array
    @param1: input array to be sorted
    '''
    for i in range(1, len(nums)):       # iterate over all elements (not including 0 as we assume this is already "sorted")
        key = nums[i]                   # key is current element
        j = i-1                         # let j be the index of the previous element
        while j >= 0 and nums[j] > key: # nested loop, check each element in "sorted" portion as long as we are in bounds and key is less than the previous element
            nums[j+1] = nums[j]         # shift elements down by one
            j-=1                        # decrement j index
        nums[j+1] = key                 # set the fringe element to key as we stored previously


def insertionSort_withBounds(nums, start, end):
    '''
    This function performs insertion on the input array only for the given array bounds (e.g. sort only the first X elements)
    @param1: input array to be sorted
    @param2: start index
    @param3: end index
    '''
    for i in range(start + 1, end + 1):         # iterate from 2nd to last element, do same as above
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

# "randomised" non-ascending input array
nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
print("Before:\t", nums)

# perform insertion sort and print results
insertionSort(nums)
# insertionSort_withBounds(nums, 0, len(nums)-1)
print("After:\t", nums)