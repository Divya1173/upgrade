#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import Counter


# Look for edge case like s = 'a' and t = 'ab'
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        for i in count_s.keys():
            if count_s[i] != count_t[i]:
                return False
        return True


# @lc code=end
