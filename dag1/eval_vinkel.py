"""

Program som bruker numpy sin degrees for
å regne ut arealet av en trekant.

"""

from numpy import degrees, sin

side1 = float(input("Gi meg en sidekant: "))
side2 = float(input("Gi meg en sidekant til: "))
vinkel = float(input("Gi meg en vinkel: "))

areal = 0.5*side1*side2*sin(degrees(vinkel))

print(f"Vinkelen er {vinkel}.")
print(f"Vinkelen er {areal}.")


