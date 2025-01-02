class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['u','e','a','o','i']
        tmp = [0]
        for i in range(len(words)):
            check =  (words[i][0] in vowel) and (words[i][-1] in vowel)
            tmp.append(tmp[i])
            tmp[i+1] += (1 if check else 0)

        res = []
        for l,r in queries:
            res.append(tmp[r+1]-tmp[l])
        return res
        