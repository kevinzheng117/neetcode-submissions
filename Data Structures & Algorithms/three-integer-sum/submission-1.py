class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairsMap = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pairsMap[nums[i] + nums[j]].append((i, j))

        seen = set()

        for k in range(len(nums)):
            target = -nums[k]

            for i, j in pairsMap[target]:
                if k != i and k != j:
                    trip = tuple(sorted([nums[i], nums[j], nums[k]]))
                    seen.add(trip)

        return [list(trip) for trip in seen]