class PID:
    def __init__(self):
        self.kp = 3
        self.ki = 1
        self.kd = 0.1
        self.erro = 30
        self.pid = 0
        self.erro_somado = 0
        self.erro_derivado = 0

    def return_pid(self):
        pid = self.kp*self.erro + self.ki*self.erro_somado + self.kd*self.erro_derivado
        self.erro_somado = self.erro + self.erro_somado
        self.erro_derivado = self.erro - self.erro_derivado
        print("PID:", pid)
        return pid
    
PID_instance = PID()
PID_instance.return_pid()