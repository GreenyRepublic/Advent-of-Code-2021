from os import linesep
from typing import Deque, Dict, List, Set

inputFile = "12_Cave_Path_input.txt"
inputTestFile = "12_Cave_Path_test_input.txt"

def EnumerateRoutes(connections : Dict[str, List[str]], currentNode : str, currentPath : List[str] = [], currentVisited : Set[str]= set()) -> List[List[str]]:
    
    currentPath.append(currentNode)
    if currentNode == "end":
        return [currentPath]
        
    if currentNode.islower():
        currentVisited.add(currentNode)
    
    routes = []

    for node in connections[currentNode]:
        if node not in currentVisited:
            routes += (EnumerateRoutes(connections, node, list(currentPath), set(currentVisited)))

    return routes
    

def ParseInput(filename : str) -> Dict[str, List[str]]:    

    file = open(filename)
    nodes = dict()
    for line in file.readlines():
        start, end = line.strip().split('-')
        if start not in nodes:
            nodes[start] = []
        nodes[start].append(end)

        if end not in nodes:
            nodes[end] = []
        nodes[end].append(start)

    return nodes

def Main() -> None :

    caveNodes = ParseInput(inputFile)

    # Part 1
    routes = EnumerateRoutes(caveNodes, "start")
    print(str(len(routes)))

    
    # Part 2

    
Main()