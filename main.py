# Cai Yang
# Operation System Simulation

from process import Process
from computer import Computer

def print_invalid():
    print('Invalid input. Please try again.')

while True:
    try:
        ram = int(input('How much RAM memory is there on the simulated computer? '))
    except ValueError:
        print_invalid()
        continue
    else:
        break
while True:
    try:
        hdd = int(input('How many hard disks does the simulated computer have? '))
    except ValueError:
        print_invalid()
        continue
    else:
        break

computer = Computer(ram,hdd)
_loop = 1
_pid = 0

while _loop == 1 :
    reply = input('')
    ans = reply.split()

    if ans[0] == "A":
        if ans[1].isdigit and len(ans) == 2:
            _pid += 1
            process = Process(int(ans[1]),_pid,'Common')
            computer.add_process(process)
        else:
            print_invalid()

    elif ans[0] == 'AR' and len(ans) == 2:
        if ans[1].isdigit:
            _pid += 1
            process = Process(int(ans[1]),_pid,'Real-Time')
            computer.add_process(process)
        else:
            print_invalid()

    elif ans[0] == 'Q' and len(ans) == 1:
        computer.end_time_slice()

    elif ans[0] == 't' and len(ans) == 1:
        computer.terminate()

    elif ans[0] == 'd':
        if ans[1].isdigit and int(ans[1]) <= hdd-1:
            computer.hdd_request(int(ans[1]))
        else:
            print('Disk does not exist')

    elif ans[0] == 'D':
        if ans[1].isdigit and int(ans[1]) <= hdd-1:
            computer.hdd_finish(int(ans[1]))
        else:
            print('Disk does not exist')

    elif ans[0] == 'S':
        if ans[1] == 'r':
            computer.show_cpu()
        elif ans[1] == 'i':
            computer.show_hdd()
        elif ans[1] == 'm':
            computer.show_memory()
        else:
            print_invalid()

    elif ans[0] == 'exit':
        _loop = 0
        print('Program Terminated')

    else:
        print_invalid()
