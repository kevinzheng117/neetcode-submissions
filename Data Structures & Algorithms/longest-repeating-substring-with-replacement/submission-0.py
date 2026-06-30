class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        best = 0
        freqMap = defaultdict(int)
        l = 0

        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best