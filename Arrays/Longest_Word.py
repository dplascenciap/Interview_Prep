"""
Have the function LongestWord(sen) take the sen parameter being passed and
return the longest word in the string. If there are two or more words that are
the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Words may also contain
numbers, for example "Hello world123 567"
"""
import re

def LongestWord(sen):
    # code goes here
    match = re.findall("\w+", sen)
    max_len = 0
    for item in match:
        temp_len = len(item)
        if temp_len > max_len:
            max_len = temp_len
            sen = item
    return sen

# keep this function call here
# Example 1:
string = "fun&!! time"
# Output: time
print(LongestWord(string))

# Example 2:
string = "I love dogs"
# Output: love
print(LongestWord(string))