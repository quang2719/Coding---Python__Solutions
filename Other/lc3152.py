class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def search_false_point(arr,l , r,query):
            if l > r:
                return False
            x,y = query
            mid = (l+r)//2
            if arr[mid] <= x:
                return search_false_point(arr, mid+1, r, (x,y))
            else:
                if arr[mid] <= y:
                    return True
                else:
                    return search_false_point(arr,l, mid-1, query)

        false_points = []
        for i in range(1,len(nums)):
            if (nums[i]+nums[i-1]) % 2 ==0:
                false_points.append(i)
        if len(false_points) == 0:
            return [True]*len(queries)
        
        res = []
        for l,r in queries:
            if search_false_point(false_points, 0, len(false_points)-1,(l,r)):
                res.append(False)
            else:
                res.append(True)
            
        
        return res