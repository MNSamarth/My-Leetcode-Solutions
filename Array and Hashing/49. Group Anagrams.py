class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash={}
        t=""
        for s in strs:
            t=str(sorted(s))
            # print(t)
            if t in hash:
                hash[t].append(s)
            else:
                hash[t]=[s]
        return hash.values()