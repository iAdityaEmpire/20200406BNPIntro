#!/usr/bin/env python
import numpy as np

limit = 100
is_prime = np.ones(limit + 1)
print(is_prime)
for n in range(2,limit+1):
     if is_prime[n]:
         print(n)
         for m in range(2*n,limit+1,n):
             is_prime[m] = 0
