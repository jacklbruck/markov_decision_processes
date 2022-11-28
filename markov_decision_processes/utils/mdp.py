import numpy as np

from hiive.mdptoolbox.example import forest
from gym.envs.toy_text import frozen_lake


def make_frozen_lake(size=8, p=0.85):
    map_ = ["SFFFFHFF", "FHHFFFFF", "FHFFHFFH", "FHFFFHFF", "FFFHFFFF", "FHFHFFFF", "FFFFFFFF", "FFFFFFHG"]
    env = frozen_lake.FrozenLakeEnv(desc=map_)

    A = env.action_space.n
    S = env.observation_space.n

    T = np.zeros((A, S, S))
    R = np.zeros((A, S, S))

    for s in np.arange(S):
        for a in np.arange(A):
            for p, s_, r, _ in env.P[s][a]:
                T[a, s, s_] += p
                R[a, s, s_] = r

    return T, R, map_


def make_forest_management(S=2500, r1=5000, r2=2500, p=0.001):
    T, R = forest(S=S, r1=r1, r2=r2, p=p)

    return T, R, None
