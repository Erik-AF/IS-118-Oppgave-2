print("du er sjef i et team")
print("teamet mitt skal levere en prototype om 6 uker")
print("du er leder Erlng, og du må ta en rekke valg for å løse konflikter i teamet")

print("konflikten mellom Silje og Sivert må løses, du kan velge å ta det i plenum (A) eller ta en personlig samtale med hver av dem (B)")
Valg_1 = input("skriv A eller B:").upper()
if Valg_1 == "A":
    print("du velger å ta det i plenum, og konflikten løser seg")
    
else:
    print("du velger å ta en personlig samtale, noe som fører til at konflikten eskalerer")
    
print("-----------------------------------------------------------------------")
    
print("Konflikter mellom Hamdi og Jaber må også løses, du kan velge å sette opp et møte mellom Hamdi og Jaber (A), eller så lar han konflikten løse seg selv (B)")
Valg_2 = input("skriv A eller B:").upper()
if Valg_2 == "A":
    print("du velger å sette opp et møte, og konflikten løses seg")
    
else:
    print("du velger å la konflikten løse seg selv, noe som fører til at konflikten eskalerer")
    
print("-----------------------------------------------------------------------")
   
   
print("Felleskonflikten i teamet må også løses, den handler om å bevare teamets motivasjon. Du kan velge mellom å ha kaffepauser/felleslunsj (A) eller feire milepæler (B)")
Valg_3 = input("skriv A eller B:").upper()
if Valg_3 == "A":
       print("du velger å ha kaffepauser/felleslunsj, og teamets motivasjon bevares")
       
else:
       print("du velger å feire milepæler, noe som fører til at teamets motivasjon synker")
       
print("-----------------------------------------------------------------------")
       

if Valg_1 == "A" and Valg_2 == "A" and Valg_3 == "A":
    print("Teamet gjennoppretter tillit og går videre til norming-fasen")

elif Valg_1 == "B" and Valg_2 == "B" and Valg_3 == "B":
    print("Prosjektet mister samholdet og forsinkes delvis.")

else: 
    print("Konflikten løses delvis, men relasjoner er fortsatt sårbare.")   
               