class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        splitted = haystack.split(needle)
        if len(splitted[0]) == len(haystack):
            return -1
        return len(splitted[0])


