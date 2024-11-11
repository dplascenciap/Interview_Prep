"""
Summary of Time and Space Complexities
Approach                Best Case    Worst Case    Space Complexity
Standard                O(n log n)   O(n log n)         O(n)
"""
"""
We'll use the 'Divide and Conquer Approach.
1. Divide  - Split the array as evenly as possible
2. Conquer - Recursively sort each half
3. Combine - Merge the sorted halves back together

The base case for the recursion is one the array length is <= 1
"""
# Merge sort
def merge_sort(nums):
    # Base case
    if len(nums) <= 1:
        return nums

    # 1. Divide the array into two halves
    middle = len(nums) // 2

    # 2. Recursively sort each half
    left_half  = merge_sort(nums[:middle])
    right_half = merge_sort(nums[middle:])

    # 3. Merge the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    i = j = 0
    sorted_array = []
    # Compare the first element of each list, append the lower to the array
    # once we can't compare one to one, meaning that one of the arrays is empty
    # we have to copy the remaining elements, from either part, to the sorted
    # array. To copy the remaining elements, we should scan the array from the
    # last index position
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    # Copy remaining elements starting from the last index position
    # Alternatively you can copy the remaining elements like this:
    # Append remaining elements from either left or right
    # sorted_array.extend(left_half[i:])
    # sorted_array.extend(right_half[j:])
    # Or, use a loop to copy
    for i in range(i, len(left_half)):
        sorted_array.append(left_half[i])
    for j in range(j, len(right_half)):
        sorted_array.append(right_half[j])
    # Return the sorted array
    return sorted_array

# Test cases for merge sort
# Test Case 1: Empty list
assert merge_sort([]) == []
# Test Case 2: Single element list
assert merge_sort([1]) == [1]
# Test Case 3: Already sorted list
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
# Test Case 4: Reverse sorted list
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
# Test Case 5: Unsorted list with all positive numbers
assert merge_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
# Test Case 6: List with negative and positive numbers
assert merge_sort([-1, 3, 0, -5, 2, -4]) == [-5, -4, -1, 0, 2, 3]
# Test Case 7: List with duplicate values
assert merge_sort([4, 5, 5, 3, 1, 1]) == [1, 1, 3, 4, 5, 5]
# Test Case 8: Large numbers
assert merge_sort([10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000]
# Test Case 9: Already sorted list with duplicates
assert merge_sort([1, 2, 2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]
# Test Case 10: List with identical elements
assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]
assert merge_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([-3, -1, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]
assert merge_sort([4, 3, 1, 4, 2, 1]) == [1, 1, 2, 3, 4, 4]
assert merge_sort([1]) == [1]
assert merge_sort([]) == []
print("If you didn't get an assertion error, your program works great :)")