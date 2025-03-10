class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for x in magazine:
            chars[x] = chars.get(x,0) + 1
        for x in ransomNote:
            if x in chars:
                if chars[x] == 0: return False
                chars[x] -= 1
            else: return False
        return True