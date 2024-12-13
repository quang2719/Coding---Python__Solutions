class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ''
        self.gen_str(n,n,cur,res)
        return res
    def gen_str(self,l,r,cur,res):
        if l < r:
            if l >= 1:
                self.gen_str(l-1,r,cur+'(',res)
            self.gen_str(l,r-1,cur+')',res)
        else: # only l == r are accepted
            if l >= 1:
                self.gen_str(l-1,r,cur+'(',res)
            else: #l==r ==0
                res.append(cur)
