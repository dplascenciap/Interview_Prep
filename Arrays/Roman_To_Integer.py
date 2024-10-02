"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Hint: Scan the string backwards, and consider that if a lesser number follows
# it means a subtraction. E.g.
# Input = 'IV' is 'VI' backward, since 'I' is lesser than 'V', this means 5 - 1.
class Solution:
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 1:
            return roman_dict[s]
        total_sum   = 0
        index = len(s) - 1
        prev_number = roman_dict[s[index]]
        while index >= 0:
            current_number = roman_dict[s[index]]
            if current_number < prev_number:
                total_sum -= current_number
            else:
                total_sum += current_number
            prev_number = current_number
            index -= 1
        return total_sum

solution = Solution()
# Example 1
s = "III"
# Output: 3
solution.romanToInt(s)

# Example 2:
s = "LVIII"
# Output: 58
solution.romanToInt(s)

# Example 3:
s = "MCMXCIV"
# Output: 1994
solution.romanToInt(s)