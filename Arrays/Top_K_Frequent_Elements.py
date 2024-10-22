from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums

        # Build dict_count
        dict_count = {}
        for item in nums:
            if item in dict_count:
                dict_count[item] += 1
            else:
                dict_count[item] = 1

        # Initialize frequency list.
        # Create a list of list
        frequency_list = []
        for _ in range(len(nums) + 1):
            frequency_list.append([])

        # Scan dictionary and map frequency list
        for key, value in dict_count.items():
            frequency_list[value].append(key)

        # Flatten the list
        frequency_flat = []
        for sublist in frequency_list:
            for item in sublist:
                frequency_flat.append(item)

        # Return k elements
        return frequency_flat[-k:]

    def top_k_bucket_sort(self, nums, k):
        # Step 1 - Count frequencies
        # A) Use the method counter O(n)
        # dict_frequency = Counter(nums)
        # B) Populate the dictionary O(n)
        dict_frequency = {}
        for item in nums:
            if item in dict_frequency:
                dict_frequency[item] += 1
            else:
                dict_frequency[item] = 1

        # Step 2 - Create a bucket
        # A) Use list comprehension O(n)
        buckets = [[] for _ in range(len(nums) + 1)]
        # B) Use a nested loop O(n)
        #
        # buckets = []
        # for _ in range(len(nums) + 1):
        #     buckets.append([])
        #
        # '_'. The underscore is used as a placeholder for the loop variable
        # since it's not actually needed or used in the comprehension. This is a
        # common practice when the index or loop variable isn't necessary for
        # the operation.

        # Step 2.1 - Distribute the elements into buckets. This is only part of
        # the problem that relates to the "bucket sort" method. Technically, we
        # don't need to sort each bucket to solve this problem, therefore,
        # THIS IS NOT A BUCKET SORT problem.
        # There are many ways to distribute the elements, one option could be
        # index = int(num*n). In this case, this is not a bucket sort problem
        # so we are just distributing the items based on their count. E.g., if
        # the number '2' shows up three times, it will go into the index = 3
        #
        for key, value in dict_frequency.items():
            buckets[value].append(key)

        # Step 3 - Gather the top k frequent elements - O(n)
        # This step is part of the bucket sort process, we need to 'flat' or
        # 'concatenate' the buckets.
        # We'll scan the bucket backwards since we need the top k elements.
        # The top K elements are located at the end of the array. We'll scan the
        # array and we'll stop when the len of the array equals k
        result = []
        for index in range(len(buckets) - 1, 0, -1):
            for item in buckets[index]:
                result.append(item)
                if len(result) == k:
                    return result



"""
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
"""
solution = Solution()
# Example 1:
nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]
print(solution.topKFrequent(nums, k))
print(solution.top_k_bucket_sort(nums, k))

# Example 2:
nums = [1]
k = 1
# Output: [1]
print(solution.topKFrequent(nums, k))

# Example 3:
nums = [-1,-1]
k = 1
# Output: [-1]
print(solution.topKFrequent(nums, k))

# Example 4:
nums = [1,2]
k = 2
# Output: [1,2]
print(solution.topKFrequent(nums, k))
