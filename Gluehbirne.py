import numpy as np
import matplotlib.pyplot as plt
import math

#Konstanten für Wolframdraht Sm/mm²
a20 = 0.0044  
b20 = 0.0001  
k20 = 18.2  
v0 = 20      #kalter Einschatzustand 20 °C (Temperaturkonstante)

v = 20        #Für den Graphen von 20-2200 °C

#Widerstand der mit der Formel berechnet wird eingeben
R20=float(input("Gib den Widerstand R20 (in Ohm) bei 20 °C ein: "))  

liste=[]

#Wertebereich Temp.
while v <=1200:
    R=(R20*(1+a20*(v-v0)) +b20*((v-v0)**2))
    v = v+1
    #print(R)
    liste.append(R)
    
plt.figure(figsize=(12, 6))
plt.plot(liste, label='Parabelverlauf des Widerstandes')
plt.xlabel('Temperatur in °C', fontsize=13)
plt.ylabel('Widerstand in Ohm', fontsize=13)
plt.xticks([500, 1000, 1500])
plt.yticks([0, 100, 200, 400, 600, 800, 1000])
plt.title('Widerstand eines Glühdrates in Abhängigkeit von der Temperatur mit Wolframdraht', fontsize=16, color='blue')
plt.grid(True)
plt.legend()
plt.show()