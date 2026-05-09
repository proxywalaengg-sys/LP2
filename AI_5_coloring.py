# Function to check if it's safe to assign color c to vertex v
def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


# Backtracking function
def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c

            if graph_coloring_util(graph, m, color, v + 1):
                return True

            color[v] = 0  # Backtrack

    return False


# Main function
def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    if not graph_coloring_util(graph, m, color, 0):
        print("No solution exists")
        return False

    print("\nSolution exists!")
    for i in range(n):
        print(f"Vertex {i} -> Color {color[i]}")
    return True


# ----------- User Input Section -----------

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix row by row:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

# Run algorithm
graph_coloring(graph, m)
