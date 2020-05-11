# Cai Yang
# Operation System Simulation
# CSCI 340

class Computer:
    def __init__(self,_ram,_hdd):
        self._hdd = _hdd
        self._ram = _ram
        self.hdd_state = []
        self.memory = [['null',-1,-1],['null',_ram,_ram]]
        self.memory_usage = 0
        self.cpu = []

    def add_to_memory(self,process):
        for x in range(len(self.memory)-1):
            if self.memory[x+1][1] - self.memory[x][2] - 1 >= process.size:
                self.memory.insert(x+1,[process.pid,self.memory[x][2]+1,self.memory[x][2] + process.size])
                return bool(1)
        print ("Error, not enough memory")
        return bool(0)

    def add_process(self,process):
        if self.add_to_memory(process):
            if process.type == 'Common':
                self.cpu.append([process.pid,process.type,process.status])
                if len(self.cpu) == 1:
                    self.cpu[0][2] = 'Running'

            elif process.type == 'Real-Time':
                self.cpu.insert(0,[process.pid,process.type,process.status])
                self.cpu[0][2] = 'Running'
                if len(self.cpu) > 1:
                    self.cpu[1][2] = 'Waiting'

    def terminate(self):
        pid = self.cpu.pop(0)
        self.cpu[0][2] = 'Running'
        for x in range(len(self.memory)-2):
            if self.memory[x+1][0] == pid[0]:
                self.memory.pop(x+1)
                return

    def end_time_slice(self):
        running_proccess = self.cpu.pop(0);
        self.cpu[0][2] = 'Running'
        running_proccess[2] = 'Waiting'
        self.cpu.append(running_proccess)

    def hdd_request(self,hdd_number):
        print('')

    def hdd_finish(self,hdd_number):
        print('')

    def show_hdd(self):
        print('|---PID---|---HDD---|----STATUS----|')
        for each in self.hdd_state:
            print(
            '|',each[0],' '*(6-len(str(each[0]))),
            '|',each[1],' '*(6-len(each[1])),
            '|',each[2],' '*(11-len(each[2])), '|')

    def show_cpu(self):
        print('|---PID---|----TYPE----|----STATUS----|')
        for each in self.cpu:
            print(
            '|',each[0],' '*(6-len(str(each[0]))),
            '|',each[1],' '*(9-len(each[1])),
            '|',each[2],' '*(11-len(each[2])), '|')

    def show_memory(self):
        print('|---PID---|----START----|----END----|')
        for x in range(len(self.memory)-1):
            if x != 0:
                print(
                '|',self.memory[x][0],' '*(6-len(str(self.memory[x][0]))),
                '|',self.memory[x][1],' '*(10-len(str(self.memory[x][1]))),
                '|',self.memory[x][2],' '*(8-len(str(self.memory[x][2]))),'|')
