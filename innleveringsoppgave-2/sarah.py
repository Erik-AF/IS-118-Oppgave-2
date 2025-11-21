# innleveringsoppgave-2  – interaktiv historie for rammefortellingen
# Sarah sin løsning
# Dette programmet bygger på storyline-strukturen med tre beslutningspunkter.
# Brukeren spiller som Erling, prosjektleder.




print("\nHei! og velkommen til min interaktive historie besvarelse☺️")
print("\nFør spillet begynner skal du få en innføring i hvem du er og hva du prøver å oppnå")
print("I denne historien jobber du for kommunens nye medborgerportal og spiller som prosjektlederen Erling.\n")
print("Ditt team finner seg midt i en storming-fase som bare du kan navigere.")
print("Dessverre, er det stadigg økende konflikter blant medarbeiderne Silje (UX-designer) og Sivert (IT-rådgiver) og Hamdi (Kulturavdelingen) og Jabir (Brukerrepresentant).") 
print("Alle valgene du tar bestemmer avslutningen du får. Lykke til.\n")

# --------------------
# Beslutningspunkt 1
# --------------------

print("BESLUTNING 1: Konflikten mellom Silje og Sivert har pågått en stund og blir stadig verre.")
print("Uenigheten dems i hvordan å løse prototypens designvalg har ført til at flere har blitt blandet inn.")
print("Hva som først var en sakskonflikt har nå blitt til en personkonflikt som påvirker arbeidet.")
print("Hva ønsker du å gjøre?")

print("A: Ta en personlig samtale..")
print("B: Ta det opp i felleskap.")

valg1 = input("Skriv A eller B: ").strip().upper()

if valg1 == "A":
    konsekvens1 = "Økt spenning"
    print("\nDu velger å ta individuelle samtaler. Konflikten kartlegges, men møtet slår seg vrang og relasjonenen ødelegges videre.")
    print("Dette resulterer i to valg til som fører til nye scenarios.")

    print("A1: Du velger å sende saken videre til HR.")
    print("A2: Du tar endelig beslutning.")

#----------Hvis B----------

else:
  konsekvens1 = "Minket spenning"
print("\nDu velger å ta opp konflikten foran hele teamet. Den åpne samtalen med gruppa virker positivt på Silje og Sivert.")  

#-----------Hvis A------------

valg1A = input("Skriv A1 eller A2: ").strip().upper()

if valg1A == "A1":
        konsekvens1 = "Ikke vellykket møte"
        print("\nDu sender saken til HR og håper det løser seg.")
elif valg1A == "A2":
        konsekvens1 = "Svekket relasjon"
        print("\nI å ta siste beslutning fikk Silje og Sivert aldri løst personkonflikten deres.")



# --------------------
# Beslutningspunkt 2
# --------------------

print("\nBESLUTNING 2: Hamdi og Jabir opplever småuenigheter om hvordan innbyggerdialogen i portalen skal utføres.")
print("Heldigvis har du fått ord om uenigheten tidlig og kan dermed ha en reell mulighet å gripe inn. Men er det behov?")
print("Hva ønsker du å gjøre?")

print("A: Gripe aktivt inn og sette opp et møte.")
print("B: La situasjonen løse seg selv.")

valg2 = input("Skriv A eller B: ").strip().upper()

if valg2 == "A":
    konsekvens2 = "Konflikten er løst"
    print("\nDu samler dem. De forstår hverandres perspektiver bedre.")
else:
    konsekvens2 = "Konflikten løses ikke"
    print("\nDu venter og ser. Uenigheten blir ikke bedre og fører til at tid og ressurser blir sløset.")

# --------------------
# Beslutningspunkt 3
# --------------------

print("\nBESLUTNING 3: Som leder merker du at teamets motivasjon er i ferd med å synke.")
print("De nyligste konfliktene har hatt en innvirkning på det generelle arbeidsmiljøet.")
print("Som leder er det ditt ansvar å finne en løsning på dette.")
print("Hva gjør du?")

print("A: Feiring av milepæle.")
print("B: Kaffe og lunsj pause.")

valg3 = input("Skriv A eller B: ").strip().upper()

if valg3 == "A":
    konsekvens3 = "Trygge og glade medarbeidere"
    print("\nTeamet setter pris på avbrekket og samarbeidet styrkes.")
else:
    konsekvens3 = "nøytrale medarbeidere"
    print("\nFint med mat men er ikke til stor hjelp for motivasjonen eller relasjonene.")

# --------------------
# Sluttresultater
# --------------------

print("\n--- SLUTTUTFALL ---")

if konsekvens1 == "dempet_konflikt" and konsekvens2 == "avklart" and konsekvens3 == "sosialt_fokus":
    print("UTFALL 1: Teamet returnerer til god samhold og kommer seg vellykket inn i norming-fasen.")
    print("Gratulerer! Relasjonene finner seg på god fot igjen og samarbeidsflyten gjenopprettes. Prosjektet opplever framdrift.")

elif konsekvens2 == "ikke_avklart" and konsekvens3 == "leveranse_fokus":
    print("UTFALL 2: Konflikten løses delvis, men de interpersonlige relasjonene blir negativt påvirket.")
    print("En større andel av teamet føler seg uhørte og dermed graves konflikten, men forsvinner ikke helt.")

else:
    print("UTFALL 3: Prosjektet mister samhold og blir fosinket.")
    print("Fremdriften har dessverre blit påvirket negativt og teamet opplever disharmoni.")

print("\nSpillet er gjennomført. Takk for din tid\n")
