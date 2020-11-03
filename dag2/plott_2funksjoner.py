
from pylab import *

def f(x):
    return x**2 + 2*x - 1

def g(x):
    return 2/x


xverdier = linspace(-5, 5, 200)
yverdier = f(xverdier)

xverdier2 = linspace(-5, 5, 201)
yverdier2 = g(xverdier2)

plot(xverdier, yverdier, label="f(x) = x**2 + 2x - 1")
plot(xverdier2, yverdier2, label="g(x) = 2/x")

legend()
xlabel("x")
ylabel("y")
title("To funksjoner")
savefig("plott.png")
show()
