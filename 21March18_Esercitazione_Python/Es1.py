# Esercizio Bubble Sort



# Bubble sort
# alla prima iterazione, scandisco l'array e swappo tutti gli elementi
# col successivo se più grandi, e così succede che il più grande viene
# definitivamente confinato alla fine.
# alla seconda iterazione, scandisco l'array fino al penultimo elemento
# e ripeto così definitivamente trovo il penultimo

x = [3,2,10,24,1,63,7,33,45,73]
"""
# Implementazione naive
indice = len(x)-1
while indice >= 0:
    for i in range(indice):
        if x[i] > x[i+1]:
            x[i],x[i+1] = x[i+1], x[i]
    indice = indice - 1
"""

# Implementazione con doppio for
for indice in reversed(range(len(x))):
    for i in range(indice):
        if x[i] > x[i+1]:
            x[i],x[i+1] = x[i+1], x[i]

print(x)
