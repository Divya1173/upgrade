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
        check = defaultdict(str)
        counter_dict = defaultdict(dict)
        for i in strs:
            check[i] = False
            counter_dict[i] = Counter(i)

        def validAnagram(a, b):
            if counter_dict[a] == counter_dict[b]:
                return True
            return False

        ans = []
        for i in range(len(strs)):
            anagram = []
            if not check[strs[i]]:
                check[strs[i]] = True
                anagram.append(strs[i])
                for j in range(i + 1, len(strs)):
                    if validAnagram(strs[i], strs[j]):
                        anagram.append(strs[j])
                        check[strs[j]] = True
            if len(anagram) != 0:
                ans.append(anagram)
        return ans


# @lc code=end
