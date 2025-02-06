class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        color: 
        0 - not visit
        1 - visiting
        2 - visited
        """
        adj = {x:[] for x in range(numCourses)}
        for i,j in prerequisites:
            adj[i].append(j)
        color = {x:0 for x in range(numCourses)}
        circle = False
        
        for x in range(numCourses):
            if circle: break
            if color[x] ==0:
                recStack = []
                # travel
                stack = [x]
                while stack:
                    cur = stack.pop(0)
                    


        return not circle