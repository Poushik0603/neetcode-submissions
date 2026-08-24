class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(left)
            left = left * nums[i]
        for i in range(n,0,-1):
            output[i-1] = output[i-1] * right
            right = right * nums[i-1]
        return output