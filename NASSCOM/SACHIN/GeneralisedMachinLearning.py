#Generalised model for machine learning Preditcion based system

#prelimnary imports

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

#Data Prepration and Exploratory analysis:

#Do it as per need


#model building
''' Assuming you have all the features avalable in data frame
df....'''

CSV_File_Path = r'ABC.csv'
dataframe = pd.read_csv(CSV_File_Path)

print (dataframe)


X = df.drop('target column', axis = 1)
y = df['']

#step 1. Feature scaling : using Std Scaler you can then use min max scalaerif required.
scalar = StandardScaler()
#fitting the Df 
X = scalar.fit_transform(X)

#note  the scalar model will be required to transform test set which will be new to our training model so save it and use transform method to scale test data 

#traing and validation set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Can be used but i will use whole traing data set for cross validfation
#X_cv, X_test, y_cv, y_test = train_test_split(X_train, y_train, test_size=0.15, random_state=42)

'''Using hyper parameter tuning we fill fit the modle and evaluate at the same time'''

#launching Models
LR = LinearRegression()
Rf = RandomForestRegressor()




###Creating a dict for hyper paramerter
##rfParams = {
##        'n_estimators' : [10,20,50,100,75,200,500],
##        'n_jobs' = [-1]
##        
##        
##        }
##
##LRParams = {
##        'n_jobs' = [-1]
##        
##        
##        }
##
## skf = StratifiedKFold(n_splits=5,random_state=99,shuffle=True)
##
##
###change Estimator after each run to evaluate best result
##randCV = RandomizedSearchCV(estimator=LR,param_distributions=LRParams,scoring='accuracy',n_iter=10,
##                            cv = skf.split(X_train,y_train))
##
##randCv.fit(X_train,y_train)
##
###this will Train the model.
##
###now we will evauate on test data
##
##predict = randCV.predict(X_test)
##
##
##
###printing the RMS error : lower the rror good wil be the result
##print(np.sqrt(mean_squared_error(predict,y_test)))
##
##
##'''
##Now if the new data is given then do not use predict method on new valiblae data instead first convert it into a single array and then scale the data using the m scaler model createrd abaove
##then use randCv .predict method on newly scaled data and get the result.
##
##if u wqant u c an switch the estimator to RandomforestRegressor for ebvaluation
##
##'''
##
##
##



  






