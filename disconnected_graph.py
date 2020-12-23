from typing import List

def split_graph(graph: List[List[int]]) -> List(List[List[int]])):
    ''' Getting a unidirectional graph as an argument, return List of connected graphs '''
    visited = [False]*len(graph)
    result = []

    while not all(visited):
        # Performing BFS starting from first not visited
        node = visited.index(False)

        current_graph = []
        current_visited = {}

        


