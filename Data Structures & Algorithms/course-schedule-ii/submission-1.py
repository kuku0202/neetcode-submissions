class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq = {c: [] for c in range(numCourses)}
        # for crs, pre in prerequisites:
        #     prereq[crs].append(pre)
        
        # output = []
        # visit, cycle = set(), set()

        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     if crs in visit:
        #         return True
            
        #     cycle.add(crs)
        #     for pre in prereq[crs]:
        #         if dfs(pre) == False:
        #             return False
        #     cycle.remove(crs)
        #     visit.add(crs)
        #     output.append(crs)
        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        # return output

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)


        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        
        return output[::-1]