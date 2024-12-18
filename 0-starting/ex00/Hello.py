ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here
# we replace the value at index 1
ft_list[1] = "World!"

# ft_tuple[1] = "France!" # <- not possible
# a tuple is immutable, we have to recreate one
ft_tuple = ("Hello", "France!")

# ft_set[1] = "France!"  # <- not possible
# a set is a dict "with no values".
# we can only remove or add keys, and they are therefore unique.
# the set is unordered, so we might get the output in reverse
# order sometimes.
ft_set.remove("tutu!")
ft_set.add("Paris!")
# now if we print ft_set we might get {"Paris!", "Hello"} sometimes

# we just change the value at key "Hello"
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
