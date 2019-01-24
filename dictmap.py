def dictmap(d,f):
    for key in d.keys():
        d[key] = f(d[key])
