from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if len(strs) == 0:
            return commonPrefix
        maxLength = min([len(v) for v in strs])
        for i in range(0, maxLength):
            temp = set()
            for item in strs:
                temp.add(item[i])
            if len(temp) == 1:
                commonPrefix += temp.pop()
            else:
                break
        return commonPrefix
