import json, os

lagersystem = {'vareliste':[]}


# Sjekker om output.json eksisterer og laster det inn
#
if os.path.exists("output.json"):
    with open("output.json") as file:
        lagersystem = json.load(file)


def printMeny():
        print("\n=== LAGERMENY ===")
        print("1. Registrere ny vare")
        print("2. rediger varer")
        print("3. Slette vare")
        print("4. vis lager")
        print("5. Vise rapport")
        print("6. Avslutt")
        print("=====================")
        menyvalg = input("Velg handling: ")
        utfoerMenyValg(menyvalg)

def utfoerMenyValg(valg):
    if valg == "1": 
        registrer_vare() # Registrer vare er valg nummer 1 / hvis bruker trykker 1 får de registrere vare
    elif valg == "2":
        rediger_vare()
    elif valg == "3":
        slett_vare()
    elif valg == "4":
        vis_lager()
    elif valg == "5":
        vis_rapport()
    elif valg == "6":
        exit()
    else:
        print("Ugyldig valg.")


def registrer_vare():
    varenummer = input("Skriv inn Varenummer: ")
    navn = input("Skriv inn navn: ")
    kategori = input("Skriv inn kategori: ")
    pris = input("skriv in pris:")
    antall = input("skriv in antall:")

    nyRegistrering ={'varenummer':varenummer, 'navn':navn, 'kategori':kategori, 'pris':pris, 'antall':antall}
    lagersystem["vareliste"].append(nyRegistrering)

    with open('output.json', 'w') as f:
        json.dump(lagersystem, f)

    print("{0} {1} er registrert ved kategori {2}"
        .format(varenummer, navn, kategori, pris, antall))
    input("trykk 1 for å gå tilbake til menyen: ")
    printMeny()
    # valg =="1":
    # printMeny()


# def rediger_vare():


def vis_lager():
    output = ""
    for item in lagersystem["vareliste"]:
        output += f"Varenummer: {item['varenummer']}, Navn: {item['navn']}, Kategori: {item['kategori']}, Pris: {item['pris']}, Antall: {item['antall']}\n"
        
        for item in lagersystem["vareliste"]:
            total += int(item["antall"])
        print("antall varer totalt", total)
    print(output)
    input("trykk 1 for å gå tilbake til menyen: ")
    printMeny()
# def slett_vare():

printMeny()


# def vis_rapport():