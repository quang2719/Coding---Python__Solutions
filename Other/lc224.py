class Solution:
    def calculate(self,s:str)->int:
        lst_s = [x for x in s if x != ' ']
        stack = []
        for i in range(len(lst_s)):
            if lst_s[i] ==')':
                tmp = []
                while stack:
                    x = stack.pop()
                    if x == '(':
                        break
                    tmp.insert(0,x)
                print('before handle:',tmp)
                res_tmp = self.handle(tmp)
                stack.append(res_tmp)
                print('done ',res_tmp)
            else:
                stack.append(lst_s[i])
        print('before last handle:',stack)
        res = self.handle(stack)
        print('done res',res)
        return res
    def handle(self,lst:list):
        # using to:
        # concat 2 int string: '2','3' -> 23
        # calculate math funcion, [2,'+',3] -> 5
        s = ''.join([str(x) for x in lst])
        s = '0'+ s

        math_expres = ['+','-']
        tmp = 0
        arr = []
        for i,x in enumerate(s):
            if x in math_expres:
                arr.append(int(s[tmp:i]))    
                arr.append(x)
                tmp = i+1
        arr.append(int(s[tmp:]))
        res = 0
        for i,x in enumerate(arr):
            if i==0:
                res += x
            elif x not in math_expres:
                res += (x if arr[i-1] == '+' else -x)
        return res