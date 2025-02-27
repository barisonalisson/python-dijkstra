class Dijkstra:
    def __init__(self, graph):
        self.validate_graph(graph)
        self._graph = graph  # Graph distance matrix

    def validate_graph(self, graph):
        if not graph or len(graph) == 0:
            raise ValueError("The graph cannot be empty.")
        for row in graph:
            if len(row) != len(graph):
                raise ValueError("The graph must be represented by a square matrix.")
            for weight in row:
                if weight < 0:
                    raise ValueError("The graph cannot have negative weights.")

    def initialize(self, start):
        if start < 0 or start >= len(self._graph):
            raise ValueError(f"Invalid start vertex: {start}.")
        num_vertices = len(self._graph)
        self._distances = [float('inf')] * num_vertices  # Initialize distances as infinite
        self._visited = [False] * num_vertices  # Mark visited vertices
        self._previous = [None] * num_vertices  # Track the path

        self._distances[start] = 0  # The starting vertex distance is 0

    def find_min_distance_vertex(self):
        min_distance = float('inf')
        current_vertex = -1

        for i in range(len(self._graph)):
            if not self._visited[i] and self._distances[i] < min_distance:
                min_distance = self._distances[i]
                current_vertex = i

        return current_vertex

    def update_distances(self, current_vertex):
        for neighbor in range(len(self._graph)):
            if self._graph[current_vertex][neighbor] != 0 and not self._visited[neighbor]:
                new_dist = self._distances[current_vertex] + self._graph[current_vertex][neighbor]
                if new_dist < self._distances[neighbor]:
                    self._distances[neighbor] = new_dist
                    self._previous[neighbor] = current_vertex

    def find_shortest_path(self, start, end):
        if end < 0 or end >= len(self._graph):
            raise ValueError(f"Invalid end vertex: {end}.")
        self.initialize(start)

        while True:
            current_vertex = self.find_min_distance_vertex()

            # If there are no more unvisited vertices or the current vertex is the destination
            if current_vertex == -1 or current_vertex == end:
                break

            self._visited[current_vertex] = True
            self.update_distances(current_vertex)

        return self.construct_path(end)

    def construct_path(self, end):
        path = []
        if self._distances[end] == float('inf'):
            return path  # Return an empty path if no possible path exists
        at = end
        while at is not None:
            path.append(at)
            at = self._previous[at]
        path.reverse()
        return path
    
    def get_distances(self):
        return self._distances

    def get_visited(self):
        return self._visited

    def get_previous(self):
        return self._previous
