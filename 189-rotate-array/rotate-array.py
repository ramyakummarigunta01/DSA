class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        rotated_arr=[0]*n
        for i in range(n):
            rotated_arr[(i+k)%n]=nums[i]
        nums[:]=rotated_arr[:]    