"""
Given an integer array nums, find the subarray with the largest sum, and return
its sum.
"""
class Solution:
    # Kadane’s Algorithm
    def maxSubArray(self, nums):
        print ("-------")
        largest_sum = nums[0]
        sum_temp    = nums[0]
        for index in range(1, len(nums)):
            sum_temp = max(nums[index], nums[index] + sum_temp)
            if sum_temp > largest_sum:
                largest_sum = sum_temp
        return (largest_sum)

    def max_sub_array_brute_force(self, nums):
        largest_sum = nums[0]
        for i in range(len(nums)):
            sum_temp = nums[i]
            for j in range(i, len(nums)):
                if i == j:
                    continue
                sum_temp += nums[j]
                print (f"sum_temp:{sum_temp}")
                if sum_temp > largest_sum:
                    largest_sum = sum_temp
                    print (f"largest_sum:{largest_sum}")
        return largest_sum


solution = Solution()
"""
# Example 1
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
print (solution.max_sub_array_brute_force(nums))

# Example 2:
nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
print (solution.max_sub_array_brute_force(nums))

# Example 3:
nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
print (solution.max_sub_array_brute_force(nums))
"""
# Example 4:
nums = [-2, 1]
# Output: 1
print (solution.max_sub_array_brute_force(nums))

# # Example 5:
# nums = [-2, -1]
# # Output: -1
# print (solution.max_sub_array_brute_force(nums))
