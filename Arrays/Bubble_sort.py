"""
Summary of Time and Space Complexities
Approach                Best Case  Worst Case   Space Complexity
Basic Bubble Sort          O(n²)      O(n²)          O(1)
Optimization Early Exit    0(n)       O(n²)          O(1)
"""
# Basic bubble sort
def bubble_sort_basic(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# Optimization with early exit
# This optimized version includes a flag (swapped) to check if any swaps
# occurred during a pass. If no swaps are made, the array is already sorted,
# and the algorithm exits early.
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

# Test Case 1: Empty list
assert bubble_sort([]) == []
# Test Case 2: Single element list
assert bubble_sort([1]) == [1]
# Test Case 3: Already sorted list
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
# Test Case 4: Reverse sorted list
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
# Test Case 5: Unsorted list with all positive numbers
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
# Test Case 6: List with negative and positive numbers
assert bubble_sort([-1, 3, 0, -5, 2, -4]) == [-5, -4, -1, 0, 2, 3]
# Test Case 7: List with duplicate values
assert bubble_sort([4, 5, 5, 3, 1, 1]) == [1, 1, 3, 4, 5, 5]
# Test Case 8: Large numbers
assert bubble_sort([10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000]
# Test Case 9: Already sorted list with duplicates
assert bubble_sort([1, 2, 2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]
# Test Case 10: List with identical elements
assert bubble_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

print("If you didn't get an assertion error, your program works great :)")