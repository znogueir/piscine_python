from time import sleep

from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(10)):
    sleep(11)
print()

# for elem in tqdm(range(10)):
#     sleep(2)
print()
