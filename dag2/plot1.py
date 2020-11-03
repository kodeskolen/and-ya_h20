

from pylab import linspace, arange


def f(x):
    return x**2 + 2*x - 1

xverdier = linspace(-5, 5, 21)
yverdier = f(xverdier)


#print(xverdier)
#print(yverdier)

xverdier2 = arange(-5, 5.5, 0.5)
yverdier2 = f(xverdier2)

#print(xverdier2)
#print(yverdier2)

for x in xverdier:
    print(x, end=" ")