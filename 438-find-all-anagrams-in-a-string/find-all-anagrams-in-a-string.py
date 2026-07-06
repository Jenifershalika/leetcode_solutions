class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        # Store frequency of characters in p
        for ch in p:
            index = ord(ch) - ord('a')
            p_count[index] += 1

        left = 0
        ans = []

        for right in range(len(s)):
            # Add current character to window
            index = ord(s[right]) - ord('a')
            window[index] += 1

            # If window becomes larger than p
            if right - left + 1 > len(p):
                index = ord(s[left]) - ord('a')
                window[index] -= 1
                left += 1

            # Compare frequencies
            if window == p_count:
                ans.append(left)

        return ans
        