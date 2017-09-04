import numpy as np
import matplotlib.pyplot as plt

G = 6.674*10**(-11)
dsuelo = 2700.0

#Caso Esfera
def anomEsfera(x,z, desf):
	r= 10.0
	return (4/3)*np.pi*G*(r**3)*(desf-dsuelo)*z/(((x)**2+(z)**2)**(3/2))

x = np.linspace(-120,120,1000)

z1 = 20.0
z2 = 40.0
z3 = 60.0
esf1 = anomEsfera(x,z1,3500.0)
esf2 = anomEsfera(x,z2,3500.0)
esf3 = anomEsfera(x,z3,3500.0)
Diapiro = anomEsfera(x,z2,2000.0)


plt.plot(x,esf1, label = "z = 20")
plt.plot(x,esf2, label = "z = 40")
plt.plot(x,esf3, label = "z = 60")
plt.plot(x,Diapiro, label = "z = 40, Diapiro(densidad menor)")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")
plt.title("Efecto de gravedad de una esfera")
plt.tight_layout()
plt.savefig("AEsfera.pdf")
plt.close()


#relacion xhalf y z
xhalf1 = 2*(2*np.log(2))**0.5*np.std(esf1)
xhalf2 = 2*(2*np.log(2))**0.5*np.std(esf2)
xhalf3 = 2*(2*np.log(2))**0.5*np.std(esf3)
xhalfDip = 2*(2*np.log(2))**0.5*np.std(Diapiro)

#print xhalf1, xhalf2, xhalf3, xhalfDip
#NOSALEEE


#Caso Cilindro
def anomCil(x,z, dcil):
	r= 10.0
	return 2*np.pi*G*(r**2)*(dcil-dsuelo)*z/((x)**2+(z)**2)

cil1 = anomCil(x,z1, 10000.0)
cil2 = anomCil(x,z2, 10000.0)
cil3 = anomCil(x,z3, 10000.0)

plt.plot(x,cil1, label = "P. Somera")
plt.plot(x,cil2, label = "P. Media")
plt.plot(x,cil3, label = "P. Profunda")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")
plt.title("Efecto de gravedad de un cilindro horizontal")
plt.tight_layout()
plt.savefig("ACilindro.pdf")
plt.close()

#relacion xhalf y z cilindro
xm1 = 2*(2*np.log(2))**0.5*np.std(cil1)
xm2 = 2*(2*np.log(2))**0.5*np.std(cil2)
xm3 = 2*(2*np.log(2))**0.5*np.std(cil3)

print z1/xm1, z2/xm2, z3/xm3

#Caso Losa
def anomLosa(x, h, z, dLosa):
	return 2*G*(dLosa-dsuelo)*h*(np.pi/2 + np.arctan(x/z))

L1 = anomLosa(x, 20.0, 10.0, 10000.0)
L2 = anomLosa(x, 30.0, 20.0, 5000.0)
L3 = anomLosa(x, 40.0, 50.0, 7000.0)

#Grafica efecto de gravedad de una losa
plt.plot(x,L1, label = "h = 20, p. somera, densidad = 10000 ")
plt.plot(x,L2, label = "h = 30, p. media, densidad = 5000")
plt.plot(x,L3, label = "h = 40, p. profunda, densidad = 7000")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")
plt.title("Efecto de gravedad de una losa")
plt.tight_layout()
plt.savefig("ALosa.pdf")
plt.close()

#Primera derivada
def Dx(x, h, z, dLosa):
	return 2*G*(dLosa-dsuelo)*h*(z/(x*x+z*z))

dxL1 = Dx(x, 20.0, 10.0, 10000.0)
dxL2 = Dx(x, 30.0, 20.0, 5000.0)
dxL3 = Dx(x, 40.0, 50.0, 7000.0)

#Segundas derivadas
def D2x(x, h, z, dLosa):
	return 2*G*(dLosa-dsuelo)*h*(-2*x*z/(x*x+z*z)**2)

d2xL1 = D2x(x, 20.0, 10.0, 10000.0)
d2xL2 = D2x(x, 30.0, 20.0, 5000.0)
d2xL3 = D2x(x, 40.0, 50.0, 7000.0)

#Grafica derivadas
plt.subplot(3,1,1)
plt.plot(x,dxL1, label = "primera derivada ")
plt.plot(x,d2xL1, label = "segunda derivada ")
plt.title("Anomalia 1 (h = 20, p. somera, densidad = 10000)")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")

plt.subplot(3,1,2)
plt.plot(x,dxL2, label = "primera derivada ")
plt.plot(x,d2xL2, label = "segunda derivada ")
plt.title("Anomalia 2 (h = 30, p. media, densidad = 5000)")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")

plt.subplot(3,1,3)
plt.plot(x,dxL3, label = "primera derivada ")
plt.plot(x,d2xL3, label = "segunda derivada ")
plt.title("Anomalia 3 (h = 40, p. profunda, densidad = 7000)")
plt.legend(loc=0)
plt.xlabel("x(m)")
plt.ylabel("g(mGal)")

plt.tight_layout()
plt.savefig("derivadas.pdf")
plt.close()







