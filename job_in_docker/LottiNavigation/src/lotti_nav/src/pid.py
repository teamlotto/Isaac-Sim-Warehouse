class PID:
    def __init__(self, kp, ki, kd, target_value):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target_value = target_value
        self.error = 0
        self.prev_error = 0
        self.p_err = 0
        self.i_err = 0
        self.d_err = 0

    def __call__(self, current_value):
        print("===================start===================")
        self.prev_error = self.error
        print(f"prev_err:{self.prev_error}")
        self.error = self.target_value - current_value
        print(f"err:{self.error}")

        self.p_err = self.error
        print(f"p_err:{self.p_err}")
        self.i_err += self.prev_error
        print(f"i_err:{self.i_err}")
        self.d_err = self.error - self.prev_error
        print(f"d_err:{self.d_err}")
        print("===================end=====================")
        return self.kp * self.p_err + self.ki * self.i_err + self.kd * self.d_err

if __name__ == "__main__":
    target = 1
    pid = PID(0.1, 0.3, 0.02, target)
    value = 0.0008
    while True:
        result = pid(value)
        if result == target:
            break
        else:
            print(f"result: {result}")
            value = result
        break

