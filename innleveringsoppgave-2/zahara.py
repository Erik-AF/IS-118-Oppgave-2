# interaktiv_historie.py
# Introduksjon
print("Velkommen til prosjektlederspillet!")
print("Du er Erling, prosjektleder for utviklingen av kommunens nye medborgerportal.")
print("Teamet ditt står midt i storming-fasen, og du må ta tre viktige valg for å sikre fremdrift og trivsel.\n")

# Beslutningspunkt 1: Konflikten mellom Silje og Sivert
print("Beslutningspunkt 1: Hvordan håndterer du konflikten mellom Silje og Sivert?")
print("A: Du tar det opp i plenum.")
print("B: Du tar personlige samtaler.")
valg1 = input("Velg A eller B: ").strip().upper()
if valg1 == "A":
    print("Skaper åpenhet, men kan eskalere konflikten offentlig")
if valg1 == "B":
    print("Demper temperaturen, men risiko for manglende felles forståelse")
# Beslutningspunkt 2: Uenigheten mellom Hamdi og Jabir
print("\nBeslutningspunkt 2: Hvordan håndterer du uenigheten mellom Hamdi og Jabir?")
print("A: Du setter opp et strukturert møte med klare rammer.")
print("B: Du lar dem prøve ut egne løsninger og håper på enighet.")
valg2 = input("Velg A eller B: ").strip().upper()
if valg1 == "A":
    print("Fremmer dialog og felles løsning, styrker tillit.")
if valg1 == "B":
    print("Kan gi kreativ frihet, men risiko for splittelse og forsinkelser.")
# Beslutningspunkt 3: Hvordan bevarer du motivasjonen i teamet?
print("\nBeslutningspunkt 3: Hvordan bevarer du motivasjonen i teamet?")
print("A: Du organiserer sosiale tiltak og feirer milepæler.")
print("B: Du otganiserer et feiring av milepæl.")
valg3 = input("Velg A eller B: ").strip().upper()
if valg1 == "A":
    print("erling samler teamet for god stemning og dialog om problemene, men dette blir et miljø for videre polarisering, der problemene smittes over på de andre og teamet splittes ved at de tar sider.  ")
if valg1 == "B":
    print("Øker trivsel og samhold, gir ny energi og motivasjon for å nå fremtidige mål")
# Sluttresultat basert på valg
print("\n--- UTFALL ---")
if valg1 == "A" and valg2 == "A" and valg3 == "B":
    print("Teamet gjenoppretter tillit og går videre til norming-fasen. Samarbeidet styrkes og prosjektet får ny energi.")
elif valg1 == "B" and valg2 == "B" and valg3 == "A":
    print("Prosjektet mister samhold og forsinkes. Konfliktene får vokse og teamet splittes.")
else:
    print("Konfliktene løses delvis, men relasjonene er fortsatt sårbare. Prosjektet leverer, men med redusert trivsel og tillit.")

print("\nTakk for at du spilte prosjektlederspillet!")