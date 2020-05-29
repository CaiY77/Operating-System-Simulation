# Cai Yang
# Operation System Simulation

class Computer:
    def __init__(self, _ram, _hdd):
        self.hdd = [[]*1 for _ in range(_hdd)]
        self._ram = _ram
        self.memory = [['null', -1, -1], ['null', _ram, _ram]]
        self.memory_usage = 0
        self.cpu = []

    def add_to_memory(self, process):
        for x in range(len(self.memory)-1):
            if self.memory[x+1][1] - self.memory[x][2] - 1 >= process.size:
                self.memory.insert(
                    x+1, [process.pid, self.memory[x][2]+1, self.memory[x][2] + process.size])
                return bool(1)
        print("Error, not enough memory")
        return bool(0)

    def add_process(self, process):
        if self.add_to_memory(process):
            if process.type == 'Common':
                self.cpu.append([process.pid, process.type, process.status])
                if len(self.cpu) == 1:
                    self.cpu[0][2] = 'Running'

            elif process.type == 'Real-Time':
                if not self.cpu:
                    self.cpu.insert(
                        0, [process.pid, process.type, process.status])
                    self.cpu[0][2] = 'Running'
                    return
                for x in range(len(self.cpu)):
                    if self.cpu[x][1] == 'Common':
                        self.cpu.insert(
                            x, [process.pid, process.type, process.status])
                        self.cpu[0][2] = 'Running'
                        self.cpu[1][2] = 'Waiting'
                        return
                    elif self.cpu[x][1] == 'Real-Time' and x == len(self.cpu) - 1:
                        self.cpu.append(
                            [process.pid, process.type, process.status])

    def terminate(self):
        pid = self.cpu.pop(0)
        if self.cpu:
            self.cpu[0][2] = 'Running'
        for x in range(len(self.memory)-2):
            if self.memory[x+1][0] == pid[0]:
                self.memory.pop(x+1)
                return

    def end_time_slice(self):
        running_proccess = self.cpu.pop(0)
        running_proccess[2] = 'Waiting'
        if running_proccess[1] == 'Real-Time':
            for x in range(len(self.cpu)):
                if self.cpu[x][1] == 'Common':
                    self.cpu.insert(x, running_proccess)
                    return
            self.cpu.append(running_proccess)
            self.cpu[0][2] = 'Running'
            return
        else:
            self.cpu.append(running_proccess)
            self.cpu[0][2] = 'Running'
            return

    def hdd_request(self, hdd_number):
        if self.cpu:
            process = self.cpu.pop(0)
            if self.cpu:
                self.cpu[0][2] = 'Running'
            if self.hdd[hdd_number]:
                self.hdd[hdd_number].append(
                    [process[0], hdd_number, 'Waiting', process[1]])
            else:
                self.hdd[hdd_number].append(
                    [process[0], hdd_number, 'Running', process[1]])
        else:
            print('You currently have no process')

    def hdd_finish(self, hdd_number):
        if self.hdd[hdd_number]:
            process = self.hdd[hdd_number].pop(0)
            if self.hdd[hdd_number]:
                self.hdd[hdd_number][0][2] = "Running"
            if self.cpu:
                if process[3] == 'Real-Time':
                    self.cpu[0][2] = 'Waiting'
                    self.cpu.insert(0, [process[0], process[3], 'Running'])
                else:
                    self.cpu.append([process[0], process[3], 'Waiting'])
            else:
                self.cpu.append([process[0], process[3], 'Running'])
        else:
            print('There are no process running on this disk')

    def show_hdd(self):
        print('|---PID---|---HDD---|----STATUS----|')
        for hdd in self.hdd:
            for each in hdd:
                print(
                    '|', each[0], ' '*(6-len(str(each[0]))),
                    '|', each[1], ' '*(6-len(str(each[1]))),
                    '|', each[2], ' '*(11-len(each[2])), '|')

    def show_cpu(self):
        print('|---PID---|----TYPE----|----STATUS----|')
        for each in self.cpu:
            print(
                '|', each[0], ' '*(6-len(str(each[0]))),
                '|', each[1], ' '*(9-len(each[1])),
                '|', each[2], ' '*(11-len(each[2])), '|')

    def show_memory(self):
        print('|---PID---|----START----|------END------|')
        for x in range(len(self.memory)-1):
            if x != 0:
                print(
                    '|', self.memory[x][0], ' ' *
                    (6-len(str(self.memory[x][0]))),
                    '|', self.memory[x][1], ' ' *
                    (10-len(str(self.memory[x][1]))),
                    '|', self.memory[x][2], ' '*(12-len(str(self.memory[x][2]))), '|')
