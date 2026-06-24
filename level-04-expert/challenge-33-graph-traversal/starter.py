from collections import deque


class Graph:

    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []


    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)

        # Undirected connection
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)


    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])


    def bfs(self, start):
        if start not in self.adjacency_list:
            return []

        visited = set()
        queue = deque([start])
        result = []

        visited.add(start)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


    def dfs(self, start):
        if start not in self.adjacency_list:
            return []

        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                result.append(node)

                # reverse to maintain insertion order
                for neighbor in reversed(self.adjacency_list[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result


    def has_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return False

        return end in self.bfs(start)


    def shortest_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []

        if start == end:
            return [start]

        parent = {start: None}
        visited = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()

            if node == end:
                path = []

                while node is not None:
                    path.append(node)
                    node = parent[node]

                return list(reversed(path))


            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)

        return []
