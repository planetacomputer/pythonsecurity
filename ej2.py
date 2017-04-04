#!/usr/bin/python
europe = []
germany = {"name": "Germany", "population": 81000000, "price": 1000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000, "price": 2000}
europe.append(luxembourg)
andorra = {"name": "Andorra", "population": 900000, "price": 3000}
europe.append(andorra)

print(len(europe))


europe2 = europe[:]
for item in europe2:
    print(item["name"])
    if item["population"] < 1000000 and item["name"].find("A", 0, 1)==0:
        print(str(item["population"]) + " - " + item["name"])
    else:
        europe.remove(item)

print ("Ahora europe tiene %s y %d naciones" % (len(europe), 12) )
for item in europe:
    print(item["name"])