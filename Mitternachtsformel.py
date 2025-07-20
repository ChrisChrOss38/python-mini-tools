#QuadGleichung
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
print("Dies ist ein Rechner für die Quadratische Gleichung ax^2 + bx + c  = 0")
#print("Zum Beenden des Rechners geben Sie e ein.")

while True:

    a=int(float(input("Geben Sie hier die Zahl a ein: ")))
    if a == 0:
        print("Durch 0 darf man nich teilen!")
        continue
    b=int(float(input("Geben Sie hier die Zahl b ein: ")))
    c=int(float(input("Geben Sie hier die Zahl c ein: ")))
    liste=[]
 #   if a or b or c =="a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z":
   #     print("Es müssen Zahlen sein!")
     #   continue
    #d=int(4)
    #e=int(2)
    def QuadGleichung():
        x_1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        print("Das Ergebnis für x1 lautet: " + str(round(x_1, 4)))
        x_2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        print("Das Ergebnis für x2 lautet: " + str(round(x_2, 4)))
        liste.append(round(x_1, 4))
        liste.append(round(x_2, 4))
        print(liste)
    QuadGleichung()
    plt.plot(liste)
    plt.show()
    
    print("-------------------------")
    print("Weiter Rechnen? y/n")
    Exit=input()
    if Exit == "y":
        print(":-)")
        continue
    if Exit == "n":
        print("Danke für Ihr Vertrauen")
        sys.exit()
       
    
