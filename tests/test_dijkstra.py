import unittest
from dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):

    def setUp(self):
        # Graph represented as an adjacency matrix
        self.graph = [
            [0, 10, 0, 30, 100],
            [10, 0, 50, 0, 0],
            [0, 50, 0, 20, 10],
            [30, 0, 20, 0, 60],
            [100, 0, 10, 60, 0]
        ]
        self.dijkstra = Dijkstra(self.graph)

    def test_initialize_vectors(self):
        self.dijkstra.initialize(0)
        self.assertEqual(self.dijkstra.get_distances(), [0, float('inf'), float('inf'), float('inf'), float('inf')])
        self.assertEqual(self.dijkstra.get_visited(), [False, False, False, False, False])

    def test_find_min_distance_vertex(self):
        self.dijkstra.initialize(2)  # Start from a vertex other than 0
        self.dijkstra._distances = [float('inf'), 5, 10, float('inf'), 20]
        self.assertEqual(self.dijkstra.find_min_distance_vertex(), 1)

    def test_update_distances(self):
        self.dijkstra.initialize(0)
        self.dijkstra.update_distances(0)
        self.assertEqual(self.dijkstra.get_distances(), [0, 10, float('inf'), 30, 100])

    def test_find_shortest_path(self):
        path = self.dijkstra.find_shortest_path(0, 4)
        self.assertEqual(path, [0, 3, 2, 4])  # Expected shortest path

    def test_construct_path(self):
        self.dijkstra.initialize(0)
        self.dijkstra._previous = [None, 0, 1, None, 2]  # Set the predecessor list
        self.dijkstra._distances = [0, 10, 20, float('inf'), 30]  # Set the distances
        path = self.dijkstra.construct_path(4)
        self.assertEqual(path, [0, 1, 2, 4])  # Verify the reconstructed path

    def test_graph_without_edges(self):
        graph = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        dijkstra = Dijkstra(graph)
        path = dijkstra.find_shortest_path(0, 2)
        self.assertEqual(path, [])  # No possible path

    def test_graph_with_negative_weights(self):
        with self.assertRaises(ValueError):
            Dijkstra([
                [0, -1, 0],
                [-1, 0, 1],
                [0, 1, 0]
            ])  # Should raise an error due to negative weights

    def test_empty_graph(self):
        with self.assertRaises(ValueError):
            Dijkstra([])  # Should raise an error due to an empty graph

    def test_invalid_start_vertex(self):
        with self.assertRaises(ValueError):
            self.dijkstra.find_shortest_path(-1, 4)  # Invalid start vertex

    def test_invalid_end_vertex(self):
        with self.assertRaises(ValueError):
            self.dijkstra.find_shortest_path(0, 5)  # Invalid end vertex

if __name__ == "__main__":
    unittest.main()
