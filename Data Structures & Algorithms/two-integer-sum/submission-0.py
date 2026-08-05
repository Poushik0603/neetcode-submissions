class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        twosum = []
        n = len(nums)
        for i in range(0,n):
            if nums[i] in hash.values():
                index = nums.index((target - nums[i]))
                twosum.append(index)
                twosum.append(i)
            else:
                hash[i] = target - nums[i]
        return twosum
