
from pylab import *

def f(x):
    return x**2 + 2*x - 1

def g(x):
    return 2/x

plt.figure(figsize=(6, 4))

xverdier = linspace(-5, 5, 200)
yverdier = f(xverdier)

xverdier2 = linspace(-5, 5, 201)
yverdier2 = g(xverdier2)

plot(xverdier, yverdier, 'o-', label="f(x) = x**2 + 2x - 1")
plot(xverdier2, yverdier2, 'o-', label="g(x) = 2/x")

legend()
xlabel("x")
ylabel("y")
title("To funksjoner")
savefig("plott.png")
show()
