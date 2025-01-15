class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def decToBi(num):
                res = []
                while num:
                    res.append(str(num%2))
                    num//=2
                return "".join(res[::-1])
        def biToDec(num):
            res = 0
            cnt = 0
            for i in range(len(num)-1,-1,-1):
                res += (int(num[i]))*(2**cnt)
                cnt+=1
            return res
        bi_n2 = decToBi(num2)
        count_1_n2 = sum([1 for x in bi_n2 if x =='1'])
        bi_n1 = decToBi(num1)
        count_1_n1 = sum([1 for x in bi_n1 if x=='1'])
        if count_1_n2 == count_1_n1: return num1


        added = count_1_n2 - count_1_n1
        # padding
        if len(bi_n1) <= len(bi_n2):
            bi_n1 = "".join(
                ["0"]*(len(bi_n2) - len(bi_n1))
            ) + bi_n1
        else:
            bi_n2 = "".join(
                ["0"]*(len(bi_n1) - len(bi_n2))
            ) + bi_n2
        res = [x for x in bi_n1]
        if added >0:
            #add 1 from the end if num of 1 in n2 > n1
            for i in range(len(bi_n1)-1,-1,-1):
                if added == 0: break
                if bi_n1[i] == '0':
                    res[i] = '1'
                    added -=1
        else:
            #remove 1 from the end if num of 1 in n2 > n1
            for i in range(len(bi_n1)-1,-1,-1):
                if added == 0: break
                if bi_n1[i] == '1':
                    res[i] = '0'
                    added +=1
        return biToDec("".join(res))
                     


solution = Solution()
print(solution.minimizeXor(25,72))