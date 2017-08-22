import numpy as np
import matplotlib.pyplot as plt

G = 6.674*10**(-11)
dsuelo = 50.0

#Caso Esfera
def anomEsfera(x,z, desf):
	r= 10.0
	return (4/3)*np.pi*G*(r**3)*(desf-dsuelo)*z/(((x)**2+(z)**2)**(3/2))

x = np.linspace(-80,80,100)

z1 = 20.0
z2 = 40.0
z3 = 60.0
esf1 = anomEsfera(x,z1,100.0)
esf2 = anomEsfera(x,z2,100.0)
esf3 = anomEsfera(x,z3,100.0)
Diapiro = anomEsfera(x,z2,25.0)

ze1 = esf1/max(esf1)
ze2 = esf2/max(esf2)
ze3 = esf3/max(esf3)
zDiapiro = Diapiro/abs(min(Diapiro))

plt.plot(x,ze1, label = "z = 20")
plt.plot(x,ze2, label = "z = 40")
plt.plot(x,ze3, label = "z = 60")
plt.plot(x,zDiapiro, label = "z = 20, Diapiro(densidad menor)")
plt.legend(loc=0)
plt.savefig("AEsfera.pdf")
plt.close()


#relacion xhalf y g
ge1= max(esf1)/2
ge2= max(esf2)/2
ge3= max(esf3)/2
geDip= max(Diapiro)/2

v = 0
val1 = 0
val2 = 0
val3 = 0
valDip = 0
while v<len(x):
	if x[v]==ge1:
		val1 = v
	v+=1

while v<len(x):
	if x[v]==ge2:
		val2 = v
	v+=1

while v<len(x):
	if x[v]==ge3:
		val3 = v
	v+=1

while v<len(x):
	if x[v]==geDip:
		valDip = v
	v+=1

x1med = 2*val1
coesf1 = x1med/z1

x2med = 2*val2
coesf2 = x2med/z2

x3med = 2*val3
coesf3 = x3med/z3

xDipmed = 2*valDip
coesfDip = xDipmed/z2


#Caso Cilindro
def anomCil(x,z, dcil):
	r= 10.0
	return 2*np.pi*G*(r**2)*(dcil-dsuelo)*z/((x)**2+(z)**2)

cil1 = anomCil(x,20.0, 100.0)
cil2 = anomCil(x,40.0, 100.0)
cil3 = anomCil(x,60.0, 100.0)

zcil1 = cil1/max(cil1)
zcil2 = cil2/max(cil2)
zcil3 = cil3/max(cil3) 

plt.plot(x,zcil1, label = "P. Somera")
plt.plot(x,zcil2, label = "P. Media")
plt.plot(x,zcil3, label = "P. Profunda")
plt.legend(loc=0)
plt.savefig("ACilindro.pdf")
plt.close()

#Caso Losa
def anomLosa(x, h, z, dLosa):
	r = 10.0
	return 2*G*(dLosa-dsuelo)*h*(np.pi/2 + np.arctan(x/z))

L1 = anomLosa(x, 20.0, 10.0, 100.0)
L2 = anomLosa(x, 30.0, 20.0, 20.0)
L3 = anomLosa(x, 40.0, 50.0, 150.0)

zL1 = L1/max(L1)
zL2 = L2/max(L2)
zL3 = L3/max(L3)

plt.plot(x,zL1, label = "h = 20, z = 10, densidad = 100 ")
plt.plot(x,zL2, label = "h = 30, z = 20, densidad = 20")
plt.plot(x,zL3, label = "h = 40, z = 50, densidad = 150")
plt.legend(loc=0)
plt.savefig("ALosa.pdf")




