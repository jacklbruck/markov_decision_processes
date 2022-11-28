PARAMS_DEFAULT = {
    "Q-Learning": {
        "Frozen Lake": {
            "gamma": 0.90,
            "alpha": 0.1,
            "epsilon": 1.0,
            "alpha_decay": 1.0,
            "epsilon_decay": 0.99,
            "alpha_min": 0.001,
            "epsilon_min": 0.1,
            "n_iter": int(1e6),
            "skip_check": False,
        },
        "Forest Management": {
            "gamma": 0.999,
            "alpha": 0.1,
            "epsilon": 1.0,
            "alpha_decay": 1.0,
            "epsilon_decay": 0.99,
            "alpha_min": 0.001,
            "epsilon_min": 0.1,
            "n_iter": int(1e6),
            "skip_check": False,
        },
    },
    "Value Iteration": {
        "Frozen Lake": {
            "gamma": 0.90,
            "epsilon": 0.001,
            "max_iter": int(1e5),
            "skip_check": False,
            "run_stat_frequency": 1,
        },
        "Forest Management": {
            "gamma": 0.90,
            "epsilon": 0.001,
            "max_iter": int(1e5),
            "skip_check": False,
            "run_stat_frequency": 1,
        },
    },
    "Policy Iteration": {
        "Frozen Lake": {
            "gamma": 0.90,
            "max_iter": int(1e5),
            "skip_check": False,
            "run_stat_frequency": 1,
        },
        "Forest Management": {
            "gamma": 0.90,
            "max_iter": int(1e5),
            "skip_check": False,
            "run_stat_frequency": 1,
        },
    },
}

PARAMS_GRID = {
    "Q-Learning": {
        "alpha": [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0],
        "epsilon": [0.75, 0.85, 0.95, 0.99, 0.999, 0.9999, 1.0],
        "alpha_decay": [1.0, 0.9999, 0.999, 0.99, 0.9],
        "epsilon_decay": [1.0, 0.9999, 0.999, 0.99, 0.9],
    },
    "Value Iteration": {
        "gamma": [0.1, 0.25, 0.5, 0.75, 0.85, 0.9, 0.95, 0.99, 0.999],
    },
    "Policy Iteration": {
        "gamma": [0.1, 0.25, 0.5, 0.75, 0.85, 0.9, 0.95, 0.99, 0.999],
    },
}