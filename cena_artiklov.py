cena_artikla = 1
vsota = 0

while cena_artikla != 0:
    cena_artikla = int(input("Vnesite ceno artikla: "))
    vsota += cena_artikla
print("Vsota: " , vsota)