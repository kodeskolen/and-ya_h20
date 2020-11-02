"""

Program som sjekker hvilke av tallene fra 1 til 100 som er
delelig på 5 og 3, delelig på 5 eller delelig på 3.

"""


faktor1 = 5
faktor2 = 3


for tall in range(1, 101):

    deleligpåfaktor1 = (tall % faktor1) == 0
    deleligpåfaktor2 = (tall % faktor2) == 0


    if (deleligpåfaktor1 and deleligpåfaktor2):
        print(f"Tallet {tall} er delelig både på {faktor1} og {faktor2}")
    elif deleligpåfaktor1:
        print(f"Tallet {tall} er delelig på {faktor1}")
    elif deleligpåfaktor2:
        print(f"Tallet {tall} er delelig på {faktor2}")
    #else:
    #    print(f"Tallet {tall} er hverken delelig både på {faktor1} eller {faktor2}")
