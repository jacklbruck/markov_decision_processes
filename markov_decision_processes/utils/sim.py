import pandas as pd
import numpy as np
import time


def simulate_policy(simulator, epochs=100, steps=int(1e4)):
    results = []

    for epoch in np.arange(epochs):
        start = time.time()
        reward, total, step = simulator.simulate(steps=steps)
        end = time.time()

        results.append((epoch, end - start, reward, total, step))

    return pd.DataFrame(data=results, columns=["Epoch", "Time", "Reward", "Total Reward", "Steps"])
