try:
    f = open("months.txt")
    print(f.read())
except IOError as e:
    print("Se ha producido el siguiente error: ")
    print "I/O error({0}): {1}".format(e.errno, e.strerror)