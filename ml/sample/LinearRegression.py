#import libraries
import numpy as np
import pandas as pd

#import dataset
dataset = pd.read_csv("QR3.csv")
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values

#encode data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
X[:, 4] = labelencoder.fit_transform(X[:, 4])
X[:, 5] = labelencoder.fit_transform(X[:, 5])
X[:, 6] = labelencoder.fit_transform(X[:, 6])
X[:, 7] = labelencoder.fit_transform(X[:, 7])
onehotencoder = OneHotEncoder(categorical_features = [3,4,5,6,7])
X = onehotencoder.fit_transform(X).toarray()

#Avoid dummy variable
X = X[:,[2,4,7,9,10,11,12,13,14,15,16,17,18,19,20]]

#optimal model; backward elimination
X = np.append(np.ones((147,1)).astype(int), values = X, axis = 1)
X_opt = X[:, [1,5,6,7,9,15]]


##splitting data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_opt, y, test_size = .3, random_state = 0)

#Fit model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

def maturityLevel(userData):
    #predict
    y_pred = regressor.predict(userData)
    return y_pred
