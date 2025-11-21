#Printer en forklaring av situasjonen.
print("Du er leder av et team, og du må håndtere tre ulike konflinkter.")
print("Du skal nå være leder Erling, og ta ulike valg som resulterer om du velger et bra eller dårlig team.")
print("Lykke til!")

#Her får brukeren vite at det er en konflikten mellom Silje og Sivert, og brukeren får et valg om de skal velge A eller B.
print("Silje og Sivert har en konflikt, og du må ta et valg. Valg A, å ta konflikten i plenum, eller valg B, Personlig samtale med begge partene")

#Brukeren får vite to valg, A eller B, h*n får også vite hva disse valgene tilsvarer.
valg_1 = input("Velg A eller B:").upper()
 
 #Jeg bruker "if" hvis brukeren velger A, og jeg bruker "else" hvis brukeren velger B.
if valg_1 == "A" :
  print("Du tar konflikten i plenum, og konflikten løses.")
else:
  print("Du valgte å ha en personlig samtale, noe som forværret situasjonen")
  print("Stemningen er ikke helt på topp, skal du 1, sende saken til HR, eller 2, ta en sjefsavgjørelse?")
  valg_1B = input("Velg 1 eller 2:").upper()
  #Her får brukeren valget om 1 eller 2, jeg bruker "if" hvis brukeren velger 1, og jeg bruker "else" hvis brukeren velger 2
  if valg_1B == "1" : 
     print("Relasjonen forværres")
  else: 
     print("relasjonen forværres")
     

#Her får brukeren innsyn i konflikten til Jabir og Hamdi, brukeren får da valg om enten A eller B.
print("Jabir og Hamdi har en konflikt om de skal bruke den kommunale nettportalen eller ikke. Du kan velge valg A, ha et møte med begge to, eller valg B, la konflikten løse seg selv.")
valg_2 = input("Velg A eller B:").upper()

#Jeg bruker "if" hvis brukeren velger A, og jeg bruker "else" hvis brukerebn velger B.
if valg_2 == "A" :
   print("Møte går bra, og konlikten løste seg")
else:
   print("Du lar konflikten løse seg selv, noe som forværret situasjonen.")

#Her bruker jeg print, for å gi brukeren innsyn i motivasjonen til teamet, for å så gi brukeren noe valg. 
print("Motivasjonen i teamet er lavt, du kan velge mellom Kaffepause, eller feire en milepæl")

#Her har jeg brukt samme metode som tidligere, jeg bruker "if" hvis brukeren velger A, og jeg bruker "else" hvis brukeren velger B.
valg_3 = input("Velg A eller B:").upper()

if valg_3 == "A" :
   print("Du velger å ta en kaffepause med teamet, det forbedrer relasjoner innat i gruppen")
else:
   print("Du feirer en milepæl, dette sløser tid og ressurser og derfor utsettes prosjektet.")


#Dette er slutten av alle konfliktene, brukeren får så vite hvordan valgene h*n har tatt hvordan dette påvirker teamet.
#Jeg har gjort at hvis brukeren velger bare positive handlinger gjennom historien, så får de motivert teamet og det løser konflikten. 
#Hvis brukeren bare velger bare negative handlinger, så resulterer det i at konflikten ikke blir løst, teamet er ikke motivert og prosjektet blir forsinket. 
#hvis brukeren blander positive og negative handligner, så resulterer det med at noen av konflikten har løst seg, men det er fortsatt dårlig stemning i teamet.
if valg_1 == "A" and valg_2 == "A" and valg_3 == "A" :
   print("Du har tatt riktig valg, og teamet er motivert og konfliktfri.")
elif valg_1 == "B" and valg_2 == "B" and valg_3 == "B" :
   print("Du har ikke løst konflikten, teamete er ikke motivert og prosjektet er forsinket.")
else:
   print("Du har løst noen konflikter, men det er fortsatt dårlig stemning i teamet.")



