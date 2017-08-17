import numpy as np
import matplotlib.pyplot as plt

G = 6.674*10**(-11)
dsuelo = 50.0

#Caso Esfera
def anomEsfera(x,z, desf):
	r = ((x)**2+(z)**2)**(0.5)
	return (4/3)*np.pi*G*(r**3)*(desf-dsuelo)*z/(((x)**2+(z)**2)**(3/2))

x = np.linspace(-50,50,100)


esf1 = anomEsfera(x,20.0,100.0)
esf2 = anomEsfera(x,40.0,100.0)
esf3 = anomEsfera(x,60.0,100.0)
Diapiro = anomEsfera(x,40.0,25.0)

ze1 = esf1/max(esf1)
ze2 = esf2/max(esf2)
ze3 = esf3/max(esf3)
zDiapiro = Diapiro/abs(min(Diapiro))

plt.plot(x,ze1, label = "P. Somera")
plt.plot(x,ze2, label = "P. Media")
plt.plot(x,ze3, label = "P. Profunda")
plt.plot(x,zDiapiro, label = "Diapiro P. Media")
plt.legend(loc=0)
plt.show()
plt.close()


#Caso Cilindro
def anomCil(x,z, dcil):
	r = ((x)**2+(z)**2)**(0.5)
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

plt.show()






