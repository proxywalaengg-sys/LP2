import heapq


# ---------------- Selection Sort ----------------
def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        # Assume current index has minimum element
        min_index = i

        # Find minimum element in remaining array
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Pass {i + 1}: {arr}")

    return arr


# ---------------- Dijkstra Algorithm ----------------
def dijkstra(graph, start, n):

    dist = [float('inf')] * n
    dist[start] = 0

    pq = []

    heapq.heappush(pq, (0, start))

    while pq:

        current_dist, u = heapq.heappop(pq)

        for v, weight in graph[u]:

            if dist[v] > current_dist + weight:

                dist[v] = current_dist + weight

                heapq.heappush(pq, (dist[v], v))

    print("\nShortest Distances from Source Vertex:")

    for i in range(n):
        print(f"Vertex {i} -> Distance {dist[i]}")


# ---------------- Main Menu Program ----------------
def main():

    while True:

        print("\n===== MENU =====")
        print("1. Selection Sort")
        print("2. Dijkstra Algorithm")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        # -------- Selection Sort --------
        if choice == 1:

            n = int(input("Enter number of elements: "))

            arr = []

            print("Enter elements:")

            for i in range(n):
                arr.append(int(input()))

            print("\nOriginal Array:")
            print(arr)

            selection_sort(arr)

            print("\nSorted Array:")
            print(arr)

        # -------- Dijkstra Algorithm --------
        elif choice == 2:

            n = int(input("Enter number of vertices: "))
            e = int(input("Enter number of edges: "))

            graph = {i: [] for i in range(n)}

            print("Enter edges (u v weight):")

            for i in range(e):

                u, v, w = map(int, input().split())

                graph[u].append((v, w))
                graph[v].append((u, w))   # Remove for directed graph

            start = int(input("Enter source vertex: "))

            dijkstra(graph, start, n)

        # -------- Exit --------
        elif choice == 3:

            print("Exiting Program...")
            break

        else:

            print("Invalid Choice! Try Again.")


# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()
