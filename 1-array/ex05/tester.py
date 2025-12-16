import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


array = ft_load("landscape.jpg")
if array is None:
    print("Error: Encountered issue while loading.")
    exit(1)

print("# ==== Docstrings: ==== #")
print("ft_invert", ft_invert.__doc__)
print("ft_red", ft_red.__doc__)
print("ft_green", ft_green.__doc__)
print("ft_blue", ft_blue.__doc__)
print("ft_grey", ft_grey.__doc__)

print("# ==== Showing imgs ==== #")
print("(Click on the cross to see next img)")
img = ft_invert(array)
plt.imshow(img)
plt.show()

img = ft_red(array)
plt.imshow(img)
plt.show()

img = ft_green(array)
plt.imshow(img)
plt.show()

img = ft_blue(array)
plt.imshow(img)
plt.show()

img = ft_grey(array)
plt.imshow(img)
plt.show()
