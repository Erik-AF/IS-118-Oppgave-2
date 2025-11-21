import os
import time

#Rydde terminalen 
os.system("cls")

#Liste godkjente valg alternativer
a = ("a", "A", "Alternativ A", "Valg A")
b = ("b", "B", "Alternativ B", "Valg B")


#Funksjon som sjekker at input er en av de godkjente valg alternativene
def validate_choice(x):     
    while True:
        if x in a:
            return x
        elif x in b:
            return x
        else:
            x = input("Du må velge en av de godkjente alternativene: ")
            

#Første konflikt
def first_conflict():
    #Legger grunnlag for første konflikt       
    print("Konflikt 1: Silje og Sivert Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt.")
    print("\n• Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon.")
    print("• Sivert mener Siljes forslag er urealistisk, usikkert og for kostbart.")
    print("Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.")
    print("\nHvordan vil du løse konflikten mellom Silje og Sivert?")
    print("\nA: Ta personlige samtaler. (Først ringe for å høre begges side av saken, så medarbeidersamtale med begge tilstede)")
    print("\nB: Ta det opp i plenum grunnet alvorligheten av saken")
    choice = input("\nHva vil du gjøre for å løse konflikten alternativ A eller B: ")
    first_encounter = validate_choice(choice)

    if first_encounter in a:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte A: Ta personlige samtaler. (Først ringe for å høre begges side av saken, så medarbeidersamtale med begge tilstede")
        print("\nKosekvens av ditt valg:")
        print("\nDet viser seg slik at spenningen mellom de to partene har nådd topplokket og møtet slår seg vrang.")
        print("Konflikten har tilsynelatende pågått alt for lenge uten innblanding.")
        print("\n--------------------------------------------------------------------")
        return "negativ"

    elif first_encounter in b:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte B: Ta det opp i plenum grunnet alvorligheten av saken")
        print("\nKosekvens av ditt valg:")
        print("\nTeamet lufter nye ideer eller utdypende tanker som etterlater Silje og Sivert inspirerte.")
        print("De er nå fulle av nytenkning takket være alle de gode forslagene fra medarbeiderne sine.")
        print("\n--------------------------------------------------------------------")
        return "positiv"


#Andre konflikt
def second_conflict():
    #Legger grunnlag for for Andre konflikt       
    print("\nKonflikt 2: Samtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi(kulturavdelingen) og Jabir(brukerrepresentant).")
    print("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter:")
    print("\n• Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
    print("• Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
    print("\nHvordan vil du løse konflikten mellom Hamdi og Jabir?")
    print("\nA: Sette opp et strukturert møte med klare rammer,  og gir rom for at både Hamdi og Jabir kan argumentere og utdype sine perspektiver.")
    print("\nB: La Hamdi og Jabir prøve ut sine egne løsninger parallelt, og håper at de selv klarer å finne en vei mot enighet.")
    choice1 = input("\nHva vil du gjøre for å løse konflikten alternativ A eller B: ")
    second_encounter = validate_choice(choice1)

    if second_encounter in a:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte A: Sette opp et strukturert møte med klare rammer,  og gir rom for at både Hamdi og Jabir kan argumentere og utdype sine perspektiver.")
        print("\nKosekvens av ditt valg:")
        print("\nDenne tilnærmingen styrker motivasjonen og bidra til at teamet beveger seg fra storming-fasen til norming-fasen")
        print("Dette fører også til positivitet, skaper økt tillit, bedre samarbeid og en tydelig felles kurs.")
        print("\n--------------------------------------------------------------------")
        return "positiv"

    elif second_encounter in b:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte B: La Hamdi og Jabir prøve ut sine egne løsninger parallelt, og håper at de selv klarer å finne en vei mot enighet.")
        print("\nKosekvens av ditt valg:")
        print("\nDette fører til sløsing av resurser og prosjektet mister fremdrift.")
        print("\n Det blir en taper vinner situasjonen der Hamdi eller Jabir gir etter, og kun ett av deres ønske blir utfylt.")
        print("\nResultat av valget ditt")
        print("\n--------------------------------------------------------------------")
        return "negativ"
    
#Tredje konflikt
def third_conflict():
    #Legger grunnlag for for tredje konflikt       
    print("\nKonflikt 3: Hvordan bevare motivasjonen i teamet som helhet?.")
    print("\nHvordan vil du prøve å bevare motivasjonen for teamet?")
    print("\nA: Små feiring av milepæler")
    print("\nB: Organisere sosiale møter og workshops, eller anerkjenne det de har nådd fram til nå")
    choice2 = input("\nHva vil du gjøre for å løse konflikten alternativ A eller B: ")
    third_encounter = validate_choice(choice2)

    if third_encounter in a:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte A: Små feiring av milepæler")
        print("\nKosekvens av ditt valg:")
        print("Dette gir positiv energi og synliggjør fremdrift og motiverer mot fremtidige mål.")
        print("\n--------------------------------------------------------------------")
        return "positiv"

    elif third_encounter in b:
        print("\n--------------------------------------------------------------------")
        print("\nDu valgte B: Organisere sosiale møter og workshops, eller anerkjenne det de har nådd fram til nå")
        print("\nKosekvens av ditt valg:")
        print("\nDette fører til at medarbeiderne kan dele høydepunkter og utfordringer og at de ikke føler seg alene i utfordringene.")
        print("Men dette fører til et miljø for videre polarisering i teamet der problemene smittes over til de andre og det blir valg av sider og teamet splittes.")
        print("\n--------------------------------------------------------------------")
        return "negativ"




## Selve historien
first_result = first_conflict()
time.sleep(7)
second_result = second_conflict()
time.sleep(7)
third_result = third_conflict()
time.sleep(7)

choices = (first_result, second_result, third_result)

if choices.count("positiv") == 3:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif choices.count("negativ") == 3:
    print("Prosjektet mister samhold og forsinkes.")
else:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")

