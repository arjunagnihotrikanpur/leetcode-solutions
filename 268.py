class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        expectedSum = sum(range(len(nums)+1))
        actualSum = sum(nums)

        return expectedSum - actualSum # missing number