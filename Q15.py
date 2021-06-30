class Solution:
    def threeSum(self, nums):
        result = []
        sorted_nums = sorted(nums)
        for i in range(0, int(len(sorted_nums) / 2)):
            for j in range(int(len(sorted_nums) / 2), len(sorted_nums)):
                sm = -(sorted_nums[i] + sorted_nums[j])
                start = 0
                sm_count = sorted_nums.count(sm)
                for k in range(0, sm_count):
                    ind = start + sorted_nums[start:].index(sm)
                    print(ind)
                    if i != ind and j != ind:
                        result.append(sorted([sorted_nums[i], sorted_nums[j], sorted_nums[ind]]))
                    start = ind + 1
        return list(set(tuple(i) for i in result))


s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSum([-1, 0, 1, 2, -1, -4, 5]))
print(s.threeSum([0, 0, 0]))
