class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target: return True
        s_dic = []
        e_dic = []
        for i in range(len(start)):
            if start[i]!= '_':
                s_dic.append([start[i],i])
            if target[i] != '_':
                e_dic.append([target[i],i])
        i,j = 0,len(s_dic)-1
        if len(s_dic) != len(e_dic): return False

        while i < len(s_dic):
            val_s,iter_s = s_dic[i]
            val_e,iter_e = e_dic[i]
            if val_s != val_e: return False

            if val_s == 'L':
                if iter_s < iter_e: return False
                elif iter_s == iter_e: 
                    i+=1
                    continue
                else:
                    if i == 0:
                        iter_s = iter_e
                    else:
                        if iter_e > s_dic[i-1][1]:
                            iter_s = iter_e
                        else: return False
                    s_dic[i][1] = iter_s
            i+=1
        
        while j >=0:
            val_s,iter_s = s_dic[j]
            val_e,iter_e = e_dic[j]

            if val_s == 'R':
                if iter_s > iter_e: return False
                elif iter_s == iter_e: 
                    j-=1
                    continue
                else:
                    if j == len(s_dic)-1:
                        iter_s = iter_e
                    else:
                        if iter_e < s_dic[j+1][1]:
                            iter_s = iter_e
                        else: return False
                    s_dic[j][1] = iter_s
            j-=1
        return True
