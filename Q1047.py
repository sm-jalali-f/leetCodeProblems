class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for i in range(0, len(s)):
            if len(result) == 0:
                result.append(s[i])
            else:
                if s[i] == result[-1]:
                    result.pop()
                else:
                    result.append(s[i])
        return "".join(result)

