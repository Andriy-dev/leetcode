from typing import List

def traversal(graph: List[List[int]]),source):


def split_graph(graph: List[List[int]]) -> List[List[List[int]]] :
    ''' Getting a unidirectional graph as an argument, return List of connected graphs '''
    visited = [False]*len(graph)
    result = []

    while not all(visited):
        # Performing inorder traversal starting from first not visited
        node = visited.index(False)

        # [ [List] [List] [List] ]
        
        stack = [node]
        localgraph = []

        while stack:
            node = stack.pop()
            if node not in graph:
                localgraph.append(node)
            for leaf in graph[node]
        


