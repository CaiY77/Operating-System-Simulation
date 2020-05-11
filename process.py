# Cai Yang
# Operation System Simulation

class Process:
    def __init__(self,size,pid,type):
        self.size = size
        self.pid = pid
        self.type = type
        self.status = 'Waiting'
