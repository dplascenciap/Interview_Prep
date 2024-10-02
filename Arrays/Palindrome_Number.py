class Solution:
    def isPalindrome(self, x):
        x_string    = str(x)
        lex_x_sting = len(x_string)
        if lex_x_sting == 1:
            return True
        # left_index, right_index = 0, lex_x_sting - 1
        left_index  = 0
        right_index = lex_x_sting - 1
        while left_index > right_index:
            if x_string[left_index] != x_string[right_index]:
                return False
            left_index  += 1
            right_index -= 1
        return True

solution = Solution()
x = 121
print (solution.isPalindrome(x))
