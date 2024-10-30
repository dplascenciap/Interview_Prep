# Selection sort
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        index_min = i
        for j in range(i + 1, n):
            if nums[j] < nums[index_min]:
                index_min = j
        # Swap elements
        nums[i], nums[index_min] = nums[index_min], nums[i]
    return nums

# Test cases for selection sort
# Test Case 1: Empty list
assert selection_sort([]) == []
# Test Case 2: Single element list
assert selection_sort([1]) == [1]
# Test Case 3: Already sorted list
assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
# Test Case 4: Reverse sorted list
assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
# Test Case 5: Unsorted list with all positive numbers
assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
# Test Case 6: List with negative and positive numbers
assert selection_sort([-1, 3, 0, -5, 2, -4]) == [-5, -4, -1, 0, 2, 3]
# Test Case 7: List with duplicate values
assert selection_sort([4, 5, 5, 3, 1, 1]) == [1, 1, 3, 4, 5, 5]
# Test Case 8: Large numbers
assert selection_sort([10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000]
# Test Case 9: Already sorted list with duplicates
assert selection_sort([1, 2, 2, 3, 4, 5]) == [1, 2, 2, 3, 4, 5]
# Test Case 10: List with identical elements
assert selection_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

print("If you didn't get an assertion error, your program works great :)")