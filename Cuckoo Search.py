
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def f(x):
    return x**2 + 4*x + 4

n = 25
iterations = 100
pa = 0.25
lower = -10
upper = 10
nests = np.random.uniform(lower, upper, n)
fitness = np.array([f(x) for x in nests])
best = nests[np.argmin(fitness)]
history = []

for t in range(iterations):
    for i in range(n):
        step = 0.01 * np.random.standard_cauchy()
        candidate = np.clip(nests[i] + step * (nests[i] - best), lower, upper)
        value = f(candidate)

        if value < fitness[i]:
            nests[i] = candidate
            fitness[i] = value

    abandon = np.random.rand(n) < pa
    nests[abandon] = np.random.uniform(lower, upper, np.sum(abandon))
    fitness = np.array([f(x) for x in nests])

    idx = np.argmin(fitness)
    if fitness[idx] < f(best):
        best = nests[idx]

    history.append(f(best))

print("Best Solution:", round(best, 6))
print("Minimum Function Value:", round(f(best), 6))

plt.plot(range(1, iterations + 1), history)
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title("Cuckoo Search Optimization")
plt.grid(True)
plt.show()
