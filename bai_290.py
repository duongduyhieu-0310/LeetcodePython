#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char
            elif char in char_to_word and word in word_to_char:
                if char_to_word[char] == word and word_to_char[word] == char:
                    continue
                else:
                    return False
            else:
                return False
            
        return True

# @lc code=end

