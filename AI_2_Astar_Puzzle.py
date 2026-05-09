# A* Algorithm for 8 Puzzle Problem (Dynamic Input)

import heapq


# Goal State
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Node Class
class Node:

    def __init__(self, state, parent, g, h):

        self.state = state
        self.parent = parent
        self.g = g          # Cost from start
        self.h = h          # Heuristic cost
        self.f = g + h      # Total cost

    def __lt__(self, other):
        return self.f < other.f


# Heuristic Function (Manhattan Distance)
def heuristic(state):

    distance = 0

    for i in range(3):
        for j in range(3):

            value = state[i][j]

            if value != 0:

                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3

                distance += abs(i - goal_x) + abs(j - goal_y)

    return distance


# Find blank tile position
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                return i, j


# Convert state to tuple for hashing
def state_to_tuple(state):

    return tuple(tuple(row) for row in state)


# Generate neighboring states
def get_neighbors(state):

    neighbors = []

    x, y = find_blank(state)

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]

            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


# Print solution path
def print_path(node):

    path = []

    while node:
        path.append(node.state)
        node = node.parent

    path.reverse()

    print("\nSolution Steps:\n")

    step = 0

    for state in path:

        print("Step", step)

        for row in state:
            print(row)

        print()

        step += 1


# A* Algorithm
def a_star(start_state):

    open_list = []

    closed_set = set()

    start_node = Node(
        start_state,
        None,
        0,
        heuristic(start_state)
    )

    heapq.heappush(open_list, start_node)

    while open_list:

        current = heapq.heappop(open_list)

        # Goal Check
        if current.state == GOAL_STATE:

            print("\nGoal State Reached!")
            print("Total Moves =", current.g)

            print_path(current)
            return

        closed_set.add(state_to_tuple(current.state))

        # Generate neighbors
        for neighbor in get_neighbors(current.state):

            if state_to_tuple(neighbor) in closed_set:
                continue

            neighbor_node = Node(
                neighbor,
                current,
                current.g + 1,
                heuristic(neighbor)
            )

            heapq.heappush(open_list, neighbor_node)

    print("No Solution Found")


# Main Function
def main():

    print("Enter the initial state row-wise")
    print("Use 0 for blank space\n")

    start_state = []

    for i in range(3):

        row = list(map(int, input().split()))

        start_state.append(row)

    print("\nInitial State:")

    for row in start_state:
        print(row)

    a_star(start_state)


if __name__ == "__main__":
    main()
