people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# Equal of lambda
def byName(person):
    return person["name"]

def byHouse(person):
    return person["house"]

# Lambda = Short one line function
people.sort(key = lambda person: person["name"])
print(people)

people.sort(key = lambda person: person["house"])
print(people)