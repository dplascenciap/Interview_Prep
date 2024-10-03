class Solution:
    # First attemmpt
    def find_distance(self, nums, k):
        l = 0
        r = 1
        while (l < len(nums) - 1):
            d = abs(nums[l] - nums[r])
            if d <= k:
                return True
            l += 1
            r = l + 1
        return False

    def containsNearbyDuplicate_first_attempt(self, nums, k):
        dup_dict = {}
        # Find duplicates and their index
        for i in range(len(nums)):
            index_list = []
            if nums[i] in dup_dict:
                index_list = dup_dict[nums[i]]
                index_list.append(i)
                dup_dict[nums[i]] = index_list
            else:
                index_list.append(i)
                dup_dict[nums[i]] = index_list
        print (dup_dict)

        # Scan dictionary to find index's distance
        for value in dup_dict.values():
            if len(value) >= 2:
                if (self.find_distance(value, k)):
                    return True
        return False

    # Optimization lv 1
    def containsNearbyDuplicate(self, nums, k):
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            # if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
            if nums[idx] in hset:
                d = abs(idx - hset[nums[idx]])
                if d <= k:
                    return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False

"""
Explanation.
Example 1:
Input: nums = [1, 2, 3, 1], k = 3

You are asked to check if there are two duplicate numbers where the distance
between their indices is less than or equal to 3.
In this case, nums[0] = 1 and nums[3] = 1, and the difference between their
indices is abs(0 - 3) = 3.
Since the difference 3 is less than or equal to k (3), the answer is true.

Input: nums = [1, 0, 1, 1], k = 1

You are checking for two identical numbers with a distance of at most 1 between
their indices.
Here, nums[2] = 1 and nums[3] = 1. The difference between their indices is abs(2 - 3) = 1.
Since the difference is 1 and it is less than or equal to k (1), the answer is true.
"""

solution = Solution()

# Example 1:
nums = [1,2,3,1]
k = 3
# Output: true
print (solution.containsNearbyDuplicate(nums, k))

# Example 2:
nums = [1,0,1,1]
k = 1
# Output: true
print (solution.containsNearbyDuplicate(nums, k))

# Example 3:
nums = [1,2,3,1,2,3]
k = 2
# Output: false
print (solution.containsNearbyDuplicate(nums, k))