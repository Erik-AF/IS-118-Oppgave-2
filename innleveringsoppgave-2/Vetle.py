



# lager en pause funksjon, bruker må trykke enter for å fortsette
def pause():
    input("trykk enter for å fortsette...")  

#forklaring av scenario, Bruk av \n for avstand mellom linjer
print("\nDu er leder for ett team som skal utvikle en digital medborgerportal.")
print("\nteamet skal levere en prototype om 6 uker, men det er konflikter i teamet.")
print("\ndu må nå som leder Erling ta noen valg for å håndtere konfliktene og motivasjonen i teamet.")
print("\nLykke til!")

#bruk av pause funksjon
pause() 
#printer en linje i terminal for å separere valg
print("------------------------------------------------------------------")

#printer første valg, håndtere konflikten mellom silje og sivert
print("silje og sivert har en konflikt og du som leder må håndtere det: du kan velge å ta det opp i plenum (valg A) eller ha en personlig samtale med de to (valg B).")

#bruker må skrive A eller B, store og små bokstaver godtas.
valg_1 = input("skriv A eler B: ").upper()

#sjekker om input er gyldig, hvis ikke spør coden igjen.
while valg_1 not in ["A", "B"]:
    valg_1 = input("ugyldig valg, vennligst skriv A eller B: ").upper() 

#resultat av valg A
if valg_1 == "A": 
     print("du tar det opp i plenum og konflikten løses.") 
     pause()

#resultat av valg B, valg B gir to nye valg ved bruk av if else i den første else setningen.
else:
     print("du har en personlig samtale med de to, men møtet går dårligere og forværrer situasjonen.") 
     print("du kan sende saken vidre til HR (valg 1) eller ta en sjefsavgjørese (valg 2).")
     valg_B2 = input("skriv 1 eller 2:") 
    
     while valg_B2 not in ["1", "2"]:
            valg_B2 = input("ugyldig valg, vennligst skriv 1 eller 2:")

     if valg_B2 == "1":
        print("du sender saken vidre til HR, noe som forværrer relasjonene mellom de to.")

     else:
          print("Erling tar valget selv, noe som forværrer relasjonene mellom de to.")
          pause()

print("------------------------------------------------------------------")



#printer valg 2, konflikten mellom Hamdi og Jabir.
print("Hamdi og Jabir har en konflikt og du som leder må håndtere det: du kan velge å sette opp et møte mellom de to (valg A) elelr la situasjonen løse segselv (valg B).")

#bruker må skrive A eller B, både store og små bokstaver godtas.
valg_2 = input("skriv A eller B: ").upper()

#sjekker om input er gyldig, hvis ikke spør coden igjen:
while valg_2 not in ["A", "B"]:
    valg_2 = input("ugyldig valg, vennligst skriv A eller B: ").upper()

#resultat av valg A og B, med if else setning.
if valg_2 == "A": 
    print("du setter opp et møte mellom de to, og konflikten forbedrer relasjonene.") 

else: 
    print("du lar situasjonen løse seg selv, noe som resulterer i at konflikten ikke løser seg og sløser tid ogr ressurser.")

pause()

print("------------------------------------------------------------------")




#printer valg 3, hådtere teamets motivasjon
print("teamet ditt er umptivert og trenger noe for å øke motivasjonen: du kan velge å lage en felles lunsj med kaffe og en god pause fra arbiedet (valg A) elelr arrangere en feiring av hvor langt teamet har kommet (valg B).")

#bruker må skrive A eller B, bade store og små bokstaver godtas.
valg_3 = input("skriv A eller B: ").upper()

#sjekker om imput er gyldig.
while valg_3 not in ["A", "B"]:
    valg_3 = input("ugyldig valg, vennligst skriv A eller B: ").upper()

# if else setning for resultat av valg 3
if valg_3 == "A": 
 print("du lager en felles lunjs med kaffe og ett godt avbrekk fra arbeiet, noe som senker terksl for dialog og skaper trygghet i teamet, dette øker motiavasjon.")

else:
 print("du arrangerer en feiring av hvor langt dere har kommet som team, noe som sløser tid og ressurser.") 
 pause()

print("------------------------------------------------------------------")



#sjekekr kombinasjonen av valg 1, 2 og 3 for å gi en avsluttende melding.
#bruk av if elif else for å sjekke kombinasjonene. 

if valg_1 == "A" and valg_2 == "A" and valg_3 == "A": 
    print("teamet gjennoppretter tillit og går vidre til norming-fasen.")

elif valg_1 == "B" and valg_2 == "B" and valg_3 == "B":
    print("prosjektet mister sammholdet og forsinkes delevis.")

else:
    print("konflikten løses delevis, men relasjoner er fortsatt sårbare.")

