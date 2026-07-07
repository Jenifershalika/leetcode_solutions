class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        p_count = {}
        window = {}

        # Count characters in p
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        left = 0
        ans = []

        for right in range(len(s)):
            # Add current character
            window[s[right]] = window.get(s[right], 0) + 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # Check if current window is an anagram
            if window == p_count:
                ans.append(left)

        return ans