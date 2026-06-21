class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # Rotation=k%n
        # for _ in range(Rotation):
        #     last_ele=nums.pop()
        #     nums.insert(0,last_ele)
        n = len(nums)
        k = k % n

        # Reverse entire array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])

