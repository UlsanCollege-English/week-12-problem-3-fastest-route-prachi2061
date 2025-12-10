import heapq

def dijkstra_shortest_path(graph, start, goal):
    """Return (path, total_cost) for the shortest weighted path in a graph."""

    if start not in graph or goal not in graph:
        return [], None

    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    parent = {node: None for node in graph}

    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]:
            continue

        if node == goal:
            break

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if dist[goal] == float("inf"):
        return [], None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return path, dist[goal]


if __name__ == "__main__":
    pass
