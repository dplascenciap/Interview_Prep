"""
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.
"""

class Solution:
    def isAnagram(self, s, t):
        # First attempt
        """
        if len(s) != len(t):
            return False
        for char in s:
            s1 = s.count(char)
            t1 = t.count(char)
            if s1 != t1:
                return False
        return True
        """
        # Two Hash implementation
        """
        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        if s_dict == t_dict:
            return True
        else:
            return False
        """
        # One hash implementation
        if len(s) != len(t):
            return False
        anagram_dict = {}

        for char in s:
            if char in anagram_dict:
                anagram_dict[char] += 1
            else:
                anagram_dict[char] = 1

        for char in t:
            if char not in anagram_dict:
                return False
            elif char in anagram_dict and anagram_dict[char] < 1:
                return False
            else:
                anagram_dict[char] -= 1

        return True

solution = Solution()

# Example 1:
s = "anagram"
t = "nagaram"
print (solution.isAnagram(s, t))
# Output: true

# Example 2:
s = "rat"
t = "car"
print (solution.isAnagram(s, t))
# Output: false
