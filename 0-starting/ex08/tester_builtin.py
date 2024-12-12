from time import sleep

from tqdm import tqdm


print("Original tqdm:")
print()
for elem in tqdm(range(10)):
    sleep(11)
print()
