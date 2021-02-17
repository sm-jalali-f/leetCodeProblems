from typing import List


def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    pointer1 = 0
    pointer2 = 0
    medianIndex = int((len(nums1) + len(nums2)) / 2)
    isOne = True
    if (len(nums1) + len(nums2)) % 2 == 0:
        medianIndex -= 0.5
        isOne = False
    sumPointer = 0
    l = []
    lastNum = 0
    while True:
        if pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                lastNum = nums1[pointer1]
                pointer1 += 1
            else:
                lastNum = nums2[pointer2]
                pointer2 += 1
        elif pointer1 < len(nums1) and pointer2 == len(nums2):
            lastNum = nums1[pointer1]
            pointer1 += 1
        elif pointer1 == len(nums1) and pointer2 < len(nums2):
            lastNum = nums2[pointer2]
            pointer2 += 1
        else:
            break
        l.append(lastNum)
        if isOne and sumPointer == medianIndex:
            return l[sumPointer]
        elif not isOne and sumPointer > medianIndex > sumPointer - 1:
            return (l[sumPointer] + l[sumPointer - 1]) / 2.
        sumPointer += 1
