def linearSearch(nums: list[int], target: int) -> bool:
    '''
    Linear Search is the most simple seaching algorithm working by simply traversing a list and comparing each element to the target

    Time complexity: O(n)
    Space complexity: O(1)
    '''

    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False


nums = [5, 2, 7, 3, 8, 9, 3, 10, 1, 6, 4]

target = 3 # True
print(linearSearch(nums, target))

target = 30 # False
print(linearSearch(nums, target))