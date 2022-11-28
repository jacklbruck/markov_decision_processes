import numpy as np
import itertools
import argparse
import logging
import random

from .utils.mdp import make_frozen_lake, make_forest_management
from .learner import LearnerWrapper

mdps = {
    "0": "Frozen Lake",
    "1": "Forest Management",
}

algorithms = {
    "0": "Value Iteration",
    "1": "Policy Iteration",
    "2": "Q-Learning",
}


def run(mdp, algorithm):
    # Get MDP.
    if mdp == "Frozen Lake":
        T, R, map_ = make_frozen_lake()
    elif mdp == "Forest Management":
        T, R, map_ = make_forest_management()

    # Create learner.
    learner = LearnerWrapper(mdp, algorithm, T, R, map_=map_)
    learner.run()


def main(args):
    iterator = itertools.product(
        list(mdps.values()) if args.mdp == "*" else [mdps.get(args.mdp)],
        list(algorithms.values()) if args.algorithm == "*" else [algorithms.get(args.algorithm)],
    )

    for mdp, algorithm in iterator:
        run(mdp, algorithm)


if __name__ == "__main__":
    # Reproducability.
    random.seed(0)
    np.random.seed(0)

    # Configure logger.
    logging.basicConfig(level=logging.INFO)

    # Create argument parser.
    parser = argparse.ArgumentParser(description="Markov Decision Processes app.")
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str.lower,
        help="Choose which algorithm to run.",
        choices=["0", "1", "2", "*"],
    )
    parser.add_argument(
        "-m",
        "--mdp",
        type=str.lower,
        help="Choose which MDP to run.",
        choices=["0", "1", "*"],
    )

    # Parse arguments.
    args = parser.parse_args()

    # Run application.
    main(args)
