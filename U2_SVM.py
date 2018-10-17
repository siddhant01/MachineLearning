'''
    sklearn is a Python module integrating classical machine
    learning algorithms in the tightly-knit world of scientific Python
    packages (numpy, scipy, matplotlib).

    It aims to provide simple and efficient solutions to learning problems
    that are accessible to everybody and reusable in various contexts:
    machine-learning as a versatile tool for science and engineering.


    `sklearn.datasets` module includes utilities to load datasets,
    including methods to load and fetch popular reference datasets.

    The iris dataset is a classic and very easy multi-class classification
    dataset.
    =================   ==============
    Classes                          3
    Samples per class               50
    Samples total                  150
    Dimensionality                   4
    Features            real, positive
    =================   ==============

    `sklearn.cross_validation` module includes utilities for cross-
    validation and performance evaluation.

    train_test_split(*arrays, **options)
    Split arrays or matrices into random train and test subsets    
    Parameters
    ----------
    *arrays : sequence of indexables with same length / shape[0]
        Allowed inputs are lists, numpy arrays, scipy-sparse
        matrices or pandas dataframes.
    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.
    test_size : float, int, or None (default is None)
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the test split. If
        int, represents the absolute number of test samples. If None,
        the value is automatically set to the complement of the train size.
        If train size is also None, test size is set to 0.25.

   `sklearn.svm` module includes Support Vector Machine algorithms.

   'sklearn.svm.SVC' is a class which implements the SVM

   `sklearn.metrics` module includes score functions, performance metrics
    and pairwise metrics and distance computations.


    from sklearn import datasets
    from sklearn.cross_validation import train_test_split
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score
'''




from sklearn import datasets  #sklearn where data sets are present
iris=datasets.load_iris()
#print(iris)
X=iris.data[:,[2,3]] #it return a np.array type and we slice to 2nd and 3rd columns
#print(X)
y=iris.target  #target is the class
#print(y)

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

from sklearn.svm import SVC
svm = SVC(kernel='linear', C=1, random_state=0)
svm.fit(X_train, y_train)   #training the model
y_pred=svm.predict(X_test)
print("misclassified samples:",(y_test!=y_pred).sum())#compute
from sklearn.metrics import accuracy_score
print('Accuracy:%.2f'%accuracy_score(y_test,y_pred))





'''
#for more then 2 feature sets
from sklearn import datasets #sklearn where data sets are prsent
import numpy as np
iris=datasets.load_iris()
print(iris)
X=iris.data[:,(0,3)]
print(X)
Y=iris.target   #target is the class
print(Y)

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split( X,Y,test_size=0.3,random_state=0)

from sklearn.svm import SVC
svm=SVC(kernel='linear',C=1,random_state=0)
svm.fit(X_train,Y_train)  #taining the model
Y_pred=svm.predict(X_test)
print('misclassified samples: %d'%(Y_test != Y_pred).sum()) #compute 
from sklearn.metrics import accuracy_score
print ('Accuracy:%.2f'%accuracy_score(Y_test,Y_pred))
'''
