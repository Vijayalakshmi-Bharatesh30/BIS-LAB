
import numpy as np

distance = np.array([
    [0, 2, 5, 4],
    [2, 0, 3, 6],
    [5, 3, 0, 2],
    [4, 6, 2, 0]
])

n = len(distance)
ants = 4
iterations = 10
alpha = 1
beta = 2
evaporation = 0.5
Q = 100

pheromone = np.ones((n, n))

best_path = None
best_distance = float('inf')

for iteration in range(iterations):

    all_paths = []
    all_distances = []

    for ant in range(ants):

        path = [0]
        unvisited = list(range(1, n))

        while unvisited:

            current = path[-1]

            probabilities = []

            for city in unvisited:
                value = (
                    pheromone[current][city] ** alpha
                    * (1 / distance[current][city]) ** beta
                )
                probabilities.append(value)

            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]

            next_city = unvisited[
                np.argmax(probabilities)
            ]

            path.append(next_city)
            unvisited.remove(next_city)

        path.append(0)

        total_distance = sum(
            distance[path[i]][path[i + 1]]
            for i in range(len(path) - 1)
        )

        all_paths.append(path)
        all_distances.append(total_distance)

        if total_distance < best_distance:
            best_distance = total_distance
            best_path = path.copy()

    pheromone *= (1 - evaporation)

    for path, length in zip(all_paths, all_distances):
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length

    print("Iteration:", iteration + 1,
          "Best Distance:", best_distance)

print("\nBest Path:", best_path)
print("Shortest Distance:", best_distance)
