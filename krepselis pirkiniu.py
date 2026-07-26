import time
print("Sveiki atvyke į maisto prekių parduotuvę. Išsirinkite produktus, kuriuos norite pirkti.")
print("pirkiniu sarasas: duona (1.50Eur), pienas(1.39Eur), vanduo(0.85Eur), desra(2.49Eur).")
atsakymas = input("pradeti apsipirkima? (taip arba ne): ")
while True: 
    if atsakymas.lower() == "ne":
        exit() 
    elif atsakymas.lower() == "taip":
        break
    else:
        print("neteisingas atsakymas, bandykite dar karta")
        atsakymas = input("pradeti apsipirkima? (taip arba ne): ")
duona = 1.50
pienas = 1.39
vanduo = 0.85
desra = 2.49
# Pirmas produktas
while True:
    pirmas_produktas = input("iveskite pirma produkta: ").lower()
    if pirmas_produktas == "duona":
        kiekis1 = int(input("iveskite kieki: "))
        kaina1 = kiekis1 * duona
        print(f"jusu pasirinktas produktas: {pirmas_produktas}, kaina: {kaina1}Eur, kiekis: {kiekis1}vnt")
        break
    elif pirmas_produktas == "pienas":
        kiekis1 = int(input("iveskite kieki: "))
        kaina1 = kiekis1 * pienas
        print(f"jusu pasirinktas produktas: {pirmas_produktas}, kaina: {kaina1}Eur, kiekis: {kiekis1}vnt")
        break
    elif pirmas_produktas == "vanduo":
        kiekis1 = int(input("iveskite kieki: "))
        kaina1 = kiekis1 * vanduo
        print(f"jusu pasirinktas produktas: {pirmas_produktas}, kaina: {kaina1}Eur, kiekis: {kiekis1}vnt")
        break
    elif pirmas_produktas == "desra":
        kiekis1 = int(input("iveskite kieki: "))
        kaina1 = kiekis1 * desra
        print(f"jusu pasirinktas produktas: {pirmas_produktas}, kaina: {kaina1}Eur, kiekis: {kiekis1}vnt")
        break
    else:
        print("tokio produkto nera")

ar_daugiau = input("Ar norite pirkti dar? (taip/ne): ").lower()
if ar_daugiau == "ne":
    print("\nJūsu krepselis:")
    print(f"{pirmas_produktas}: {kaina1}Eur, {kiekis1}vnt.")
    galutine_kaina = kaina1
    print(f"Galutine kaina: {galutine_kaina:.2f}Eur")
    time.sleep(20)
    exit()

# Antrasis produktas
while True:
    antrasis_produktas = input("iveskite antra produkta: ").lower()
    if antrasis_produktas == "duona":
        kiekis2 = int(input("iveskite kieki: "))
        kaina2 = kiekis2 * duona
        print(f"jusu pasirinktas produktas: {antrasis_produktas}, kaina: {kaina2}Eur, kiekis: {kiekis2}vnt")
        break
    elif antrasis_produktas == "pienas":
        kiekis2 = int(input("iveskite kieki: "))
        kaina2 = kiekis2 * pienas
        print(f"jusu pasirinktas produktas: {antrasis_produktas}, kaina: {kaina2}Eur, kiekis: {kiekis2}vnt")
        break
    elif antrasis_produktas == "vanduo":
        kiekis2 = int(input("iveskite kieki: "))
        kaina2 = kiekis2 * vanduo
        print(f"jusu pasirinktas produktas: {antrasis_produktas}, kaina: {kaina2}Eur, kiekis: {kiekis2}vnt")
        break
    elif antrasis_produktas == "desra":
        kiekis2 = int(input("iveskite kieki: "))
        kaina2 = kiekis2 * desra
        print(f"jusu pasirinktas produktas: {antrasis_produktas}, kaina: {kaina2}Eur, kiekis: {kiekis2}vnt")
        break
    else:
        print("tokio produkto nera")

ar_daugiau = input("Ar norite pirkti dar? (taip/ne): ").lower()
if ar_daugiau == "ne":
    print("\nJūsu krepselis:")
    print(f"{pirmas_produktas}: {kaina1}Eur, {kiekis1}vnt.")
    print(f"{antrasis_produktas}: {kaina2}Eur, {kiekis2}vnt.")
    galutine_kaina = kaina1 + kaina2
    print(f"Galutine kaina: {galutine_kaina:.2f}Eur")
    time.sleep(20)
    exit()

