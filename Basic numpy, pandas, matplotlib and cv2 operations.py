#wap to check if a string is pallindrom or not
def pal():
    string=input()
    if string == string[::-1]:
        return True

#use a lot of help()

#import numpy operations
import numpy as np
a=np.array([[1,2,3,4,5],[2,4,6,8,9]])  #note numpy array has no comma in output
print(a)         #print matrix
print(a.T)       #print Transpose of matrix
print(a.shape)   #(2,3)           use this r,c=a.shape
print(a[0].shape)#(5,)
print(a.shape[0])#2    note shape returns a tuppen (r,c) so 0 is for r and c is for column
print(a.shape[1])#5
print(a.size)    #10
print(a.dtype)   #int32  other different np data types are float, int 16
print(type(a))          #numpy.ndarray


print(a[0][1]) #1st row and 2nd col
#a[rows and to use range use ':' or direct limit [,]   ,   columns and to use range use use ':' or direct limit [,]
print(a[0,1])  #only for numpy array not for python list
print(a[1,:]) #2nd row all col
print(a[:,3]) #all row 4th col
print(a[0:1,3])
print(a[1,1:3])
print(a[:,[2,3]])#print only the 2nd& 3rd columns


print(a.sum()) #print sum of all elements
print(a.sum(axis=0)) #print sum of elements column wise (r=0 so ans will be row so we need to add column wise)
print(a.sum(axis=1)) #print sum of elements row wise (c=1 so ans will be a column so we need to add row wise)
print(np.exp(a))    #print exponential of each element  e^x
print(np.exp(a[0,0]))
print(np.sqrt(a))
print(np.square(a))
print(np.transpose(a))

c=np.zeros((3,5)) #by default data type is float
print(c)
d=np.ones((3,4),dtype=np.int16)
print(d)
e=np.eye(4,4)  #or np.eye(4)
print(e)

f=np.arange(10,20,2)  #same as list(range(10,20,2) but note arange can have float skip values where as range have only int skip values
print(f)
g=np.arange(12).reshape(4,3)  #arranges 1D list 0-11 to 2D matrix, but the original matrix remains unchanged
print(g)
h=np.arange(0,24,1).reshape(2,3,4) #arranges 1d list 0-24 to 2 3d matrix of 2*3*4   n*r*c
print(h)   #[[[ 0  1  2  3][ 4  5  6  7][ 8  9 10 11]][[12 13 14 15][16 17 18 19][20 21 22 23]]]

i=np.linspace(10,20,5) #to make 1d array of 10 to 20 (not like arange) have 5 values with equal diff
print(i)               #note arange is like range and linspace is like full end to end included range,but instread of step size we have no. of elements required 

j=np.array([20,30,40,50])
h=np.arange(4)
print("a-b=",j-h)  # note how we can make matrix operation in numpy very easily without dealing with individual elements
print("a+b=",j+h)

a=np.array([[1,2],[3,4]])
b=np.array([[0,1],[1,1]])
print(a*b) #direct multiplication of elements in order
print(a.dot(b)) #matrix multiplication
print(np.dot(a,b)) #other format of matrix multiplication


a = np.random.random()  #it just assigns a random value
print(a)
a=np.random.random((2,3)) #random matrix is created of 2*3
print(a)
b=np.random.randint(low =0,high=5,size=5) #gives a random list of size 5  or np.random.randint(0,5,5)
print(b)
b=np.random.randint(0,5,(2,2)) #it gives a 2d matrix of 2*2
print(b)
#it is wrong
##b=np.random.randint((2,2))  np.random.randint requires limit also
##print(b)

k=np.array([[1,3],[2,4],[3,5],[4,8]])
print(k)
k1=k.reshape(2,4) #[[1 3 2 4][3 5 4 8]], but original remains unchanged unlike resize()
print(k1)
k1=k.transpose()  #[[1 2 3 4][3 4 5 8]] note the difference with reshape
print(k1)

# shape manupulation
b=np.array([[1,2, 3],[4,5,6],[7,8,9],[10,11,12]])
b.reshape(4,3) # converted to 4 x 3 using row wise but orignal matrix unchnaged
b.resize(4,3) #converted to 4 x 3 using row wise but orignal matrix chnaged



#wap to display the bmi of a person using height and weight using numpy operations, also find corelation b/w weight and height
'''
bmi=w/(height*height)
'''
height=np.array([2,1.5,1.3,1.4])
weight=np.array([55,60,50,52])

