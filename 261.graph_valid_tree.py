class Solution:
    def validTree(self, n, edges):
        #
        # Graph is a valid tree if:
        #   * It does not have any loops
        #   * We can visit all nodes from root
        #
        # Perform BFS traversal, keep track of "visited", ignore if thats a parent
        # Upon completion check if all nodes were visited
        #
        if n==0:
            return True

        graph_matrix = [[] for _ in range(n) ]
        for edge in edges:
            graph_matrix[edge[0]].append(edge[1])
            graph_matrix[edge[1]].append(edge[0])

        visited=[False]*n

        s = []
        s.append([None,0])

        while s:
            parent,node = s.pop()
            for neighbor in range(n):
                if neighbor in graph_matrix[node]:
                    if neighbor != parent:
                        if visited[neighbor]:
                            return False
                        else:
                            s.append([node,neighbor])
            visited[node] = True
        
        return all(visited)


s = Solution()

print(s.validTree(5,[[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree(5,[[0,1], [1,2], [2,3], [1,3], [1,4]]))
