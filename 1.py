# TWO SUM
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        ret = []
        for i in range(0, len(nums)):
            neededValue = target - nums[i]
            if (neededValue in hashMap):
                ret.append(hashMap[neededValue])
                ret.append(i)
                return ret
            else:
                hashMap[nums[i]] = i
            

# O(n) - HASHMAP SOLUTION