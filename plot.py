import matplotlib.pyplot as fig
fig.figure(figsize=(8, 5))
tam = 2




ListaH = []
ListaP = []
for i in range(10):
    ListaH = ListaH + [0]
    ListaP = ListaP + [1]

ListaH = ListaH + [10]
ListaP = ListaP + [1]

#c1 > c3
a = 0.2
b = 1/100
c = 0.8
d = 10**15

e = 0.8
f = 100000000

H = 10
P = 200


def F(e, f, h, p):
    return(e*p**4/(f+p**4)*h/(1+(h/80)**4))

for i in range(500):
   
    dH = F(e, f, H, P) - F(e, f, ListaH[0], ListaP[0])
    dP = P*(a/(1+(b*P)**5)-c*H**8/(d+H**8))
    #print(dH)
    H = H + dH
    P = P + dP
    if H <=0 or P<=0:
        break
    del ListaH[0]
    del ListaP[0]
   
    ListaH = ListaH + [H]
    ListaP = ListaP + [P]
   
    #print(H)
    #print('    ', P)
   
    x1 = i
    y1 = H
    y2 = P
   
    fig.scatter(x1, y1, s=tam, c="mediumblue")
    fig.scatter(x1, y2, s=tam, c="green")
    fig.plot(x1, y1)
    fig.plot(x1, y2)
