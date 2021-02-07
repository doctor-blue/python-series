my_dict = {
    "name":"John",
    "age":16,
    "address":"Ha Noi"
}

my_dict_2 = dict(full_name="John Smith",email="abc@efg.com")


# print(my_dict)
# print(my_dict_2)
# print(my_dict["name"])
# my_dict["Name"] = "Mew"
# print(my_dict)

# if "Name" in my_dict:
#     print(my_dict["name"])

# try:
#     print(my_dict["abcd"])
# except:
#     print("Error")

# del my_dict["name"]
# for key,value in my_dict.items():
#     print(key,value)

my_dict.update(my_dict_2)

print(my_dict)
print(my_dict_2)