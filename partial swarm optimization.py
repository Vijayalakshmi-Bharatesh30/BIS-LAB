
def objective(x):
    return x ** 2

particles = [8.0, 6.0, 4.0, 2.0]
velocities = [0.0, 0.0, 0.0, 0.0]

w = 0.5
c1 = 1.0
c2 = 1.0

iterations = 10
r1 = 1.0
r2 = 1.0

pbest = particles.copy()
pbest_value = [objective(x) for x in particles]

gbest_index = pbest_value.index(min(pbest_value))
gbest = pbest[gbest_index]

for iteration in range(iterations):

    for i in range(len(particles)):

        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest[i] - particles[i])
            + c2 * r2 * (gbest - particles[i])
        )

        particles[i] += velocities[i]

        current_fitness = objective(particles[i])

        if current_fitness < pbest_value[i]:
            pbest[i] = particles[i]
            pbest_value[i] = current_fitness

    gbest_index = pbest_value.index(min(pbest_value))
    gbest = pbest[gbest_index]

    print("Iteration:", iteration + 1,
          "Best Solution:", round(gbest, 4),
          "Best Fitness:", round(objective(gbest), 6))

print("\nOptimal Solution:", round(gbest, 4))
print("Minimum Function Value:", round(objective(gbest), 6))
