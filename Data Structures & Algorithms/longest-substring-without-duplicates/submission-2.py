class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        currC, maxC = 0, 0
        l = 0

        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
                currC -= 1

            seen.add(s[r])
            currC += 1
            maxC = max(maxC, currC)
        
        return maxC
