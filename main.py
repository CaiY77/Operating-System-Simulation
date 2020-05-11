# Cai Yang
# Operation System Simulation
# CSCI 340

from process import Process
from computer import Computer

def print_invalid():
    print('Invalid Command. Please try again.')

ram = int(input('How much RAM memory is there on the simulated computer? '))
hdd = int(input('How many hard disks does the simulated computer have? '))

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
        print('')

    elif ans[0] == 'D':
        print('')

    elif ans[0] == 'S':
        if ans[1] == 'r':
            computer.show_cpu()
        if ans[1] == 'i':
            computer.show_hdd()
        if ans[1] == 'm':
            computer.show_memory()

    elif ans[0] == 'exit':
        _loop = 0
        print('Program Terminated')

    else:
        print_invalid()
