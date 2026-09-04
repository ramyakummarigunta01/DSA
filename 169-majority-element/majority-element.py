class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=dict()
        for num in nums:
            if num in freq:freq[num]+=1
            else:freq[num]=1
            if freq[num]>len(nums)//2: return num        