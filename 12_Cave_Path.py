from os import linesep
from typing import Deque, Dict, List, Set

inputFile = "12_Cave_Path_input.txt"
inputTestFile = "12_Cave_Path_test_input.txt"

def EnumerateRoutes(connections : Dict[str, List[str]], currentNode : str, currentPath : List[str] = [], currentVisited : Set[str]= set(), canVisitTwice : bool = False, hasVisitedTwice : bool = False) -> List[List[str]]:
    
    currentPath.append(currentNode)
    if currentNode == "end":
        return [currentPath]
        
    if currentNode.islower():
        if currentNode in currentVisited and currentNode != "start":
            hasVisitedTwice = True
        currentVisited.add(currentNode)
    
    routes = []

    for node in connections[currentNode]:
        if (node not in currentVisited) or (canVisitTwice and not hasVisitedTwice) and node != "start":
            routes += (EnumerateRoutes(connections, node, list(currentPath), set(currentVisited), canVisitTwice, hasVisitedTwice))

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
    routesOne = EnumerateRoutes(caveNodes, "start", canVisitTwice=False)
    print(str(len(routesOne)))
    
    # Part 2
    routesTwo = EnumerateRoutes(connections=caveNodes, currentNode="start", canVisitTwice=True)
    print(str(len(routesTwo)))

    
Main()