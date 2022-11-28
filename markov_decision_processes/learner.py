import numpy as np
import logging

from hiive.mdptoolbox.mdp import PolicyIteration, ValueIteration, QLearning
from .config.params import PARAMS_DEFAULT, PARAMS_GRID
from .sim import Simulator
from pathlib import Path


algorithms = {
    "Q-Learning": QLearning,
    "Value Iteration": ValueIteration,
    "Policy Iteration": PolicyIteration,
}


class LearnerWrapper:
    def __init__(self, mdp, algorithm, T, R, map_=None):
        # Save parameters.
        self.mdp = mdp
        self.algorithm = algorithm
        self.T = T
        self.R = R
        self.map_ = map_

        # Create simulator.
        self.sim = Simulator(T, R, map_=map_)

        # Get experiment paramaters for specific learner.
        self.params = PARAMS_DEFAULT.get(algorithm).get(mdp)
        self.grids = PARAMS_GRID.get(algorithm)

    def save(self, params, learner, key):
        # Output value.
        out = {
            "mdp": self.mdp,
            "algorithm": self.algorithm,
            "params": params,
            "T": self.T,
            "R": self.R,
            "map_": self.map_,
            "policy": learner.policy,
            "time": learner.time,
            "iterations": learner.run_stat_frequency * len(learner.run_stats),
            "key": key,
        }

        # File path.
        fp = Path(__file__).parents[1] / "data" / out["mdp"] / out["algorithm"] / key / "out.npy"

        if not fp.parent.exists():
            fp.parent.mkdir(exist_ok=True, parents=True)

        np.save(fp, out)

    def run(self):
        for param, values in self.grids.items():
            for value in values:
                logging.info(f"Running {self.algorithm} on {self.mdp} with {param}={value}...")

                # Set parameters for run.
                params = self.params.copy()
                params.update({"transitions": self.T, "reward": self.R, param: value})

                if self.algorithm == "Q-Learning":
                    params.update({"iter_callback": self.sim.done})

                # Run learner.
                learner = algorithms.get(self.algorithm)(**params)
                learner.run()

                # Write output.
                self.save(params, learner, f"{param}={value}")
