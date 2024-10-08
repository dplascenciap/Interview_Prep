"""
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.
"""
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Get the len
        nums_len = len(nums)
        # Optimize the number of rotations
        k = k % nums_len
        # Create a temp array
        nums_temp = []

        """
        Try to find what the index x will be in the new array.
        Example
        A[a, b, c] with k = 2 => A[b, c, a]
        new_A[0] = A[1]
        new_A[1] = A[2]
        new_A[2] = A[0]
        In other words:
        index [0] = A[len(A) - k + index]
        index [0] = A[3 - 2 + 0]
        index [0] = A[1]
        index [1] = A[3 - 2 + 1] => A[2]
        index [2] = A[3 - 2 + 2] => A[3]. This generates an overflow so:
                                          new_index = new_index - len(A)
                                          new_index = 3 - 3
                                          new_index = 0
        index [2] = A[0]
        """
        for index in range(nums_len):
            new_index = nums_len - k + index
            if new_index >= nums_len:
                new_index = new_index - nums_len
            nums_temp.append(nums[new_index])
        # Replace original array
        nums[:] = nums_temp
        print (f"nums:{nums}")

solution = Solution()
# Example 1:
nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
solution.rotate(nums, k)

# Example 2:
nums = [-1,-100,3,99]
k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
solution.rotate(nums, k)