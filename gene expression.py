
import numpy as np

def objective(x):
    return (x - 5) ** 2

population = np.array([3, 4, 6, 7, 8, 9])

generations = 5

for generation in range(generations):

    fitness = np.array([objective(x) for x in population])

    sorted_indices = np.argsort(fitness)
    population = population[sorted_indices]

    parent1 = population[0]
    parent2 = population[1]

    child1 = (parent1 + parent2) // 2
    child2 = parent1 + (parent2 - parent1)

    child1 = max(0, child1)
    child2 = max(0, child2)

    population = np.array([
        parent1, parent2, child1, child2, 7, 3
    ])

    best = min(population, key=objective)

    print("Generation:", generation + 1,
          "Best Solution:", best,
          "Fitness:", objective(best))

print("\nOptimal Solution:", best)
print("Minimum Fitness:", objective(best))
