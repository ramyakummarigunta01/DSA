class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s=" ".join(char.lower() for char in s if char.isalnum())
        lst=list(new_s)[::-1]
        rev_s="".join(lst)
        return new_s==rev_s
        