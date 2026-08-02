class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Calculate product of all elements to the left
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Multiply with product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer