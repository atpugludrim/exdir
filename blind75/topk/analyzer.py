import numpy as np
from subprocess import Popen, PIPE
heap_times = []
part_times = []
for k in range(33):
    randseed = np.random.randint(1,1000)
    process = Popen(f'python3 heap.py {randseed}'.split(), stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    heap_time = float(stdout.decode('utf-8').split()[-1].strip())
    heap_times.append(heap_time)

    process = Popen(f'python3 quicksort.py {randseed}'.split(), stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    part_time = float(stdout.decode('utf-8').split()[-1].strip())
    part_times.append(part_time)

print("with heap:","{}s".format(np.mean(heap_times)),"with partition:","{}s".format(np.mean(part_times)))
