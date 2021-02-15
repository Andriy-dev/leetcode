from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        print(graph)
        color = {}
        
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

s = Solution()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print("-"*50)
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print("-"*50)
print(s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
print("-"*50)
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2],[],[6],[5]]))
print("-"*50)
'''
0----1----3----2
'''
print(s.isBipartite([[1],[0,3],[3],[1,2]]))
print("-"*50)

'''
Traverse graph as a BFS with dictionary and *mark visited* ( node + neighbors)
Clear the add next unvisited to dictA and try again
until sum of lengths of dictionaries do not become == to len of graph
'''