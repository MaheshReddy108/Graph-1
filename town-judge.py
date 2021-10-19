
# Time Complexity O(V+E)

# Space Complexity O(V)

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d = [0]*n
        for t in trust:
            d[t[0]-1]-=1
            d[t[1]-1]+=1
        
        for i,j in enumerate(d):
            if j ==n-1:
                return i+1
        return -1
