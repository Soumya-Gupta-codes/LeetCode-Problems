class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0] * n

        positive_index = 0
        negative_index = 1

        for num in nums:
            if num > 0:
                ans[positive_index] = num
                positive_index += 2
            else:
                ans[negative_index] = num
                negative_index += 2

        return ans