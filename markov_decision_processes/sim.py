import numpy as np


class Simulator:
    def __init__(self, T, R, policy=None, map_=None):
        super().__init__()

        self.T = T
        self.R = R
        self.map_ = map_
        self.policy = policy

    def done(self, s, a, s_) -> bool:
        if self.map_ is not None:
            row, col = np.unravel_index(s_, (len(self.map_), len(self.map_[0])))

            return self.map_[row][col] in ("H", "G")
        else:
            return s_ == 0

    def simulate(self, steps):
        # Input check.
        assert self.policy is not None

        # Container setup.
        s = [0]
        a = []
        r = []
        t = []

        for step in np.arange(steps):
            # Select action.
            a.append(self.policy[s[step]])

            # Calculate transition.
            p = self.T[a[step]][s[step]]
            s.append(np.random.choice(np.arange(p.size), p=p))

            # Calculate reward.
            r.append(self.R[a[step]][s[step]][s[step + 1]] if self.R.ndim == 3 else self.R[s[step]][a[step]])
            t.append((s[step], a[step], r[step], s[step + 1]))

            # Check if end condition is met.
            if self.done(s[step], a[step], s[step + 1]):
                break

        return r[-1], np.sum(r), step, s[step + 1]
