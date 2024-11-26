from aux import change_tuple , pop_and_add_set, change_value_dict

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
ft_tuple = change_tuple(ft_tuple,0, "Spain")
#your code here
ft_list[1] = "world"
ft_set= pop_and_add_set(ft_set,"Urduliz")
change_value_dict(ft_dict, "Hello", "42Urduliz")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

