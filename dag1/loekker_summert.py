"""

Program som summerer opp tallene 1-5.

"""

summert = 0

for tall in range(1, 6):
    #summert = summert + tall
    summert += tall

print(f"Summen av tallene er {summert}.")


