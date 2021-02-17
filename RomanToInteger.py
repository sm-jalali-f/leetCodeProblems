def romanToInt(s: str) -> int:
    result = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(s)):
        if s[i] == 'I':
            if i == len(s) - 1:
                result += romans[s[i]]
            elif s[i + 1] in ['V', 'X']:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        elif s[i] == 'X':
            if i == len(s) - 1:
                result += romans[s[i]]
            elif s[i + 1] in ['L', 'C']:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        elif s[i] == 'C':
            if i == len(s) - 1:
                result += romans[s[i]]
            elif s[i + 1] in ['D', 'M']:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        else:
            result += romans[s[i]]
    return result
