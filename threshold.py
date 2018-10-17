import numpy as np
import matplotlib.pyplot as plt


plt.figure(1)
#linear
plt.subplot(2,2,1)
x = np.array([1,2,3,4,5])
m = 2
c = 3
y = m*x + c
plt.plot(x,y)
plt.title("linear fuction")
plt.xlabel("x")
plt.ylabel("y")
#plt.show()

#sigmoidal
plt.subplot(2,2,2)
x = np.linspace(-10,10,30)
a = np.random.random()
y = 1/(1+np.exp(-a*x))
plt.plot(x,y)
#plt.show()

#signam
plt.subplot(2,2,3)
x = np.linspace(-10,10,30)
y = 1*(x>0)
plt.plot(x,y)
#plt.show()

#relu
plt.subplot(2,2,4)
x = np.linspace(-10,10,100)
y = x*(x>0)
plt.plot(x,y)
plt.show()

#log
x = np.linspace(1,50,100)
y = np.log(x)
plt.plot(x,y)
plt.show()

#exponential
x = np.linspace(-10,10,100)
y = np.exp(x)
plt.plot(x,y)
plt.show()



def ReLu(inp):                  #note this another way of writing relu function
    return(max(0,inp))









