#A List of Generatable EQ dicts for easy use.

eqlib = [
{"zeta" : 0.3, "sigma" : 0.9,"fn" :5,"T90" : 0.3,"eps" : 0.4,"tn" : 30},
{"zeta" : 0.15, "sigma" : 0.9,"fn" :5,"T90" : 0.3,"eps" : 0.4,"tn" : 80},
{"zeta" : 0.15, "sigma" : 0.9,"fn" :5,"T90" : 0.3,"eps" : 0.4,"tn" : 100}
]


#Generate data for the list(values inside may be changed manually, no method was used to select them)
for s in range(4):
    for e in range(8):
        for k in range(6):
            for j in range(1,4):
                for i in range(1,14):
                    eqlib.append(
                    {
                    "zeta" : 0.15+(0.05*j),
                    "sigma" : 0.6+(0.1*s),
                    "fn" :5+k,
                    "T90" : 0.3,
                    "eps" : 0.36+(0.01*e),
                    "tn" : 30+(5*i)
                    }
                    )
