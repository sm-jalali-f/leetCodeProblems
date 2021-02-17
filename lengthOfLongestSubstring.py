def lengthOfLongestSubstring(s: str) -> int:
    substring = set()
    maxLength = 0
    for j in range(0, len(s)):
        for i in range(j, len(s)):
            if s[i] in substring:
                maxLength = max(maxLength, len(substring))
                substring = set()
                break
            else:
                substring.add(s[i])
        maxLength = max(maxLength, len(substring))
    return maxLength
