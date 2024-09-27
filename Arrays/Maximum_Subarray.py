"""
Given an integer array nums, find the subarray with the largest sum, and return
its sum.
"""
class Solution:
    # Brute force approach
    # 201 / 210 testcases passed
    # Time Limit Exceeded...
    def max_sub_array_brute_force(self, nums):
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum


    # Divide and conquer method
    def find_max_cross(self, nums):
        # Get midpoint
        midpoint = len(nums) // 2

        # Calculate max left
        current_sum = 0
        max_left = nums[midpoint - 1]
        for item in nums[(midpoint - 1)::-1]:
            current_sum += item
            max_left = max(current_sum, max_left)

        # Calculate max left
        current_sum = 0
        max_right = nums[midpoint]
        for item in nums[midpoint:]:
            current_sum += item
            max_right = max(current_sum, max_right)

        max_cross = max(max_left, max_right, (max_left + max_right))
        return max_cross

    def find_max_array(self, nums):
        # Base case
        if len(nums) == 1:
            return nums[0]

        midpoint = len(nums) // 2
        left_array  = nums[:midpoint]
        right_array = nums[midpoint:]

        max_left  = self.find_max_array(left_array)
        max_right = self.find_max_array(right_array)
        max_cross = self.find_max_cross(nums)

        max_sum = max(max_left, max_right, max_cross)
        return max_sum

    # Kadane’s Algorithm
    def maxSubArray_kadane(self, nums):
        current_sum = 0
        max_sum = nums[0]

        for item in nums:
            current_sum += item
            current_sum = max(item, current_sum)
            max_sum = max(current_sum, max_sum)

        return max_sum

    # Optimization
    def maxSubArray(self, nums):
        max_sub = nums[0]
        current_sum = 0
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            if current_sum > max_sub:
                max_sub = current_sum
        return max_sub

solution = Solution()

# Example 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))

# Example 2:
nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))

# Example 3:
nums = [5,4,-1,7,8]
mid_point = len(nums) // 2
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))

# Example 4:
nums = [-2, 1]
# Output: 1
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))

# Example 5:
nums = [-2, -1]
# Output: -1
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))

# Example 6:
nums = [4, -5, 6, -5]
print (solution.max_sub_array_brute_force(nums))
print (solution.find_max_array(nums))
print (solution.maxSubArray(nums))
