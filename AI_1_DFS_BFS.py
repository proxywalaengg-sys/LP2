# Practical: DFS and BFS with Path Finding (Undirected Graph)

from collections import deque

# ----------- Create Graph -----------
def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    
    for i in range(n):
        node = input(f"Enter node {i+1}: ")
        graph[node] = []
    
    e = int(input("Enter number of edges: "))
    
    for i in range(e):
        u = input("Enter first node of edge: ")
        v = input("Enter second node of edge: ")
        
        # Undirected Graph
        graph[u].append(v)
        graph[v].append(u)
    
    return graph


# ----------- DFS Traversal -----------
def dfs_traversal(graph, node, visited, traversal):
    visited.add(node)
    traversal.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited, traversal)


# ----------- DFS Path (Recursive) -----------
def dfs_path(graph, node, target, visited, parent):
    visited.add(node)
    
    if node == target:
        return True
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            parent[neighbor] = node
            if dfs_path(graph, neighbor, target, visited, parent):
                return True
    
    return False


# ----------- BFS Traversal -----------
def bfs_traversal(graph, start):
    visited = set()
    queue = deque()
    traversal = []
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        traversal.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal


# ----------- BFS Path -----------
def bfs_path(graph, start, target):
    visited = set()
    queue = deque()
    parent = {}
    
    queue.append(start)
    visited.add(start)
    parent[start] = None
    
    while queue:
        node = queue.popleft()
        
        if node == target:
            # Backtrack path
            path = []
            curr = target
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            
            path.reverse()
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    
    return None


# ----------- Main Menu -----------
def main():
    graph = create_graph()
    
    while True:
        print("\n----- MENU -----")
        print("1. DFS Traversal & Path")
        print("2. BFS Traversal & Path")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        # ----------- DFS -----------
        if choice == 1:
            start = input("Enter start node: ")
            target = input("Enter target node: ")
            
            # Traversal
            visited = set()
            traversal = []
            dfs_traversal(graph, start, visited, traversal)
            
            print("DFS Traversal:", traversal)
            
            # Path
            visited = set()
            parent = {}
            parent[start] = None
            
            found = dfs_path(graph, start, target, visited, parent)
            
            if found:
                path = []
                curr = target
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr]
                
                path.reverse()
                
                print("Target found!")
                print("Path:", path)
            else:
                print("Target not found!")
        
        
        # ----------- BFS -----------
        elif choice == 2:
            start = input("Enter start node: ")
            target = input("Enter target node: ")
            
            # Traversal
            traversal = bfs_traversal(graph, start)
            print("BFS Traversal:", traversal)
            
            # Path
            path = bfs_path(graph, start, target)
            
            if path:
                print("Target found!")
                print("Path:", path)
            else:
                print("Target not found!")
        
        
        # ----------- Exit -----------
        elif choice == 3:
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice!")


# ----------- Run Program -----------
main()
