# Recursive Function to print path of given vertex u from source vertex v
def printPath(path, v, u):
    if path[v][u] == v:
        return

    printPath(path, v, path[v][u])
    print(path[v][u], end=' ')


# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, N):
    for v in range(N):
        for u in range(N):
            if u != v and path[v][u] != -1:
                print(f"Shortest Path from {v} -> {u} is ({v}", end=' ')
                printPath(path, v, u)
                print(f"{u})")


# Function to run Floyd-Warshall algorithm
def floydWarshall(adjMatrix, N):
    # cost and parent matrix stores shortest-path
    # (shortest-cost/shortest route) information

    # initially cost would be same as weight of the edge
    cost = adjMatrix.copy()
    path = [[None for x in range(N)] for y in range(N)]
    result = ""
    # initialize cost and parent
    for v in range(N):
        for u in range(N):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1

    # run Floyd-Warshall
    for k in range(N):
        for v in range(N):
            for u in range(N):
                # If vertex k is on the shortest path from v to u,
                # then update the value of cost[v][u], path[v][u]
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]

            # if diagonal elements become negative, the
            # graph contains a negative weight cycle
            if cost[v][v] < 0:
                print("Negative Weight Cycle Found")
                return
        result += ("\n A{} is \n".format(k+1) + str(cost).replace("],", "]\n"))
    # Print the shortest path between all pairs of vertices
    print(result)
    printSolution(path, N)


if __name__ == '__main__':
    # Number of vertices in the adjMatrix
    N = 6
    M = float('inf')

    # given adjacency representation of matrix
    adjMatrix = [
        [0, M, M, M, -1, M],
        [1, 0, M, 2, M, M],
        [M, 2, 0, M, M, -8],
        [-4, M, M, 0, 3, M],
        [M, 7, M, M, 0, M],
        [M, 5, 10, M, M, 0]

    ]

    # Run Floyd Warshall algorithm
    floydWarshall(adjMatrix, N)
