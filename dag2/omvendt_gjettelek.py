"""
Gjettelek:
    - Bruker tenker på et tall mellom 1 og 100
    - Datamaskinen får 10 gjett
    - For hvert gjett sier bruker om det er
      riktig, for høyt eller for lavt.
"""

def midtpunkt(a, b):
    return (a + b)/2

maks_antall = 10

minimalt = 1
maksimalt = 2000

for forsøk in range(1, maks_antall + 1):
    gjett = int(midtpunkt(minimalt, maksimalt))
    
    print(f"Dette er forsøk {forsøk}.")
    print(f"Jeg gjetter {gjett}!")
    
    tilbakemelding = input("Er det riktig, for høyt eller for lavt? ")
    
    if tilbakemelding == "riktig":
        print("Hurra! Jeg er en flink datamaskin.")
        break
    elif tilbakemelding == "for høyt":
        maksimalt = gjett
    elif tilbakemelding == "for lavt":
        minimalt = gjett
    else:
        print("Hæ??? Jeg skjønner ikke hva du mener.")
        print("Skriv inn 'riktig', 'for høyt' eller 'for lavt'.")
else:
    print("Jeg klarte dessverre ikke å gjette hvilket tall du tenkte på.")
    print("Jeg er en dum datamaskin. :(")
    print("Jeg skal prøve å bli flinkere til neste gang.")


    


