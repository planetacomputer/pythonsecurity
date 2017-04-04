#!/usr/bin/python
import sys
import operator

europe = []
germany = {"name": "Germany", "population": 81000000, "price": 1000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000, "price": 2000}
europe.append(luxembourg)
andorra = {"name": "Andorra", "population": 900000, "price": 3000}
europe.append(andorra)

print(len(europe))

for item in europe:
    print(item["name"])
    item["price"] = item["price"] + item["price"] * 0.05

print ("Ahora europe tiene %s y %d naciones" % (len(europe), 12) )
europe.sort(key=operator.itemgetter('population'), reverse=True)
for item in europe:
    print ("Ahora el precio de %s es %d y la poblacion es  %d" % (item["name"], item["price"], item["population"]) )

print(sys.version)  