import math

def reverse(x: int) -> int:
    rem = abs(x) % 10
    temp = int(abs(x) / 10)
    result = 0
    while temp > 0:
        result = result * 10 + rem
        rem = temp % 10
        temp = int(temp / 10)
    result = result * 10 + rem
    if x < 0:
        result = result * -1
    if -1 * (math.pow(2, 31)) <= result <= (math.pow(2, 31)) - 1:
        return result
    return 0
