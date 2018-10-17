#normal perceptron
import numpy as np
def signum(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1
# inputs [bias=1,in1,in2]
x=np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
d=np.array([1,-1,-1,-1])  #outputs
# Single Neuron
e=1
lr=1
w=np.array([0, 0])
b=0
r,c=x.shape

for k in range(e):
    for i in range(r):
        s=np.sum(x[i]*w)
        y=signum(s+b)
    
        if y!=d[i]:
            w=w+lr*x[i]*d[i]
            b=b+lr*d[i]
        print(w,b)



#delta or Window Hoff rule perceptron

import numpy as np
def signum(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1
# inputs [bias=1,in1,in2]
x=np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
d=np.array([1,-1,-1,-1])  #outputs
# Single Neuron
e=1
lr=1
w=np.array([0, 0])
b=0
[r,c]=x.shape

for k in range(e):
    for i in range(r):
        s=np.sum(x[i]*w)
        y=signum(s+b)
    
        if y!=d[i]:
            w=w+lr*x[i]*(d[i]-y)
            b=b+lr*(d[i]-y)
        print(w,b)



#single neutron

from math import*
import numpy as np
def linear(x):
    return x
def threshold(x):
    if x>0:
        return 1
    else:
        return 0
def ramp(x):
    if x>1:
        return 1
    elif x<0:
        return 0
    else:
        return x
def logsig(x):
    return (1/(1+exp(-x)))

x=np.array([1,0,1,0])
w=np.array([0,0,1,1])
b=0
net=np.sum(x*w)

ch=int(input("Enter neuron 1. linear,2. threshold,3. ramp,4. logsigmoid"))
y=0
if ch==1:
    y=linear(net+b)
elif ch==2:
    y=threshold(net+b)
elif ch==3:
    y=ramp(net+b)
elif ch==4:
    y=logsig(net+b)
else:
    print("Invalid choice of neuron")
print("out put for linear neuron",y)



#maculloch
from math import*
import numpy as np

def threshold(x):
    if x>0:
        return 1
    else:
        return 0

x=np.array([1,0,1,0])
w=np.array([0,0,1,1])
b=0
net=np.sum(x*w)
y=threshold(net+b)

print(y)
