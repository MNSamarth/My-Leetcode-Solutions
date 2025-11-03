class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1,l2=len(s),len(t)
        if(l1!=l2):
            return False
        c2={}
        for i in range(l1):
            if t[i] in c2:
                c2[t[i]]=c2[t[i]]+1
            else:
                c2[t[i]]=1
        for c in s:
            if c in c2:
                if c2[c]==0:
                    return False
                else:
                    c2[c]=c2[c]-1
            else:
                return False
        return True