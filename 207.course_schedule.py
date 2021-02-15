'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # building graph ( as dictionary node->neighbors)
        # looking for cycles in graph. ( may be multiple passes )
        #   find the vertice with only egress edges
        #   start DFS from there 
        #   store the full path in the stack, to detect the loops
        #   if hit the "visited" node , pull the next one from the stack
        stack =[]

        graph={} 
        reverse_graph={}

        for vertice in range(numCourses):
            graph[vertice]=[]
            reverse_graph[vertice]=[]

        for edge in prerequisites:  # ( a, b ) b is prereq for a ; b->a
            graph[edge[1]].append(edge[0])
            reverse_graph[edge[0]]=[edge[0]]

        visited=[False]*numCourses

        while not all(visited):
            #print(visited,graph,stack)
            # Looking for the vertice with egress edges only
            if not stack:
                # Looking for the vertice with egress edges only
                #candidates = [ c for c in reverse_graph.keys() if not visited[c] and reverse_graph[c]==[]  ]
                for candidate in reverse_graph.keys():
                    if not visited[candidate] and reverse_graph[candidate]==[]:
                        stack.append([candidate,set()])
                        break
                if not stack:
                    #print("Cant find any nodes without egress edges",reverse_graph,visited)
                    return(False)    
               
            #print(visited,graph,stack)
            #print()
            while stack:
                # starting dfs traversal
                node,path = stack.pop()
                #print("extracted node",node,"remaining stack",stack,"visited",visited)
                visited[node] = True
                if node in graph:
                    for neighbor in graph[node]:
                        if neighbor in path:
                            #print("Loop detected")
                            return(False)
                        if not visited[neighbor]:
                            stack.append([neighbor,path | {node}])

        return (True)

s = Solution()

#print(s.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))
#print("Expected True")

print(s.canFinish(2,[[1,0],[0,1]]))
print("Expected False")

#print(s.canFinish(3,[[2,1],[1,0]]))
#print("Expected True")