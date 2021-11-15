from tabulate import tabulate
from PrimeNumbers2 import *
import time

mydata = []
start_time_global = time.time()
for k in range(1, 8):
    n = 10 ** k
    start_time = time.time()
    a = n_of_prime_numbers(n)
    runtime = time.time() - start_time
    mydata.append([n, a, runtime])

runtime_global = time.time() - start_time_global
mydata.append(["Total time","",runtime_global])

head = ["n", "n of prime numbers", "time in sec"]
print(tabulate(mydata, headers=head, tablefmt="fancy_grid"))
