class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        frequent = sorted(zip(list(count.keys()), list(count.values())), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(frequent[i][0])
        
        return result