import numpy as np
from pylab import *
import matplotlib.pyplot as plt
ls=[]
#cambiar el numero 1000
for i in range(1000):
	l=[]
	total=0
	for j in range(1000):
		l2=[]
		for k in range(33):
			l2.append(np.random.randint(2))
		l.append(l2)
		if sum(l2)==18:
			total=total+1
	
	s=(total*1.0/1000)*100	
	if i%100==0:
		print s,'%   ', i
	ls.append(s)

plt.hist(ls)
plt.ylabel("Frecuencia")
plt.xlabel("Porcentaje que sale 18 de 33 en 1000 intentos")
plt.show()	
	
