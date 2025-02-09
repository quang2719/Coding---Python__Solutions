class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dic = {}
        n = len(s)-1
        for i,x in enumerate(s):
            if x not in dic.keys():
                dic[x] = [i,i]
            else:
                dic[x] = [dic[x][0],i]
        iter = 0
        res = []
        
        while iter <= n:
            x = s[iter]
            right = dic[x][1]
            check = True
            while check:
                check = False
                elements = set(s[iter:right+1])
                for ele in elements:
                    if dic[ele][1] > right:
                        right = dic[ele][1]
                        check = True
            res.append(right-iter+1)
            iter = right+1
        return res

                
        
        