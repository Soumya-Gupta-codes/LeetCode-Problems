class Solution(object):
    def sortedSquares(self, nums):
        result = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result