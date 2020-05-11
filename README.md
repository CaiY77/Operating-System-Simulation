# Operating System Simulation

- Python

This application simulates some aspects of the operating systems. It simulates contiguous memory management with “first-fit” approach.

To run this program, run the command: py main.py (or another methods to run python code.)

## Information to Provide:
### How much RAM memory is there on the simulated computer?
(do no include 'kilobytes' or words.)

### How many hard disks does the simulated computer have?
(The enumeration of the hard disks starts with 0.)

## Possible Inputs:
### A size
  ‘A’ input means that a new common process has been created. When the new process arrives, the program create its PCB and place the process in the ready-queue or the CPU. The requested amount of memory should be allocated for the new process. Process ID for the new process start from 1 and go up. Process ID are automatically generated and will not be reused. For example, the command A 1000 means that a new common process has been created and it requires 1000 bytes of memory.

### AR size
   'AR' input does the same as ‘A’ but the new process is an Real-Time process instead of a common process.

### Q
  'Q' input means that the time slice has ended for the currently running process.

### t
  't' input means that the currently running process is being terminated. It will be removed from the CPU and the memory allocated to it will open up.

### d number
   The process that currently uses the CPU requests a specific hard disk. For example the command d 3 means that current process is requesting to use hard disk #3.

### D number
   The hard disk #number has finished the work for one process. For example the command D 3 means that the process currently using hard disk #3 has finished.

### S r
  Shows what process is currently using the CPU and what processes are waiting on both levels of the ready-queue.

### S i
   Shows what processes are currently using the hard disks and what processes are waiting to use them. Each busy hard disk will show the process that uses it and show its I/O-queue. The enumeration of hard disks starts from 0.

### S m
  Shows the state of memory. Show the range of memory addresses used by each process in the system.
