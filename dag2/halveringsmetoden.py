"""

Program som finner nullpunktet til en funksjon.

"""

from numpy import cos, sin, sign
from pylab import linspace, plot, show

def f(x):
    return sin(x+1) + x**2 - 5

def midtpunkt(a, b):
    return (a + b)/2


maks_antall_forsøk = 100

minimalt = -6
maksimalt = 6


for forsøk in range(1, maks_antall_forsøk + 1):
    print(f"Dette er forsøk {forsøk}.")

    gjett = midtpunkt(minimalt, maksimalt)

    print(f"Jeg gjetter {gjett}! f({gjett}) = {f(gjett)}.")
    
    if abs(f(gjett)) < 1e-5:
        print("Jeg gjettet riktig! Jeg er en flink datamaskin.")
        break
    elif sign(f(gjett)) == sign(f(maksimalt)):
        maksimalt = gjett
    else:
        minimalt = gjett
        

xverdier = linspace(-6, 6, 100)
yverdier = f(xverdier)
plot(xverdier, yverdier)
plot([gjett], [f(gjett)], 'o', color="red")
show()
