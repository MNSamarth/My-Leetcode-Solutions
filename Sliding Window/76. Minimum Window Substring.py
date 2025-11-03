class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_map=Counter(t)
        window_map={}
        need=len(need_map)
        have,left=0,0
        res,res_len=[-1,-1],len(s)+1
        for right,char in enumerate(s):
            window_map[char]=1+window_map.get(char,0)
            if char in need_map and window_map[char]==need_map[char]:
                have+=1
            while have==need:
                current_len=right-left+1
                if current_len<res_len:
                    res_len=current_len
                    res=[left,right]
                left_char=s[left]
                window_map[left_char]-=1
                if left_char in need_map and window_map[left_char]<need_map[left_char]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if res_len<len(s)+1 else ''