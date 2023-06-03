#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter, defaultdict


def validAnagram(a, b):
    if Counter(a) == Counter(b):
        return True
    return False


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for cur_str in strs:
            count = [0] * 26
            for i in cur_str:
                count[ord(i) - ord("a")] += 1
            result[tuple(count)].append(cur_str)
        return result.values()


# @lc code=end
