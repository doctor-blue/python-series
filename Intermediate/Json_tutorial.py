import json
from json import JSONEncoder
''' person = {"name": "John", "age": 20, "city": "Ha Noi"}

personJson = json.dumps(person,indent=4,sort_keys=True)
print(personJson)


with open('person.json','w') as file:
    json.dump(person,file,indent=4)

with open('example.js','r') as file:
    print(json.load(file))
person =json.loads(personJson)
print(person) '''


class User:
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age


user = User('Max', 27)


def encode(ob):
    if isinstance(ob, User):
        return{'name': ob.name, 'age': ob.age, ob.__class__.__name__: True}
    else:
        return TypeError("Object is not type of User")


userJson = json.dumps(user, default=encode)

print(userJson)


class UserEncoder(JSONEncoder):
    def default(self, ob):
        if isinstance(ob, User):
            return{'name': ob.name, 'age': ob.age, ob.__class__.__name__: True}
        return JSONEncoder.default(self, ob)

userJson = UserEncoder().encode(user)
print(userJson)

user= json.loads(userJson)
print(type(user)) 


def decode_user(dict):
    if User.__name__ in dict:
        return User(dict['name'], dict['age'])
    return dict


user = json.loads(userJson, object_hook= decode_user)
print(type(user))
print(user.name)
