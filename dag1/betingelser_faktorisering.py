"""

Program som sjekker om et tall er delelig på 5 og 3, delelig på 5,
delelig på 3 eller hverken delelig på 5 eller 3.

"""


tall = int(input("Skriv inn et heltall: "))

faktor1 = 5
faktor2 = 3


deleligpåfaktor1 = (tall % faktor1) == 0
deleligpåfaktor2 = (tall % faktor2) == 0


if (deleligpåfaktor1 and deleligpåfaktor2):
    print(f"Tallet {tall} er delelig både på {faktor1} og {faktor2}")
elif deleligpåfaktor1:
    print(f"Tallet {tall} er delelig på {faktor1}")
elif deleligpåfaktor2:
    print(f"Tallet {tall} er delelig på {faktor2}")
else:
    print(f"Tallet {tall} er hverken delelig både på {faktor1} eller {faktor2}")

    