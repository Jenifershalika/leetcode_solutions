class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = sum(nums)

        if ones <= 1:
            return 0

        current = sum(nums[:ones])
        max_ones = current

        n = len(nums)

        for i in range(ones, n + ones):
            current += nums[i % n]
            current -= nums[(i - ones) % n]
            max_ones = max(max_ones, current)

        return ones - max_ones

        