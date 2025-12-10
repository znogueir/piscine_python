from time import sleep

from tqdm import tqdm
from Loading import ft_tqdm

range_size = 333
nap_time = 0.005

print("My ft_tqdm:")
for elem in ft_tqdm(range(range_size)):
    sleep(nap_time)
print()
print()

print("Original tqdm:")
for elem in tqdm(range(range_size)):
    sleep(nap_time)
print()
print()
