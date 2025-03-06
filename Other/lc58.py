class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        print(len(words[-1]))
        
s =  "   fly me   to   the moon  "
words = s.strip().split(" ")
print(words)
print(len(words[-1]))