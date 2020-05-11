# Cai Yang
# Operation System Simulation
# CSCI 340

class Process:
    def __init__(self,size,pid,type):
        self.size = size
        self.pid = pid
        self.type = type
        self.status = 'Waiting'
