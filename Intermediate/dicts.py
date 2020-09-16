mydict={
    "name":"John",
    "age":16,
    "address":"Ha Noi"
}

mydict2=dict(mydict)
mydict["email"] = "abc@gmail.com"

print(mydict2)
print(mydict)

## del mydict["Name"]

## mydict.popitem()
print(mydict)

if 'name' in mydict:
    print(mydict["name"])


try:
    print(mydict["lastname"])
except:
    print("Error")


for key,value in mydict.items():
    print(key,value)


""" item =mydict.items()
print(item) """

mydict3=dict(name="Harry",age="28")

mydict.update(mydict3)
print(mydict)

