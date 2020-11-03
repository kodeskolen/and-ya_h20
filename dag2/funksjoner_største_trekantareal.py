"""

Et program med en funksjon som returnerer arealet av
den største av to trekanter.

"""

def trekantareal(høyde, grunnlinje):
    return høyde*grunnlinje/2

def største_areal(høyde1, grunnlinje1, høyde2, grunnlinje2):
    
    areal1 = trekantareal(høyde1, grunnlinje1)
    areal2 = trekantareal(høyde2, grunnlinje2)
    
    if areal1 > areal2:
        største_areal = areal1
    else:
        største_areal = areal2
        
    return største_areal

h1 = 4
g1 = 3

h2 = 2
g2 = 5

størst = største_areal(h1, g1, h2, g2)

print(f"Det største arealet er {størst}.")
