class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
           adj[a].append(b)
        visited = defaultdict(int)
        # Detect Cycle
        def dfs(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1
            for nei in adj[course]:
                if dfs(nei):
                    return True
            visited[course] = 2
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
