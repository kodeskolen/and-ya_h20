
z = 2

def f(x):
    z = 3
    return x**2 + 2*x - 1


xverdi = 1
yverdi = f(xverdi)

print(f"f({xverdi}) = {yverdi}")

print(z)