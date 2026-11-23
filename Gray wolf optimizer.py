
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def f(x):
    return x**2 + 4*x + 4

n = 30
iterations = 100
lower = -10
upper = 10

wolves = np.random.uniform(lower, upper, n)
alpha = beta = delta = 0
history = []

for t in range(iterations):
    fitness = np.array([f(x) for x in wolves])
    order = np.argsort(fitness)
    alpha, beta, delta = wolves[order[0]], wolves[order[1]], wolves[order[2]]
    a = 2 - 2 * t / iterations

    new_wolves = []

    for wolf in wolves:
        positions = []

        for leader in [alpha, beta, delta]:
            r1, r2 = np.random.rand(), np.random.rand()
            A = 2 * a * r1 - a
            C = 2 * r2
            D = abs(C * leader - wolf)
            positions.append(leader - A * D)

        new_wolves.append(np.clip(np.mean(positions), lower, upper))

    wolves = np.array(new_wolves)
    history.append(f(alpha))

best = wolves[np.argmin([f(x) for x in wolves])]

print("Best Solution:", round(best, 6))
print("Minimum Function Value:", round(f(best), 6))

plt.plot(range(1, iterations + 1), history)
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title("Grey Wolf Optimizer")
plt.grid(True)
plt.show()
