class Solution(object):
    def convert_str_to_ascii(self, word):
        return ''.join(sorted(word))
        """
        ascii_key = [0] * 26
        for index in range(len(word)):
            ascii_key[ord(word[index]) - ord("a")] += 1
        return tuple(ascii_key)
        """

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_list = []
        if len(strs) == 1 or strs == "":
            result_list.append(strs)
            return result_list

        dict_anagram = {}
        for word in strs:
            ascii_key = self.convert_str_to_ascii(word)
            if ascii_key in dict_anagram:
                dict_anagram[ascii_key].append(word)
            else:
                dict_anagram[ascii_key] = [word]

        return dict_anagram.values()
"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""

solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
# Output : [["tan","nat"],["bat"],["eat","tea","ate"]]
print(solution.groupAnagrams(strs))