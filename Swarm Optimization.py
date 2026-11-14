
import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return (x - 5) ** 2

particles = np.array([1.0, 2.0, 8.0, 9.0])
velocities = np.array([0.0, 0.0, 0.0, 0.0])

w = 0.5
c1 = 1.0
c2 = 1.0

r1 = 1.0
r2 = 1.0

iterations = 10

pbest = particles.copy()
pbest_fitness = np.array([objective(x) for x in particles])

gbest_index = np.argmin(pbest_fitness)
gbest = pbest[gbest_index]

best_values = []

for iteration in range(iterations):

    for i in range(len(particles)):

        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest[i] - particles[i])
            + c2 * r2 * (gbest - particles[i])
        )

        particles[i] += velocities[i]

        current_fitness = objective(particles[i])

        if current_fitness < pbest_fitness[i]:
            pbest[i] = particles[i]
            pbest_fitness[i] = current_fitness

    gbest_index = np.argmin(pbest_fitness)
    gbest = pbest[gbest_index]

    best_values.append(objective(gbest))

    print("Iteration:", iteration + 1,
          "Best Solution:", round(gbest, 4),
          "Fitness:", round(objective(gbest), 6))

print("\nOptimal Solution:", round(gbest, 4))
print("Minimum Fitness:", round(objective(gbest), 6))

x = np.linspace(0, 10, 100)
y = objective(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', label='f(x) = (x-5)^2')
plt.scatter(gbest, objective(gbest),
            color='red', s=100, label='Optimal Solution')
plt.xlabel("X Values")
plt.ylabel("Objective Function")
plt.title("PSO - Function Optimization")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(range(1, iterations + 1), best_values,
         marker='o', color='green')
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title("PSO Convergence Graph")
plt.grid()
plt.show()
