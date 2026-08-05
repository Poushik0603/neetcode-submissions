class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashe = {}
        result = []
        for val in nums:
            if val in hashe:
                hashe[val] = hashe[val] + 1
            else:
                hashe[val] = 1
        hashe = dict(sorted(hashe.items(), key = lambda x:x[1],reverse=True)[:k])
        return list(hashe.keys())