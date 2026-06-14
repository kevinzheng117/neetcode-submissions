class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0

        while i < n:
            pre = i + s[i:].index("#")
            s_length = int(s[i: pre])
            res.append(s[pre + 1: pre + 1 + s_length])
            i = pre + 1 + s_length
        
        return res