# Treciasis produktas
while True:
    treciasis_produktas = input("iveskite trecia produkta: ").lower()
    if treciasis_produktas == "duona":
        kiekis3 = int(input("iveskite kieki: "))
        kaina3 = kiekis3 * duona
        print(f"jusu pasirinktas produktas: {treciasis_produktas}, kaina: {kaina3}Eur, kiekis: {kiekis3}vnt")
        break
    elif treciasis_produktas == "pienas":
        kiekis3 = int(input("iveskite kieki: "))
        kaina3 = kiekis3 * pienas
        print(f"jusu pasirinktas produktas: {treciasis_produktas}, kaina: {kaina3}Eur, kiekis: {kiekis3}vnt")
        break
    elif treciasis_produktas == "vanduo":
        kiekis3 = int(input("iveskite kieki: "))
        kaina3 = kiekis3 * vanduo
        print(f"jusu pasirinktas produktas: {treciasis_produktas}, kaina: {kaina3}Eur, kiekis: {kiekis3}vnt")
        break
    elif treciasis_produktas == "desra":
        kiekis3 = int(input("iveskite kieki: "))
        kaina3 = kiekis3 * desra
        print(f"jusu pasirinktas produktas: {treciasis_produktas}, kaina: {kaina3}Eur, kiekis: {kiekis3}vnt")
        break
    else:
        print("tokio produkto nera")

ar_daugiau = input("Ar norite pirkti dar? (taip/ne): ").lower()
if ar_daugiau == "ne":
    print("\nJūsu krepselis:")
    print(f"{pirmas_produktas}: {kaina1}Eur, {kiekis1}vnt.")
    print(f"{antrasis_produktas}: {kaina2}Eur, {kiekis2}vnt.")
    print(f"{treciasis_produktas}: {kaina3}Eur, {kiekis3}vnt.")
    galutine_kaina = kaina1 + kaina2 + kaina3
    print(f"Galutine kaina: {galutine_kaina:.2f}Eur")
    time.sleep(20)
    exit()

# Ketvirtasis produktas
while True:
    ketvirtasis_produktas = input("iveskite ketvirta produkta: ").lower()
    if ketvirtasis_produktas == "duona":
        kiekis4 = int(input("iveskite kieki: "))
        kaina4 = kiekis4 * duona
        print(f"jusu pasirinktas produktas: {ketvirtasis_produktas}, kaina: {kaina4}Eur, kiekis: {kiekis4}vnt")
        break
    elif ketvirtasis_produktas == "pienas":
        kiekis4 = int(input("iveskite kieki: "))
        kaina4 = kiekis4 * pienas
        print(f"jusu pasirinktas produktas: {ketvirtasis_produktas}, kaina: {kaina4}Eur, kiekis: {kiekis4}vnt")
        break
    elif ketvirtasis_produktas == "vanduo":
        kiekis4 = int(input("iveskite kieki: "))
        kaina4 = kiekis4 * vanduo
        print(f"jusu pasirinktas produktas: {ketvirtasis_produktas}, kaina: {kaina4}Eur, kiekis: {kiekis4}vnt")
        break
    elif ketvirtasis_produktas == "desra":
        kiekis4 = int(input("iveskite kieki: "))
        kaina4 = kiekis4 * desra
        print(f"jusu pasirinktas produktas: {ketvirtasis_produktas}, kaina: {kaina4}Eur, kiekis: {kiekis4}vnt")
        break
    else:
        print("tokio produkto nera")
print("\nJūsu krepselis:")
print(f"{pirmas_produktas}: {kaina1}Eur, {kiekis1}vnt.")
print(f"{antrasis_produktas}: {kaina2}Eur, {kiekis2}vnt.")
print(f"{treciasis_produktas}: {kaina3}Eur, {kiekis3}vnt.")
print(f"{ketvirtasis_produktas}: {kaina4}Eur, {kiekis4}vnt.")
galutine_kaina = kaina1 + kaina2 + kaina3 + kaina4
print(f"Galutine kaina: {galutine_kaina:.2f}Eur")

time.sleep(20) 
# issiaiskinti kaip veikia lower
# try and except 
# while loop 