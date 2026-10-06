import heapq

heuristic = {
    "S": 10,
    "A": 8,
    "B": 9,
    "C": 7,
    "H": 6,
    "G": 6,
    "D": 4,
    "E": 3,
    "F": 0
}

state_space_graph = {
    "S": [("A", 3), ("B", 2), ("C", 5)],
    "A": [("G", 2), ("C", 3)],
    "B": [("A", 5), ("D", 6)],
    "C": [("H", 3), ("B", 4)],
    "H": [("A", 4), ("D", 4)],
    "G": [("D", 4), ("E", 5)],
    "D": [("F", 3), ("E", 2)],
    "E": [("F", 5)],
    "F": []
}

def a_asterisk(start_state, goal_state):
    Full_list = [(heuristic[start_state], 0, start_state, [start_state])]
    Lowest_cost = {start_state: 0}

    while Full_list:
        x, y, current, path = heapq.heappop(Full_list)

        if current == goal_state:
            return path, y
        if y > Lowest_cost.get(current, float("inf")):
            continue
        for neighbor_node, cost in state_space_graph[current]:
            new_y = y + cost

            if new_y < Lowest_cost.get(neighbor_node, float("inf")):
                Lowest_cost[neighbor_node] = new_y

                new_x = new_y + heuristic[neighbor_node]
                heapq.heappush(
                    Full_list,
                    (new_x, new_y, neighbor_node, path + [neighbor_node])
                )

    return None, float("inf")
path, cost = a_asterisk("S", "F")
print("A^* Searching Path:", "Lowest Costing Path =", "->".join(path))
print("Total Cost:", cost)


