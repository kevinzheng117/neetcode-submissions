class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = defaultdict(list)

        for s in strs:
            sortedS = str(sorted(s))
            anagramsMap[sortedS].append(s)

        return list(anagramsMap.values())