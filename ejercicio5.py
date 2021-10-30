dinero=2000
preciodelhelado=100
incrementodelpreciodelhelado=1.20
edad=19
hambrequesatisfaceelhelado=edad
hambresatisfecho=edad
n=0
while (hambresatisfecho<85 and dinero>0):
    dinero=dinero-(preciodelhelado)
    hambresatisfecho=hambresatisfecho+hambrequesatisfaceelhelado
    preciodelhelado=preciodelhelado*incrementodelpreciodelhelado
    n=n+1
print("te tienes que comer", n, "helados para llenarte")
print("te queda", dinero, "euros")