"""Quick Sort Algorithm Implementation"""
def quick_sort(nums):
    """Function to perform quick sort on a list of numbers."""
    if len(nums) <= 1:
        return nums

    pivot = nums[0]

    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
