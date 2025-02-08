person = {"fName":"Selmi",
          "Lname":"Nazeeb",
          "Friends":["abc","zxc"],
          "skills":{"backend_skills":["nodeJS","ruby"],"databases":["sql","mysql"]}}
person["address"]="kerala"
print(person)
print(len(person))
print(type(person))
print(person.get("skills"))
print(person.get("skills").get("backend_skills"))
print(person.get("address"))  
print("address" in person)  #check whether address is an attribute of dictonary// true
print(person.pop("address"))
print(len(person))
del person["Friends"]
print(len(person))
print(person["skills"]["databases"])    #instead 'get' we can use this to get the elements 
person["skills"]["databases"].append("mongoDb")
print(person["skills"]["databases"])
print(person.items())
person_copy=person.copy()   #create a copy of dictionary
del person
print(person_copy)
print(person_copy.keys()) #get the keys

    #print values of keys
keys=person_copy.keys()   
for i in keys:
    print(person_copy[i])
    print("\n")
keyss=(person_copy["skills"]).keys()
for i in keyss:
    print(person_copy["skills"][i])

