import functools


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for _ in range(0, numRows)]
        for i in range(0, len(s)):
            rem = i % ((numRows - 1) * 2)
            if rem < numRows:
                result[rem].append(s[i])
            else:
                result[numRows - (rem % numRows) - 2].append(s[i])

        return "".join(functools.reduce(lambda a, b: a + b, result))


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("A", 1))
