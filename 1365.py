class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hashmap = {}
        temp = sorted(nums)
        ret = []

        for index, element in enumerate(temp):
            if element not in hashmap:
                hashmap[element] = index
            
        for i in nums:
            ret.append(hashmap[i])

        return ret