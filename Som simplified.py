import numpy as np
x = np.array([[ 1, 1, 0, 0],[0, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1]])
w =np.array([[0.2 ,0.8], [0.6, 0.4], [0.5, 0.7], [0.9, 0.3]])
lrate= 0.6
e=3
xr,xc=x.shape
wr,wc=w.shape
D=[0]*wc
print('learning rate of this epoch is',lrate);

for r in range(e):

    for i in range(xr):
        for j in range(wc):
            D[j]=np.sum(np.square(x[i,:]-w[:,j]))

        J=D.index(min(D))
        print(D,J)
            
        print('winning unit is',J+1)
        print('weight updation ...')

        w[:,J]=w[:,J]+ (lrate*(x[i,:]-w[:,J]))

        print('Updated weights',w)

    lrate = 0.5*lrate;
    print(' updated learning rate after ',e,' epoch is',lrate)


