
import numpy as np

# 1. Define objective function
def objective(x):
    return x ** 2

# 2. Initialize parameters
population_size = 6
generations = 20
crossover_rate = 0.8
mutation_rate = 0.1

# 3. Fixed initial population (no random input)
population = np.array([8, 6, 4, 2, -5, -3])

# 4. Fitness function
def fitness(x):
    return 1 / (1 + objective(x))

# 5. Selection
def selection(population):
    sorted_population = sorted(
        population, key=lambda x: objective(x)
    )
    return sorted_population[0], sorted_population[1]

# 6. Crossover
def crossover(p1, p2):
    if crossover_rate >= 0.8:
        child1 = (p1 + p2) / 2
        child2 = (p1 + p2) / 2
        return child1, child2
    return p1, p2

# 7. Mutation (fixed mutation value)
def mutation(child):
    if child > 0:
        child = child - 1
    elif child < 0:
        child = child + 1
    return child

# 8. Main Genetic Algorithm
best_solution = None
best_value = float('inf')

for generation in range(generations):

    new_population = []

    p1, p2 = selection(population)

    child1, child2 = crossover(p1, p2)

    child1 = mutation(child1)
    child2 = mutation(child2)

    new_population.extend([p1, p2, child1, child2])

    # Elitism and population update
    new_population = sorted(
        new_population, key=lambda x: objective(x)
    )

    population = np.array(new_population[:population_size])

    # Find best solution
    current_best = min(population, key=objective)

    if objective(current_best) < best_value:
        best_solution = current_best
        best_value = objective(current_best)

    print("Generation:", generation + 1,
          "Best Solution:", best_solution,
          "Fitness:", best_value)

# 9. Display result
print("\nOptimal Solution:", best_solution)
print("Minimum Objective Value:", best_value)
