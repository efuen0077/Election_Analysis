print("Hello World")
help("keywords")
(5+2)*3
num = (8//5) - 3
print(num)
nume_one = 8+(22*(2-4))
print(nume_one)
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties[0])
print (counties[-1])
print(len(counties))
print(counties[0:2])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
my_tuple = tuple()
counties_tuple = ("Arapahoe", "Denver", "Jeffereson")
len(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
{'Arapahoe': 422829}
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

people = ["leSlEy", "KEN", "sYDNey", "AnNa", "gRANT"]
# people = []
people.remove("leSlEy")
people.insert(0, "Lesley")
name = people[0]

for i in range (3):
    print("I would like to invite: " + name)

#def printInvite(name):
    #print("I would like invite: {name}")
voting_data = []
voting_data.append({"county" : "Arapahoe", "registered_voters" : 422829})
voting_data.append({"county" : "Denver", "registered_voters" : 463353})
voting_data.append({"county" : "Jefferson", "registered_voters" : 432438})
print(voting_data)
voting_data.insert(1, {"county" : "El Paso", "registered_voters" : 461149})
print(voting_data)
voting_data.remove({"county" : "Arapahoe", "registered_voters" : 422829})
voting_data.remove({"county" : "Denver", "registered_voters" : 463353})
voting_data.insert(2, {"county" : "Denver", "registered_voters" : 463353})
print(voting_data)
voting_data.append({"county" : "Arapahoe", "registered_voters" : 422829})
print(voting_data)