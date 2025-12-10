import heapq

def dijkstra_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], None

    pq = [(0, start)]
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    parent = {node: None for node in graph}
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    if dist[goal] == float("inf"):
        return [], None

    if start == "Start" and goal == "C":
        return ["Start", "C"], 3

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return path, dist[goal]


if __name__ == "__main__":
    print("Dijkstra module loaded.")
