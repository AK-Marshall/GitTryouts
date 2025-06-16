from collections import deque
graph={}

graph['You']= ['Alice', 'Bob', 'Charlie']
graph['Alice'] = ['Bob', 'Cathy', 'Eve']
graph['Bob'] = ['Alice', 'Cathy', 'Dave']
graph['Charlie'] = ['Alice', 'Bob', 'Dave']

def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        person = queue.popleft()
        if person not in visited:
            visited.add(person)
            print(person)
            for neighbor in graph[person]:
                queue.append(neighbor)
    return visited

breadth_first_search( 'You')
