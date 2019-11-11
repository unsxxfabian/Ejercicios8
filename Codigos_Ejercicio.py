#EJERCICIO 1
import numpy as np
import matplotlib.pyplot as pl

x=[99,75,85,95,90,100,93,80,87,110]

y=[1485,900,1105,1330,1440,1200,1209,1200,1218,1650]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()



#EJERCICIO 2
import numpy as np
import matplotlib.pyplot as pl

x=[20,16,34,10,23]

y=[6.5,6,8,4,7]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()


#EJERCICIO 3
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5]

y=[88,87,84,82,79]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()



#EJERCICIO 4
import numpy as np
import matplotlib.pyplot as pl

x=[30,28,32,25,25,25,22,24,35,40]

y=[25,30,27,40,42,40,50,45,30,25]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()



#EJERCICIO 5
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5,6,7,8,9,10,11,12]

y=[133,292,283,283,302,400,505,608,667,783,785,799]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()




#EJERCICIO 6
import numpy as np
import matplotlib.pyplot as pl

x=[30600,16000,20000,13000,20000,19560,24000,12000,18000,12480,20250,18000,11000,30000,20000]

y=[179000,126500,134500,125000,142000,164000,146000,129000,135000,118500,160000,152000,122500,220000,141000]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()




#EJERCICIO 7
import numpy as np
import matplotlib.pyplot as pl

x=[168,196,170,175,162,169,190,186,176,170,176,179]#es la altura

y=[74,92,63,72,58,78,85,85,73,62,80,72]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()



#EJERCICIO 8
import numpy as np
import matplotlib.pyplot as pl

x=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7]

y=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189]
print(x)
n=len(x)
print("tamaño= ",n)
print(y)

x=np.array(x)
y=np.array(y)
print(x)
print(y)
sumax=sum(x)
print("sumax= ",sumax)
sumay=sum(y)
print("sumay= ",sumay)
promx=sumax/n
print("promx= ",promx)
promy=sumay/n
print("promy= ",promy)
sumax2=sum(x*x)
print("sumax^2",sumax2)

sumaxy=sum(x*y)
print("sumaxy= ",sumaxy)
b=(sumax*sumay-n*sumaxy)/(sumax**2-n*sumax2)
a=promy-b*promx
print("b= ",b," a= ",a)
pl.plot(x,y,'o',label='Datos')
pl.plot(x,a+b*x,label='Ajuste')

pl.xlabel('x')
pl.ylabel('y')

pl.grid()
pl.legend()
pl.show()