class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # First approach
        """
        temp_nums = []
        array_index = 0
        while (array_index < len(nums)):
            x = nums[array_index]
            if x != 0:
                temp_nums.append(x)
            array_index += 1
        diff_index = len(nums) - len(temp_nums)
        while (diff_index):
            temp_nums.append(0)
            diff_index -= 1
        nums[:] = temp_nums
        """
        # Optimization lv1
        zero_index, array_index = 0, 0
        while (array_index < len(nums) and len(nums) > 1):
            if nums[array_index] != 0:
                nums[zero_index], nums[array_index] = nums[array_index], nums[zero_index]
                zero_index += 1
            array_index += 1
        print (f"nums:{nums}")

solution = Solution()

# Example 1:
nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
solution.moveZeroes(nums)

# Example 2:
nums = [0]
# Output: [0]
solution.moveZeroes(nums)

# Example 3:
nums = [0, 1]
# Output: [0, 1]
solution.moveZeroes(nums)

# Example 4:
nums = [1, 0]
# Output: [1, 0]
solution.moveZeroes(nums)