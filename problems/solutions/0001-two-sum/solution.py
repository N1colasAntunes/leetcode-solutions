#O(n2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for n in range(len(nums)):
            for i in range(n + 1, len(nums)):
                if nums[n] + nums[i] == target:
                    return [n, i]
        return []

#O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []