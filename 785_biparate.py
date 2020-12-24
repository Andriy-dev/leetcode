from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        print(f"isBiparate({graph})")

        dA = dict()
        dB = dict()
        
        visited = [False]*len(graph)

        dA[0] = True
        
        while not all(visited):
            first_unvisited = visited.index(False)
            stack=[first_unvisited]

            dA[first_unvisited] = True

            ##print(f"Iteration {visited} first_unvisited={first_unvisited} dA={dA} dB={dB}")

            while stack:
                ##print(f"   node={node} dA.keys()={dA.keys()} dB.keys()={dB.keys()} visited[{node}]={visited[node]}")
                node = stack.pop()
                if not visited[node]:
                    ##print(f"  node={node}")
                    # 
                    #print(f"len(dA.keys()) = {len(dA.keys())} len(dB.keys())={len(dB.keys())} len(graph)={len(graph)}")
                    #
                    # Checking dA
                    ##print(f"  Start node={node} dA={dA} dB={dB} visited={visited}")
                    if node in dA.keys():
                        ##print(f"   node {node} in dA.keys()")
                        visited[node] = True
                        # Checking if neighboring vertices is in dB 
                        for neighbor_vertice in graph[node]:
                            if neighbor_vertice in dA.keys():
                                # Failure
                                return(False)
                            if neighbor_vertice not in dB.keys():
                                dB[neighbor_vertice] = True
                            stack.append(neighbor_vertice)
                    elif node in dB.keys():
                        visited[node] = True
                        ##print(f"   node {node} in dB.keys()")
                        # Checking if neighboring vertices is in dA 
                        for neighbor_vertice in graph[node]:
                            if neighbor_vertice in dB.keys():
                                # Failure
                                return(False)
                            if neighbor_vertice not in dA.keys():
                                dA[neighbor_vertice] = True   
                        stack.append(neighbor_vertice)
                    else:
                        assert "We should not end up here, something wrong with a logic"
                    #print("End",node,dA,dB)
                    #print()
        return(True)

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