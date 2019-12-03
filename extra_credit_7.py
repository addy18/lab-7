class Solution(object):
    def maxProduct(self, nums):
        curr = nums[0]
        maxi, mini = max(curr, 0), min(curr, 0)
        for i in range(1, len(nums)):
            number = nums[i]
            a, b = maxi*number, mini*number
            maxi, mini = max(a, b, max(number,0)),  min(a, b, min(number,0))
            curr = max(curr, maxi)
        return curr
