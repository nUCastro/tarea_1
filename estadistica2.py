import numpy as np
import scipy as s
from scipy.misc import comb
from pylab import *
import matplotlib.pyplot as plt

r=np.linspace(0,1,10001)

c=comb(33,18)
x,y=[],[]
for i in r:
	j=1.0*i
	numero=(c*((j)**18*(1-j)**15))
	
	x.append(i)
	y.append(numero)

plt.plot(x,y,'^b')

plt.show()
#La resta es el dx, que funcionara como integrador
lisga=dot((r[124]-r[123]),y)


asd=0
cdf=[]
tt=sum(y)
for i in y:
	asd=(asd+(i/tt))
	cdf.append(asd)
	
plt.plot(x,cdf,'<b')
plt.ylim(0,1)
plt.xlabel("Rango de r")
plt.ylabel("CDF")
plt.show()	


cd1,cd2=[],[]
y=y/sum(y)
for i in range(len(y)):
	if i<0.5*len(y):
		cd1.append(y[i])
	if i>0.5*len(y):
		cd2.append(y[i])

print sum(cd1),sum(cd2)		
