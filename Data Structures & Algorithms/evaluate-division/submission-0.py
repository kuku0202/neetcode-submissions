class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        had = set()
        for equation, value in zip(equations, values):
            first, second = equation
            graph[first].append((second, value))
            graph[second].append((first, 1/value))
            had.add(first)
            had.add(second)
        
        def bfs(src, target):
            if src not in had or target not in had:
                return -1.0
            q = deque()
            q.append((src, 1))
            visited = set()
            visited.add(src)
            while q:
                cur, value = q.popleft()
                if cur == target:
                    return value
                for nei, mul in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, value * mul))
            return -1.0

        res = []
        for query in queries:
            res.append(bfs(query[0], query[1]))
        return res