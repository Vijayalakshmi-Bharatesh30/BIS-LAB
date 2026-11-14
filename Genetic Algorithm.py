
import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return (x - 5) ** 2

population = np.array([1, 2, 3, 7, 8, 9])

generations = 10
best_values = []

best_solution = None
best_fitness = float('inf')

for generation in range(generations):

    fitness = np.array([objective(x) for x in population])

    sorted_indices = np.argsort(fitness)
    population = population[sorted_indices]

    parent1 = population[0]
    parent2 = population[1]

    child1 = (parent1 + parent2) // 2
    child2 = parent1 + (parent2 - parent1)

    child1 = child1 + 1 if child1 < 5 else child1 - 1

    new_population = np.array([
        parent1, parent2, child1, child2, 7, 3
    ])

    population = new_population

    current_best = min(population, key=objective)

    if objective(current_best) < best_fitness:
        best_fitness = objective(current_best)
        best_solution = current_best

    best_values.append(best_fitness)

    print("Generation:", generation + 1,
          "Best Solution:", best_solution,
          "Fitness:", best_fitness)

print("\nOptimal Solution:", best_solution)
print("Minimum Fitness:", best_fitness)

x = np.linspace(0, 10, 100)
y = objective(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', label='f(x) = (x-5)^2')
plt.scatter(best_solution, best_fitness,
            color='red', s=100, label='Optimal Solution')
plt.xlabel("X Values")
plt.ylabel("Objective Function")
plt.title("Genetic Algorithm - Function Optimization")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(range(1, generations + 1), best_values,
         marker='o', color='green')
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Genetic Algorithm Convergence Graph")
plt.grid()
plt.show()
