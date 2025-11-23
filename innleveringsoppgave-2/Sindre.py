import os 
os.system("cls")

#funksjon for a håndtere valg A eller B 

def AB():
#while løkke som fortsetter helt til brukeren benytter riktig svar
    while True:
        valg = input("Velg A eller B: ").upper()
        if valg == 'A' or valg == 'B':
            print(f"\nDu valgte: {valg}")
            return valg
        else:
            print("Ugyldig valg. Vær så snill å prøv igjen.")

       
print("Prosjektleder Erling har samlet sitt prosjektteam for første gang. Etter en inspirerende oppstart med høy energi,")
print("begynner sammarbeidet nå å møte sine første reelle prøver.")
print("\nDu skal ta på deg rollen som prosjektleder Erling og gjøre valg for å løse konflikter på best mulig måte.")
print("\nSijle og Sivert har en uenighet om teknologi og design. Uenigheten har utviklet seg fra en sakskonflikt til en personkonflikt.")

print("Hvordan vil du gå frem for å løse konflikten?")

print("\nValg A: Ta personelige samtaler med samtlige.")

print("Valg B: Ta det opp i plenum.")

valg1 = AB()
#Denne "if" gjør så brukeren får enda et alternativ i A
if valg1 == "A": 
    print("konsekvens: Møtet går dårlig, og forverrer relasjonene.")
    print("\nDet viser seg slik at spenningen mellom de to partene har nådd topplokket og møtet slår dårlig ann.")
    print("Konflikten har tilsynelatende pågått alt for lenge uten innblanding.")

    print("\nHvordan velger du å gå frem nå?")

    print("\nValg A: Du sender saken vidre til HR.")

    print("Valg B: Du tar saken i egne hender, og velger et endelig designvalg for dem.")

    valgA = AB()
    if valgA == "A":
        print("konsekvens: HR griper inn, men relasjonene forverres ytterligere.")

    if valgA == "B":
        print("konsekvens: Du tar et endelig designvalg, men relasjonene forverres ytterligere.")

if valg1 == "B":
    print("konsekvens: Konflikten løses! Bra jobbet!")
print("\n----------------------------------------------------------------------------")
print("\nHamdi og Jabir har en uenighet. Uenigheten har ikke uviklet seg til en personkonflikt,")
print("men du merker at det fort kan vokse og bli et problem for prosjektet.")

print("\nHvordan vil du nå gå frem for å løse konflikten?")

print("\nValg A: Du setter opp et møte med begge to for å diskutere uenigheten.")

print("Valg B: Du ser ann situasjonen litt lenger før du eventuelt griper inn.")

valg2 = AB()
if valg2 == "A": 
    print("konsekvens: Relasjonene styrkes og konflikten løses! Bra jobbet!")

if valg2 == "B":
    print("konsekvens: Det løser seg ikke, tid og ressurser går tapt.")

print("\n----------------------------------------------------------------------------")

print("\nFor å bevare teamets motivasjon som helhet må du velge hva som er mest effektivt for å løfte teamets motivasjon.")

print("\nHvordan vil du gå frem?")    

print("\nValg A: Du arrangerer en sosial sammenkomst for teamet.")
print("Dette innebærer kaffepauser eller felles lunsj for å senke terskelen, og skape dialog.")
print("Her kan teamet dele høydepunkter og utfordringer.")

print("\nValg B: små feiringer av milepæler. Dette gir positiv energi og synliggjør fremdrift og motiverer mot fremtidige mål.")

print("\nHvilket valg tar du?")

valg3 = AB()
if valg3 == "A": 
    print("konsekvens: Dette fører til bedre sammhold og kommunikasjon i teamet,")
    print("men dette fører også til å skape et miljø for videre polarisering i teamet,")
    print("der problemener smittes, det blir valgt sider og teamet splittes")

if valg3 == "B":
    print("konsekvens: Dette gir positiv energi og synliggjør fremdrift og motiverer mot fremtidige mål, bra jobbet!")

    print("\n----------------------------------------------------------------------------")

print("\nGratulerer! Du har fullført scenarioet som prosjektleder Erling. Her er ditt resultat:")
#resultater av øvelse basert på hvilke valg som er tatt
if valg1 == "B" and valg2 == "A" and valg3 == "B":
    print("\nUtmerket arbeid! Teamet gjenoppretter tillit og går videre til norming-fasen.")

elif valg1 == "A" and valg2 == "B" and valg3 == "A":
    print("\nProsjektet mister samhold og forsinkes...")

else: 
    print("\nKonflikten løses delvis, men relasjonene er fortsatt sårbare.")






