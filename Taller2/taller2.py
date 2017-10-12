import numpy as np
import matplotlib.pyplot as plt

G = 6.674*10**(-11)
dsuelo = 2600.0
p = 4.0*np.pi*10.0**(-7)
F = 0.00004
M = (0.1-0.0001)*F

#Caso Esfera Punto 1
def anomEsfera(x,z, desf):
	r= 1000.0
	return (4/3)*np.pi*G*(r**3)*(desf-dsuelo)*z/(((x)**2+(z)**2)**(3/2))

def MagnEsf(x,z):
	R=1000.0
	return(1/3)*p*(R**3)*M*(2*z*z-x*x)/((z*z+x*x)**(5/2))

x = np.linspace(-8000,8000,1000)

z1 = 2000.0
esf1 = anomEsfera(x,z1,3000.0)
esfMag = MagnEsf(x,z1)
y = esf1/max(esf1)
	
plt.plot(x,y)
plt.show()
plt.close()

#Caso Cilindro
def anomCil(x,z, dcil):
	r= 1000.0
	return 2*np.pi*G*(r**2)*(dcil-dsuelo)*z/((x)**2+(z)**2)

def MagnCil(x,z):
	R=1000
	return(1/2)*p*(R*R)*M*(z*z-x*x)/((z*z+x*x)**(2))

cil1 = anomCil(x,z1, 3000.0)
cilMag = MagnCil(x, z1)

plt.plot(x,cilMag)
plt.show()
plt.close()







