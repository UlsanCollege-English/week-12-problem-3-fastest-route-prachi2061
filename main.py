import heapq

def dijkstra_shortest_path(graph, start, goal):
    """
    Compute the shortest path in a graph with positive edge weights.

    graph: dict mapping node -> list of (neighbor, weight) pairs.
    start: starting node (string).
    goal: target node (string).

    Return:
        (path, total_cost)
        - path: list of nodes from start to goal with minimum total weight
        - total_cost: sum of weights along the path
        If start/goal is not in graph or goal is unreachable, return ([], None).
    """
    if start not in graph or goal not in graph:
        return [], None
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    # Distance dictionary
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    # Parent dictionary for path reconstruction
    parent = {node: None for node in graph}
    # Visited set
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == goal:
            break
        
        for neighbor, weight in graph.get(current_node, []):
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))
    
    # Reconstruct path if goal is reachable
    if dist[goal] == float('inf'):
        return [], None
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    return path, dist[goal]

if __name__ == "__main__":
    # Optional quick check
    sample_graph = {
        "K1": [("K2", 5), ("K3", 2)],
        "K2": [("K1", 5), ("K4", 4)],
        "K3": [("K1", 2), ("K4", 7)],
        "K4": [("K2", 4), ("K3", 7)],
    }
    path, cost = dijkstra_shortest_path(sample_graph, "K1", "K4")
    print("Sample path from K1 to K4:", path, "cost:", cost)
