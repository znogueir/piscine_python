from time import sleep

from tqdm import tqdm
from Loading import ft_tqdm
from Loading import format_time

print(format_time(3599))
print(format_time(3600))
print(format_time(2451))
print(format_time(3601))
print(format_time(917823571))

range_size = 10
nap_time = 11

print("My ft_tqdm:")
print()
for elem in ft_tqdm(range(range_size)):
    sleep(nap_time)
print()

print("Original tqdm:")
print()
for elem in tqdm(range(range_size)):
    sleep(nap_time)
print()
