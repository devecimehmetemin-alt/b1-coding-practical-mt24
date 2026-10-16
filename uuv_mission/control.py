class PDController:
    """Discrete-time proportional-derivative (PD) depth controller.

    u[t] = kp * e[t] + kd * (e[t] - e[t-1]), where e[t] = r[t] - y[t] and e[-1] = 0.
    """

    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0

    def reset(self):
        # Reset the last error so the next step starts from e[-1] = 0
        self.prev_error = 0.0

    def compute(self, reference: float, observation: float) -> float:
        error = reference - observation
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action
