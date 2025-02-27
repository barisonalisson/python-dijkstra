from dijkstra import Dijkstra

def main():
    graph = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0]
    ]

    start, end = 0, 4  # Definir os vértices de origem e destino

    dijkstra = Dijkstra(graph)
    path = dijkstra.find_shortest_path(start, end)

    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Distances from start vertex: {dijkstra.get_distances()}")

if __name__ == "__main__":
    main()
