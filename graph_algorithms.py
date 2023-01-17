from collections import deque

graph = {
    "a":{"b":2,"h":15},
    "b":{"a":2,"c":1,"d":5},
    "c":{"b":1,"d":3,"f":2,"g":1},
    "d":{"b":5,"c":3,"f":4,"e":6},
    "e":{"d":6,"f":7,"i":2},
    "f":{"c":2,"d":4,"e":7,"g":1,"h":3},
    "g":{"c":1,"f":1},
    "h":{"a":15,"f":3,"i":12},
    "i":{"e":2,"h":12},
}

def dijkstra(graph, start):
    
    queue = deque()

    weights = {start:0}
    queue.append(start)
    
    while queue:

        vertex = queue.pop()
        edges = graph[vertex]
        
        for neighbour in edges:

            previous_weight = weights.get(neighbour,0)
            current_weight = weights[vertex] + graph[vertex][neighbour]
            
            if (neighbour not in weights) or (previous_weight > current_weight):
                weights[neighbour] = current_weight
                queue.appendleft(neighbour)

    return weights

def bfs(graph, start):

    visited = set()
    queue = deque()
    queue.append(start)

    while queue:
        vertex = queue.pop()
        for neighbour in graph[vertex]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            queue.appendleft(neighbour)







            



def main():
    pass


if __name__=="__main__":
    main()


