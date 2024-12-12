from time import sleep

from Loading import ft_tqdm


print("My ft_tqdm:")
print()
for elem in ft_tqdm(range(10)):
    sleep(11)
print()
