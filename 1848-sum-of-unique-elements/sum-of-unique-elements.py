class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        total = 0

        # Add only unique elements
        for num in freq:
            if freq[num] == 1:
                total += num

        return total
        