bmi=weight/(height*height)
print(bmi)
light=bmi<21 # logical array where bmi<21  [True False False False]
print(light)
print(bmi[light]) #note np array[logica array] = [elements for logcial array being True]


a=np.random.randint(2,10,6)
b=np.random.randint(2,10,6)
print(a,b)
print(np.mean(a))
print(np.median(a))
print(np.corrcoef(a,b)) # correlation of two vectors a and b
print(np.std(a))
print(np.sum(a))
print(np.sort(a))  #here a sorted value of a is returned but a remains unchanged
a.sort() #note here a value change and nothing is returned
print(np.round(2.345)) #2.0 
print(np.round(2.345,2)) #2.35
a=np.random.normal(1.75,0.2,10)  # np.random.normal(mean,stdv,number of sample). Draw random samples from a normal (Gaussian) distribution
h=np.round(np.random.normal(1.75,0.2,5000),2) # we are rounding all the elements of the array
np_city=np.column_stack(([234,324],[34,342])) # another type of np.array stacking
wh=np.random.uniform(size=(3,5)) #Draw samples from a uniform distribution (note always use size=  else default parameter is very different)


#pandas
import pandas as pd   #for reading csv here
ds1=pd.read_csv('C:\\Users\\Siddhant Saurabh\\Desktop\\Churn_Modelling.csv')  #always give full path
#dsl=pd.read_csv('Churn_Modelling.csv')
print(ds1.tail()) #print last 5 of the csv file
print(ds1.head()) #print 1st 5


from matplotlib import pyplot as plt  #or import matplotlib.pyplot as plt    for ploting pupose

#plt.figure(1) creates a new figure
plt.figure(1) #note for ploting the data should be enclose b/w figure(1) show()
plt.subplot(2,2,4)  # here we divided our graph into 4 parts and the below data is for 4th part  or we can write subplot(224) also
plt.plot([1,2,3,4],[12,14,15,16])
plt.subplot(2,2,3)
plt.plot([1,2,3,4],[10,0,20,30])
plt.subplot(2,2,1)
plt.plot([1,2,3,4],[10,0,20,30])
plt.show()

#note plt.plot([1,4,2,5])  is equal to plt.plot([1,4,2,5],[1,2,3,4]) x axis is created automatically

plt.figure(2) #creates another figure for same program
plt.plot([1,2,3,4],[1,4,9,6],'yo--') #'yo--' means yellow color and line should be default
plt.xlabel('x')
plt.ylabel('y',fontsize=10,color='red')
plt.title('Graph2')
#for printing a text at a specific coordinate
plt.text(2,2,'Hello',fontsize=10,color='green') #note fontsize and color can be left out as they have default values
plt.axis([0,6,0,20]) # for specifying the range of x(0-6) and y(0-20)
plt.grid(True)   #for allowing grid to be shown

import numpy as np
t=np.arange(0,5,0.2)
plt.plot(t,t,'r--',     t,t**2,'bs'   ,t,t**3,'g^') #note here are 3 values to be plotted  also note bs is blue square
plt.show()                                          #more symbol is 'ro' red dot

x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,label='line')   #shows at top color and label of this line
x2=[1,2,3]
y2=[4,1,3]
plt.plot(x2,y2,label='line2')
plt.legend(loc='upper center',shadow='True')   #note you need to use legend with labels else they will not be shown
plt.show()

#another way of plotting using scatter
plt.scatter([1,2,9,4], [2,3,4,5],s=20,c='green',alpha=0.8) #plt.scatter(gdp_cap, life_exp,s=size,c=color,alpha=0.8) #opacity



#plt.xscale('log') # Put the x-axis on a logarithmic scale check help

# histogram
plt.hist([2,3,4,5],(1,1,1,1))  # used for showing distrubution on histogram
plt.clf() # clear the plot drawn on screen.


####Customization
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']
# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)  #shows  1k instead of 1000 in x axis, 10k instead of 10000 and so on  


#need to install (pip install opencv-python)
##import cv2     #for reading images
##print(cv2.__version__)
###load clor image form csv
##img=cv2.imread('C:\\Users\\Siddhant Saurabh\\Desktop\\2.jpg',-10)
##cv2.imshow(img) #for new window or use plt.imshow(img) for same terminal output
