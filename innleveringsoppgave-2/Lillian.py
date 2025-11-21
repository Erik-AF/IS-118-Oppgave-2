print("\nHei og velkommen til min interaktive historie!")
print("\nI denne historien er du leder for et team som skal utvikle en digital medarbeiderportal")
print("\nEtter seks uker med arbeid, begynner teamet å møte på sine første utfordringer. Det oppstår en konflikt mellom to teammedlemmer, Silje og Sivert, og det bygger seg også opp en konflikt mellom Hamdi og Jabir.")
print("\nDu tar rollen som prosjektleder Erling, og må ta viktige beslutninger for å unngå å eskalere konflikter og opprettholde motivasjon i teamet.")
print("\nLykke til!")

print("------------------------------------------------------------------------------------------------------------------------------------------------")

print("Det oppstår en konflikt mellom to teammedlemmer, Silje og Sivert, og du som prosjektleder må håndtere situasjonen. Du kan (A) ta det opp i plenum eller (B) kalle inn Silje og Sivert til medarbeidermekling.")

#Bruker må skrive A eller B, store og små bokstaver godtas.

Choice1 = input("Skriv A eller B for å velge:") .upper()

#Sjekker om input er riktig, hvis ikke spør koden igjen. 
while Choice1 not in ["A", "B"]:
    Choice1 = input("Ugyldig valg. Vennligst skriv A eller B: ").upper()
    
#Resultat av valg A:

if Choice1 == "A":
    print("Du velger å ta det opp i plenum. Dette fører til at konflikten mellom Silje og Sivert løses.")
    print("Silje og Sivert føler seg inspirerte og fulle av nytenking etter møtet.")
    
#Resultat av valg B:

elif Choice1 == "B":
    print("Du velger å kalle inn Silje og Sivert til medarbeidermekling. Dette fører til at konflikten mellom Silje og Sivert eskalerer.")
    print("Konflikten mellom Silje og Sivert eskalerer og de føler seg frustrerte etter møtet.")
    
    print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Resultat av valg B gir to nye valg:
 
    print("Etter medarbeidermeklingen har konflikten mellom Silje og Sivert eskalert.")
    print("Erling har nå to valg: (A) Han kan involvere HR for å mekle mellom Silje og Sivert, eller (B) han tar selv en avgjørelse om uenigheten mellom dem.")
    Choice2 = input("Skriv A eller B for å velge: ") .upper()
    
    while Choice2 not in ["A", "B"]: 
        Choice2 = input("Ugyldig valg. Vennligst skriv A eller B: ").upper()
        
    if Choice2 == "A":
        print("Du velger å involvere HR for å mekle mellom Silje og Sivert.")
        print("Dette fører til at konflikten mellom Silje og Sivert forverres ytterligere.")

    elif Choice2 == "B":
        print("Du velger å ta selv en avgjørelse om uenigheten mellom dem.")
        print("Dette fører til at relasjonen mellom Silje og Sivert forverres ytterligere.")

print("------------------------------------------------------------------------------------------------------------------------------------------------")   

print("En annen konflikt oppstår i teamet, denne gangen mellom Hamdi og Jabir.")
print("Erling har nå to valg: (A) Han kan sette opp et møte mellom Hamdi og Jabir for å diskutere konflikten, eller (B) han lar situasjonen løse seg selv over tid.")
Choice3 = input("Skriv A eller B for å velge: ") .upper()

while Choice3 not in ["A", "B"]:
    Choice3 = input("Ugyldig valg. Vennligst skriv A eller B: ").upper()

#Resultat av valg A:

if Choice3 == "A":
    print("Du velger å sette opp et møte mellom Hamdi og Jabir for å diskutere konflikten.")
    print("Dette fører til at relasjonen mellom Hamdi og Jabir bedres.")
    
#Resultat av valg B:
    
elif Choice3 == "B":
    print("Du velger å la situasjonen løse seg selv over tid.")
    print("Dette fører til at relasjonen mellom Hamdi og Jabir forverres, og de sløser tid og ressurser.")
    
print("------------------------------------------------------------------------------------------------------------------------------------------------")   

print("Det siste valget erling må ta omhandler motivasjonen i teamet.")
print("Erling har to valg: (A) Han kan arrangere sosiale tiltak som kaffepause og lunsj for å senke terskelen og skape dialog, eller (B) han kan arrangere små feiringer av milepæler i prosjektet for å øke motivasjonen.")
choice4 = input("Skriv A eller B for å velge: ") .upper()

while choice4 not in ["A", "B"]:
    choice4 = input("Ugyldig valg. Vennligst skriv A eller B: ").upper()
    
#Resultat av valg A:

if choice4 == "A":
    print("Du velger å arrangere sosiale tiltak som kaffepause og lunsj for å senke terskelen og skape dialog.")
    print("Dette fører til at motivasjonen i teamet ikke øker, og du sløser tid og ressurser.")

#Resultat av valg B:
elif choice4 == "B":
    print("Du velger å arrangere små feiringer av milepæler i prosjektet for å øke motivasjonen.")
    print("Dette fører til at du senker terskelen og skaper dialog og trygghet i teamet.")

print("------------------------------------------------------------------------------------------------------------------------------------------------")   

print("Gjennom dine valg som prosjektleder har du navigert gjennom konflikter og motivasjonsutfordringer i teamet.")
print("De ulike valgene du har tatt som prosjektleder vil ha konsekvenser for sluttresultatet til prosjektet og teamets trivsel.")

if (Choice1 == "A" and Choice3 == "A" and choice4 == "B"):
    print("Gratulerer! Dine valg har ført til et vellykket prosjekt med høy motivasjon og gode relasjoner i teamet. Teamet gjenoppretter tillit og går videre til norming-fasen")
elif (Choice1 == "B" and Choice3 == "B" and choice4 == "A"):
    print("Dine valg har ført til at teamet mister samhold og forsinkes.")
else:
    print("Dine valg har ført til utfordringer i prosjektet og lav motivasjon i teamet. Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    
    
print("------------------------------------------------------------------------------------------------------------------------------------------------")   
    

print("Takk for at du spilte min interaktive historie om konflikthåndtering og motivasjon i team!")