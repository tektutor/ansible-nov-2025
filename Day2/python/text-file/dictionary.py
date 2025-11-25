#!/usr/bin/python3

contacts = {}
#contacts = dict()

contacts["Sriram"] = 1234537894
contacts["Nitesh"] = 9432344334

#Retrieve a value given the name(key)
name = "Sriram"
if contacts.get(name) is not None:
    print("Mobile number of ", name, " is ", contacts[name])
