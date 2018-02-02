import sys
import random

MAX_NUM = 2*10**5

N = 2*10**5

sys.stdout.write('{}\n'.format(N))

for _ in range(N):
   sys.stdout.write('{} '.format(random.randint(0, MAX_NUM)))

