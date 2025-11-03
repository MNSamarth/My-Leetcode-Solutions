class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_freq=0
        max_len=0
        for right in range(len(s)):
            char=s[right]
            count[char]=1+count.get(char,0)
            max_freq=max(max_freq,count[char])
            window_length=right-left+1
            if window_length - max_freq>k:
                left_char=s[left]
                count[s[left]]-=1
                left+=1
        max_len=max(max_len,right-left+1)
        return max_len
