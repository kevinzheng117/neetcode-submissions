class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        longest = 0

        for num in exists:
            if num - 1 not in exists:
                length = 1

                while num + length in exists:
                    length += 1

                longest = max(longest, length)

        return longest