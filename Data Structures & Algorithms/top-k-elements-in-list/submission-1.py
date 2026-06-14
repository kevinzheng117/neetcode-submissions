class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        sortedKeys = sorted(freqMap, key=freqMap.get, reverse=True)

        return sortedKeys[:k]