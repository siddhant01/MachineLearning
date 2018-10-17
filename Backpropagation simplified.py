"""
      H
I     
            0            check the copy example
I
      H
"""

import numpy as np

X=np.array([[0.35,0.9]])  #note [0,35,0.9] dimention is (2,) not (1,2) so while matrix multiplication use 2d matrix only
y=np.array([0.5])
wh = np.array([[0.1,0.4],[0.8,0.6]])
wout = np.array( [[0.3,0.9]] )
e = 1                                                                
lr = 1  

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)
                                 
inputlayer_neurons = 2                                                 
hiddenlayer_neurons = 2                                               
output_neurons = 1

bh = np.array( [[0.0,0.0]] ) 
bout = np.array( [[0.0]] )   

for i in range(e):
    #Forward Propogation
    hidden_layer_input = np.dot( X , wh ) + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)
    output_layer_input= np.dot( hiddenlayer_activations , wout.T) + bout
    output = sigmoid(output_layer_input)   
    #Backpropagation
    E = y-output                  
    d_output = E * derivatives_sigmoid(output)  
    
    wout += lr * np.dot(d_output , hiddenlayer_activations)  
    bout += lr * d_output  
    
    d_hiddenlayer = derivatives_sigmoid(hiddenlayer_activations) * d_output * wout 
    wh += lr * np.dot(X.T , d_hiddenlayer)      
    bh += lr * d_hiddenlayer      

print (output)
print(E)
