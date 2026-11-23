

import random
import math
import matplotlib.pyplot as plt

random.seed(7)

cities = {
    "A": (1, 5),
    "B": (3, 8),
    "C": (6, 7),
    "D": (8, 4),
    "E": (6, 1),
    "F": (3, 2)
}

names = list(cities)
n = len(names)
dist = [[math.dist(cities[a], cities[b]) for b in names] for a in names]
pheromone = [[1.0] * n for _ in range(n)]

ants = 20
iterations = 100
alpha = 1
beta = 5
evaporation = 0.5
Q = 100
best_route = None
best_length = float("inf")

for _ in range(iterations):
    routes = []

    for _ in range(ants):
        start = random.randrange(n)
        route = [start]
        unvisited = set(range(n))
        unvisited.remove(start)

        while unvisited:
            current = route[-1]
            choices = list(unvisited)
            weights = [
                pheromone[current][j] ** alpha *
                (1 / dist[current][j]) ** beta
                for j in choices
            ]
            next_city = random.choices(choices, weights=weights)[0]
            route.append(next_city)
            unvisited.remove(next_city)

        route.append(start)
        length = sum(dist[route[i]][route[i + 1]] for i in range(n))
        routes.append((route, length))

        if length < best_length:
            best_length = length
            best_route = route[:]

    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= 1 - evaporation

    for route, length in routes:
        for i in range(n):
            a, b = route[i], route[i + 1]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length

route_names = [names[i] for i in best_route]
points = [cities[name] for name in route_names]
x = [p[0] for p in points]
y = [p[1] for p in points]

print("Best Route:", " -> ".join(route_names))
print("Shortest Distance:", round(best_length, 2))

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker="o")

for name, (a, b) in cities.items():
    plt.annotate(name, (a, b), xytext=(5, 5),
                 textcoords="offset points")

plt.title("Ant Colony Optimization - TSP")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.tight_layout()
plt.show()
