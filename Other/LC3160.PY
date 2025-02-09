class Solution(object):
    def queryResults(self, limit, queries):
        color = {}
        ball = {}
        count = 0
        res = []
        for b,c in queries:
            old_color = ball.get(b,0)
            if old_color == c:
                res.append(count)
                continue
            color[c] = color.get(c,0)+1
            if color[c] == 1: count+=1
            
            if old_color !=0: # draw to color ball
                # remove old color
                color[old_color] -=1
                if color[old_color] == 0:
                    count -=1
            
            # paint
            ball[b] = c
            # res
            res.append(count)
            print(ball,color,sep="----")
        return res
solution = Solution()
queries =[[1,4],[2,5],[1,3],[3,4]]
print(queries)
print(solution.queryResults(4,queries))