import random
dinero=2000
edad=random.randrange(0,50)
hambre=edad
hambrehelado=edad
preciohelado=100
incrementopreciohelado=1.20
n=0
while(hambre<85 and dinero>0):
    dinero=dinero-preciohelado
    hambre=hambre+hambrehelado
    preciohelado=preciohelado*incrementopreciohelado
    n=n+1
print("tienes", edad, "años")
print("te tienes que comer", n, "helados para llenarte")
print("te queda", dinero, "euros")