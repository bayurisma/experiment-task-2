import random
import timeit

def Hamiltonian_with_dp(adj, N):
     
    dp = [[False for i in range(1 << N)] 
                 for j in range(N)]
 
    # Set all dp[i][(1 << i)] to
    # true
    for i in range(N):
        dp[i][1 << i] = True
 
    # Iterate over each subset
    # of nodes
    for i in range(1 << N):
        for j in range(N):
 
            # If the jth nodes is included
            # in the current subset
            if ((i & (1 << j)) != 0):
 
                # Find K, neighbour of j
                # also present in the
                # current subset
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                             adj[k][j] == 1 and
                                     j != k and
                          dp[k][i ^ (1 << j)]):
                         
                        # Update dp[j][i]
                        # to true
                        dp[j][i] = True
                        break
     
    # Traverse the vertices
    for i in range(N):
 
        # Hamiltonian Path exists
        if (dp[i][(1 << N) - 1]):
            return True
 
    # Otherwise, return false
    return False

def isSafe(adj, v, pos, path): 
    # Check if current vertex and last vertex 
    # in path are adjacent 
    if adj[ path[pos-1] ][v] == 0: 
        return False

    # Check if current vertex not already in path 
    for vertex in path: 
        if vertex == v: 
            return False

    return True

def hamPathUtil(adj, V, path, pos): 

    # base case: if all vertices are 
    # included in the path 
    if pos == V: 
        return True

    # Try different vertices as a next candidate 
    # in Hamiltonian Cycle. We don't try for 0 as 
    # we included 0 as starting point in hamCycle() 
    for v in range(1,V): 

        if isSafe(adj, v, pos, path) == True: 

            path[pos] = v 

            if hamPathUtil(adj, V, path, pos+1) == True: 
                return True

            # Remove current vertex if it doesn't 
            # lead to a solution 
            path[pos] = -1

    return False


def Ham_backtrack(adj, V): 

    for start in range(V):
        path = [-1] * V 
        path[0] = start

        if hamPathUtil(adj, V, path, 1) == True: 
            return True
    
    return False

def generate_adjacency_matrix(num_vertices, density=0.3):
    """
    Generate a random adjacency matrix for a graph.

    Parameters:
    - num_vertices: Total number of vertices in the graph.
    - density: Probability of having an edge between two vertices (default is 0.3).

    Returns:
    - A 2D list representing the adjacency matrix.
    """
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < density:
                # Randomly determine whether there is an edge based on the density
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1  # Since the graph is undirected

    return adjacency_matrix


def main():
    graph_size = [16, 18, 20]
    density = 0.5

    print("-----Dynamic Programming vs Backtracking-----\n")
    print("Algorithm            Data Size           Time(s)")
    print("================================================")

    for size in graph_size:
        adj_matrix = generate_adjacency_matrix(size, density)
        

        if (size == 16):


            start2 = timeit.default_timer()

            test = Ham_backtrack(adj_matrix, len(adj_matrix))
            print(f'Backtracking            Small           {(timeit.default_timer() - start2):.7f}')

            start1 = timeit.default_timer()

            test = Hamiltonian_with_dp(adj_matrix, len(adj_matrix))
            print(f'Dynamic Programming     Small           {(timeit.default_timer() - start1):.7f}')

            
        elif (size == 18):


            start2 = timeit.default_timer()

            test = Ham_backtrack(adj_matrix, len(adj_matrix))
            print(f'Backtracking            Medium          {(timeit.default_timer() - start2):.7f}')
            start1 = timeit.default_timer()

            test = Hamiltonian_with_dp(adj_matrix, len(adj_matrix))
            print(f'Dynamic Programming     Medium          {(timeit.default_timer() - start1):.7f}')

        elif (size == 20):

            start2 = timeit.default_timer()

            test = Ham_backtrack(adj_matrix, len(adj_matrix))
            print(f'Backtracking            Large           {(timeit.default_timer() - start2):.7f}')
            start1 = timeit.default_timer()

            test = Hamiltonian_with_dp(adj_matrix, len(adj_matrix))
            print(f'Dynamic Programming     Large           {(timeit.default_timer() - start1):.7f}')


if __name__=="__main__": 
    main() 