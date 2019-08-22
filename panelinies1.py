names = {}
passed = 0
mo_time = 0
time = 0

for i in range(35):
    name = str(input("Δωσε το ονομα του οδηγου : "))
    for i in range(4):
        laptime = 0
        laptime = int(input("Δωσε το χρονο του γύρου : "))
        if laptime>180:
            time = "ΜΗ ΣΥΜΕΤΟΧΗ"
            continue
        elif laptime<=180:
            time = laptime
            mo_time = mo_time + time
            passed = passed + 1
            break 
    names[name] = time   

key_min = min(zip(names.keys(),names.values()))
print("Περασαν :",passed)
print("Η λιστα :",list(names))
print("Μεσος Ορος: ",mo_time/passed)
print('Minimum Value: ',key_min)
input()
