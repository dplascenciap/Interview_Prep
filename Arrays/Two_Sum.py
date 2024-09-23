class Solution:
    # Approach one, brute force    
    # Scan each element in the array and sum each of them
    # Run time = 4105 ms
    def twoSum_brute_force(self, nums, target):        
        for index_a in range(len(nums)):
            for index_b in range(len(nums)):
                if index_a == index_b: continue
                sum = nums[index_a] + nums[index_b]
                if target == sum:
                    return (index_a, index_b)

    # Approach two, optimization level 1.    
    # Find if each element can add up to the target 
    # Run time = 2432 ms
    def twoSum_optimization_v1(self, nums, target):
        for index_a in range(len(nums)):
            element_to_find = target - nums[index_a]
            for index_b in range(len(nums)):                        
                if index_a == index_b: continue
                if nums[index_b] == element_to_find:
                    return (index_a, index_b)
                
    # Approach three, optimization level 2.
    # Find the element that can add up to the target in a list
    # Run time = 495 ms
    def twoSum_optimization_v2(self, nums, target):
        for index_a in range(len(nums)):
            element_to_find = target - nums[index_a]
            if element_to_find in nums:
                index_b = nums.index(element_to_find)
                if index_a == index_b: continue
                return(index_a, index_b)

    # Approach three, optimization level 3.
    # Find the element that can add up to the target in a hash map
    # Run time = 61 ms
    def twoSum_optimization_v3(self, nums, target):
        dict_candidates = {}
        for index_a in range(len(nums)):
            element_to_find = target - nums[index_a]
            if element_to_find in dict_candidates:
                return (dict_candidates[element_to_find], index_a)
            dict_candidates[nums[index_a]] = index_a

solution = Solution()

# Example 1
nums = [2,7,11,15]; target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
print (solution.twoSum_brute_force(nums, target))
print (solution.twoSum_optimization_v1(nums, target))
print (solution.twoSum_optimization_v2(nums, target))
print (solution.twoSum_optimization_v3(nums, target))
print ("------")

# Example 2
nums = [3,2,4]; target = 6
# Output: [1,2]
print (solution.twoSum_brute_force(nums, target))
print (solution.twoSum_optimization_v1(nums, target))
print (solution.twoSum_optimization_v2(nums, target))
print (solution.twoSum_optimization_v3(nums, target))
print ("------")

#Example 3:
nums = [3,3]; target = 6
# Output: [0,1]
print (solution.twoSum_brute_force(nums, target))
print (solution.twoSum_optimization_v1(nums, target))
print (solution.twoSum_optimization_v2(nums, target))
print (solution.twoSum_optimization_v3(nums, target))
print ("------")
