class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        max_idx, curr_max = 0, 0
        for i in range(n):
            id = nums[i] % n
            nums[id] += n
        
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
                max_idx = i
            
            nums[i] %= n
        
        return max_idx