# O(n) : linear
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        arrSet = set(nums)
        if (len(arrSet) != len(nums)):
            return True
        else:
            return False

