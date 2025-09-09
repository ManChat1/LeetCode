class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # First run: {2 : 0}, then check if 2 exists and return its index along with 7's
        check = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in check:
                return[i, check[comp]]
            else:
                check[num] = i
        return False