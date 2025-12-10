from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

# added
print("####################")
all_thing_is_obj([])  # list
all_thing_is_obj(())  # tuple
all_thing_is_obj(set())  # set
all_thing_is_obj({})  # dict
all_thing_is_obj("a")  # str
all_thing_is_obj(125)  # not found == int
all_thing_is_obj((125, 3))  # tuple
all_thing_is_obj([125])  # list
all_thing_is_obj(set([123, 55]))  # set
all_thing_is_obj({125: [12, 2]})  # dict
all_thing_is_obj(float("-infinity"))  # not found
all_thing_is_obj(float("nan"))  # not found
