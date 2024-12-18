from time import sleep

from tqdm import tqdm


print("Original tqdm:")
print()
for elem in tqdm(range(394)):
    sleep(0.23)
print()
