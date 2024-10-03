"""
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
"""

class Solution:
    # Using a hash
    def containsDuplicate_hash(self, nums):
        duplicate_dict = {}
        for item in nums:
            if item in duplicate_dict:
                return True
            duplicate_dict[item] = "Duplicate"
        return False

    # Using a set
    def containsDuplicate(self, nums):
        duplicate_set = set()
        for item in nums:
            if item in duplicate_set:
                return True
            duplicate_set.add(item)
        return False

solution = Solution()

# Example 1:
nums = [1,2,3,1]
print (solution.containsDuplicate(nums))
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
nums = [1,2,3,4]
print (solution.containsDuplicate(nums))
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
nums = [1,1,1,3,3,4,3,2,4,2]
print (solution.containsDuplicate(nums))
# Output: true
