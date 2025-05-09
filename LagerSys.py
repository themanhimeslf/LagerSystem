import json, os, time

lagersystem = {'vareliste':[]}

# Sjekker om output.json eksisterer og laster det inn hvis ikke, skipper den og lager nye senere
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
        menyvalg = input("\nVelg handling: ")
        
        utfoerMenyValg(menyvalg)

def printMenyDumb():
        print("\n=== LAGERMENYEN DOMME JæVEL===")
        print("1. Registrere ny vare")
        print("2. rediger varer")
        print("3. Slette vare")
        print("4. vis lager")
        print("5. Vise rapport")
        print("6. Avslutt")
        print("=====================")
        menyvalg = input("\nVelg handling HUSK VELG FRA FUCKINGS TABELLEN OVER: ")
        
        utfoerMenyValg(menyvalg)

def utfoerMenyValg(valg):
    if valg == "1": 
        registrer_vare() # Registrer vare er valg nummer 1 / hvis bruker trykker 1 får de registrere vare
    elif valg == "2":
        rediger_vare() # redigerer vare altså antall, navn etc 
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
        printMenyDumb()


def registrer_vare():
    varenummer = input("Skriv inn Varenummer: ")
    navn = input("Skriv inn navn: ")
    kategori = input("Skriv inn kategori: ")
    
    pris = float(input("skriv in pris: "))
    
    antall = float(input("skriv in antall: "))
    
    nyRegistrering ={'varenummer':varenummer, 'navn':navn, 'kategori':kategori, 'pris':pris, 'antall':antall}
    lagersystem["vareliste"].append(nyRegistrering)

    with open('output.json', 'w') as f: # her enten lager den eller ikke
        json.dump(lagersystem, f)

    print(f"{0} {1} er registrert ved kategori {2}"
        .format(varenummer, navn, kategori, pris, antall))
    input("trykk 1 for å gå tilbake til menyen: ")
    printMeny()
    
    
    
#redigere vare
def rediger_vare():
    print("---REDIGERING av varer---")
    print("*1. Tilbake til meny,")
    print("*2. Rediger antall.")
    print("*2. Rediger varenummer.")
    print("*2. Rediger Pris.")
    RedigerMENY = input("\nVelg handling: ")
    
    if RedigerMENY == "1":
        printMeny()
    if RedigerMENY == "2":
        AntallMeny()

def AntallMeny():
    søk = input("Spor hvilken vare du vil endre via Navn: ")
    time.sleep(2)
    funnet = False
    for vare in lagersystem["vareliste"]:
        if søk.lower() == vare["navn"].lower(): # "søk.lower() vare etc .lower()" ANY word that has same in it, "[navn]søk.lower() == søk.lower():" SPECIFIC SAMME FYF
            #Print total antall funnet ved navn
            print("{varenummer}  {navn} {antall}".format(**vare)) # viser bare varenummer, navn og antall ikke pris, osv
            funnet = True # prints details, matches it, marks
            nytt_antall = input("Velg nytt antall: ")
            for vare in lagersystem["vareliste"]:
                if vare["navn"].lower() == søk.lower():
                    vare["antall"] = nytt_antall
            with open("output.json", "w") as f:
                json.dump(lagersystem, f)
                print(f"Endrett nytt antall er {nytt_antall} til {søk}")
    if not funnet:
        print("Ingen varer funnet med navn: ", søk)
    time.sleep(2)
    spor = input("trykk 1, for meny, 2 for spore annen vare: ")
    if spor == "1":
        printMeny()
    if spor == "2":
        AntallMeny()
        
    pass
def VarenummerMeny():
    pass

def PrisMeny():
    
    pass

#slett vare    
def slett_vare():
    print("**SLETTING AV VARER**")
    print("*1. Tilbake til meny,")
    print("*2. Slett Vare.")
    slettINT = input("\nVelg handling: ")
    
    if slettINT == "1":
        printMeny()
    if slettINT == "2":
        slettVareMeny()
        
        
def slettVareMeny(): 
    print("\n**SLETTING AV VARER**")
    print("*1. Tilbake til meny,")
    print("*2. Skriv inn navn til vare for sletting.")
    slett = input("\nHandling: ")
    
    if slett == "1":
        printMeny()
    else:
        found = False
        for vare in lagersystem["vareliste"]:
            if slett.lower() == vare["navn"].lower():
                lagersystem["vareliste"].remove(vare)
                print(f"\n***{slett} er slettet***")
                found = True
                with open('output.json', 'w') as f: # her enten lager den eller ikke
                    json.dump(lagersystem, f)
        time.sleep(2)
        if found == False:
            print(f"\nFant ingen vare med navn '{slett}'.")    
        slettVareMeny()
            



#lager
def vis_lager(): # Lager def -----------------------
    output = "" #noe for noe
    for item in lagersystem["vareliste"]:
        output += f"Varenummer: {item['varenummer']}, Navn: {item['navn']}, Kategori: {item['kategori']}, Pris: {item['pris']}, Antall: {item['antall']}\n"

    total = len(lagersystem["vareliste"]) # viser totalt hvor mye varer vi har i totalt
    print("antall varer totalt:", total) #Printer hvor mange varer altså Antallet av hver vare, så hvis 2 varer, printer 2 varer
    
    print(output) #printer OUTPUT, altså hele lageret sortert.
    
    #Lagermeny, som hovedmeny, bare for lageret, kan spore varer
    lagermeny = input("trykk 1 for meny, 2 for sporing, 3 for lager status: ")
    
    if lagermeny == "1":
            printMeny()
    elif lagermeny == "2": 
            sporMeny()


def sporMeny(): #Sporingsmenyen
    print("\n=== SPORING ===")
    print("Velkommen til sporing, " )
    print("1 for sporing via nummer, " )
    print("2. Sporing via navn, " )
    print("3. Gå tilbake til meny," )
    print("======================")
    spor = input("\nVelg handling: " )
    
    # if spor == "1":
    #     sporNRvare()
    if spor == "2":
        sporNvare()
    if spor == "3":
        printMeny()
        
            
def sporNvare():
    søk = input("Spor vare via Navn skriv inn: ") #spør bruker hva de vill søke og sporer via navn
    time.sleep(2)
    funnet = False # holder styr hvis noe ble funnet
    for vare in lagersystem["vareliste"]:
        if søk.lower() in vare["navn"].lower(): # "søk.lower() vare etc .lower()" ANY word that has same in it, "[navn]søk.lower() == søk.lower():" SPECIFIC SAMME FYF
            #Print total antall funnet ved navn
            print("{varenummer}  {navn}  {kategori}  {pris}  {antall}".format(**vare))
            funnet = True # prints details, matches it, marks
    if not funnet:
        print("Ingen varer funnet med navn: ", søk)
    spor = input("trykk 1, for meny, 2 for spore annen vare: ")
    if spor == "1":
        printMeny()
    if spor == "2":
        sporMeny
        
def sporNRvare(): # sporer varer via nummer og ikke navn
    pass


# Lager status
    

        
printMeny()


    