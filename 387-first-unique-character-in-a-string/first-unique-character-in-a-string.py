class Solution:
    def firstUniqChar(self, s: str) -> int: 

        
        seen = set()

        for ch in s:
            if ch in seen:
                continue
            if s.count(ch) == 1:
                return s.index(ch)
            seen.add(ch)

        return -1