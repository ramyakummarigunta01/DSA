class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result =[]
        m=len(nums1)
        n=len(nums2)
        if m>n:
            for num in nums1:
                if(num in nums2) and (num not in result):
                    result.append(num)
        else:
            for num in nums2:
                if(num in nums1) and (num not in result):
                    result.append(num)
        return result            