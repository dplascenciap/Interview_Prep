"""
Summary of Time and Space Complexities
Approach                Best Case  Worst Case   Space Complexity
Standard                   O(n²)      O(n²)          O(1)
"""
# Insertion sort
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        # 'current_value' or 'key' is commonly used in standard implementations
        current_value = nums[i]
        j = i - 1
        # Move elements greater than 'current_value' one position ahead
        while j >= 0 and nums[j] > current_value:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert 'current_value' at the correct position
        nums[j + 1] = current_value
    return nums

# Test cases for sorting algorithm
# Test Case 1: Empty list
assert insertion_sort([]) == []
# Test Case 2: Single element list
assert insertion_sort([1]) == [1]
# Test Case 3: Already sorted list
assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
# Test Case 4: Reverse sorted list
assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
# Test Case 5: Unsorted list with all positive numbers
assert insertion_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
# Test Case 6: List with negative and positive numbers
assert insertion_sort([-1, 3, 0, -5, 2, -4]) == [-5, -4, -1, 0, 2, 3]
# Test Case 7: List with duplicate values
assert insertion_sort([4, 5, 5, 3, 1, 1]) == [1, 1, 3, 4, 5, 5]
# Test Case 8: Large numbers
assert insertion_sort([10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000]
# Test Case 9: Already sorted list with duplicates
assert insertion_sort([1, 2, 2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]
# Test Case 10: List with identical elements
assert insertion_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

print("If you didn't get an assertion error, your program works great :)")