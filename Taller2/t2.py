import numpy as np
import matplotlib.pyplot as plt

G = 6.674*10**(-11)
dsuelo = 0.0026
p = 4.0*np.pi*10.0**(-7)

F = 40000.0*10**(-9)
M = ((0.1-0.0001)*F

#Caso Esfera
#def anomEsfera(x,z, desf):
#	r= 1.0
#	return (4/3)*np.pi*G*(r**3)*(desf-dsuelo)*z/(((x)**2+(z)**2)**(3/2))


#def MagneEsf(x,z):
#	R=1.0
#	return(1/3)*(p)*(R**3)*M*(2*z*z-x*x)/((z*z+x*x)**(5/2))


x = np.linspace(-120,120,1000)


z1 = 16.0
esf1 = anomEsfera(x,z1,0.003)
esfMag = anomMagnEsf(x,z1,F)

plt.plot(x,esf1)
plt.plot(x,esfMag, label = "MAg")
plt.legend(loc=0)
plt.show()



