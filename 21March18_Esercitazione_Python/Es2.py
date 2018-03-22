def fun(x):
    return x**2+1

# Calcolo integrale semplificato
num_interval = 1000
interval_length = 2
dx = interval_length/num_interval

val_m = [0]*num_interval
val_M = [0]*num_interval
for i in range(num_interval):
    val_m[i] = fun(1+(i*dx))
    val_M[i] = fun(1+((i+1)*dx))

s, S = 0, 0
for i in range(num_interval):
    s += val_m[i]*dx
    S += val_M[i]*dx

print("Le due somme di Darboux sono:",s,S)
