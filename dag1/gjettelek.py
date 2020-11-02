"""
Gjettelek:
    - Vi tenker på et tall mellom 1 og 100
    - Bruker får 10 gjett
    - For hvert gjett sier vi om det er
      riktig, for høyt eller for lavt.
"""

from random import randint

fasit = randint(1, 1000)
maks_antall = 10

for forsøk in range(1, maks_antall + 1):
    gjett = int(input("Gjett et tall:"))

    if gjett > fasit:
        print("Tallet er for høyt")
    elif gjett < fasit:
        print("Tallet er for lavt.")
    else:
        print("Du gjettet riktig! Gratulerer!")
        break

if gjett != fasit:
    print("Du klarte dessverre ikke å gjette tallet.")
    print(f"Riktig tall var {fasit}. Prøv igjen!")



