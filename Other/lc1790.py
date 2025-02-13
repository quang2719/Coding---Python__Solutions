class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        l = -1
        r = -1
        tmp = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if l == -1: l = i
                elif r == -1: r = i
                else:
                    tmp = 1
                    break
        # more than 3 diff ele    
        if tmp == 1: return False

        # equal string
        if l == -1 and r == -1:
            return True

        if l!= -1 and r != -1:
            if s1[l] == s2[r] and s1[r] == s2[l]:
                return True
            return False
        return False
        