
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def f(x):
    return x**2 + 4*x + 4

size = 20
iterations = 100
lower = -10
upper = 10

cells = np.random.uniform(lower, upper, size)
history = []

for t in range(iterations):
    new_cells = cells.copy()

    for i in range(size):
        left = cells[(i - 1) % size]
        right = cells[(i + 1) % size]
        candidates = [cells[i], left, right]
        best = min(candidates, key=f)
        new_cells[i] = np.clip(best + np.random.uniform(-0.1, 0.1), lower, upper)

    cells = new_cells
    history.append(min(cells, key=f))

best = min(cells, key=f)

print("Best Solution:", round(best, 6))
print("Minimum Function Value:", round(f(best), 6))

plt.plot(range(1, iterations + 1), [f(x) for x in history])
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title("Parallel Cellular Algorithm Optimization")
plt.grid(True)
plt.show()
