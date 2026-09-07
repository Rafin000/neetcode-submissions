class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefixArr = [1] * size
        suffixArr = [1] * size

        prefixArr[0] = nums[0]
        suffixArr[size-1] = nums[size-1]

        for i in range(1 , size):
            prefixArr[i] = prefixArr[i-1] * nums[i]
        
        for i in range(size-2, -1 , -1):
            suffixArr[i] = suffixArr[i+1] * nums[i]

        result = []

        for i in range(size):
            left = prefixArr[i-1] if i > 0 else 1
            right = suffixArr[i+1] if i < size-1 else 1
            result.append(left*right)

        return result
            

