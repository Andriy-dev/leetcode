from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        dA = dict()
        dB = dict()
        
        dA[0] = True
        
        for node in range(len(graph)):
            # 
            print(f"len(dA.keys()) = {len(dA.keys())} len(dB.keys())={len(dB.keys())} len(graph)={len(graph)}")
            #
            # Checking dA
            print("Start",node,dA,dB)
            if node in dA.keys():
                # Checking if neighboring vertices is in dB 
                for neighbor_vertice in graph[node]:
                    if neighbor_vertice in dA.keys():
                        # Failure
                        return(False)
                    if neighbor_vertice not in dB.keys():
                        dB[neighbor_vertice] = True
            elif node in dB.keys():
                # Checking if neighboring vertices is in dA 
                for neighbor_vertice in graph[node]:
                    if neighbor_vertice in dB.keys():
                        # Failure
                        return(False)
                    if neighbor_vertice not in dA.keys():
                        dA[neighbor_vertice] = True   
            print("End",node,dA,dB)
            print()
        return(True)

s = Solution()
#print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))

#print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

print(s.isBipartite(
[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))