class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=(''.join([char for char in s if char.isalnum()]).lower()).strip()
        temp=len(s)
        for i in range(len(s)):
            if s[i]!=s[temp-1]:
                return False
            else:
                temp-=1
        return True