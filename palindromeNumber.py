def isPalindrome( x: int) -> bool:
    temp = str(x)
    tempRev = temp[::-1]
    if temp == tempRev:
        return True
    return False
