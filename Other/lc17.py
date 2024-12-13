class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
        }
        init_str = ''
        res = []
        self.gen_string(init_str,digits,0,res,keyboard)
        return res
    def gen_string(self,s,digits,i,res, keyboard):
        if i == len(digits):
            if len(s) >0:
                res.append(s)
            return
        if digits[i] == '1': return gen_string(s,digits,i+1,res,keyboard)
        for x in keyboard[digits[i]]:
            s = s + x
            self.gen_string(s,digits,i+1,res,keyboard)
            s = s[:-1]