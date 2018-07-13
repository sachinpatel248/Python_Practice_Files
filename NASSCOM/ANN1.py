'''
Data Preperaton '''
import pandas as pd,numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam,SGD
import matplotlib.pyplot as plt,seaborn as sns
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.callbacks import ReduceLROnPlateau


#------------------------------------------------

batch_Size = 20
epochs = 100
lr_rate = 0.001
reduceLR = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=3, 
                             verbose=0, mode='auto', epsilon=1e-4, cooldown=0, min_lr=1e-5)

optim = Adam(lr=lr_rate,decay=1e-5)

#------------------------------------------------
def getModel():
    model = Sequential()
    model.add(Dense(32,activation='relu',kernel_initializer='uniform',input_shape = [11] ))
    model.add(Dense(32,activation='relu',kernel_initializer='uniform' ))
    model.add(Dense(32,activation='relu',kernel_initializer='uniform' ))
    model.add(Dense(32,activation='relu',kernel_initializer='uniform' ))
    model.add(Dense(1,activation='sigmoid'))
    
    print(model.summary())    
    return model

#------------------------------------------------
model = getModel()
model.compile(optimizer=optim,loss='binary_crossentropy',metrics = ['accuracy'])

#------------------------------------------------
#Data pre processing
df = pd.read_csv('Churn_Modelling.csv')

#removing unwanted variables
X = df.drop(['RowNumber','CustomerId','Surname','Exited'],axis=True)

#use Lable encoding for encodig categorical vaiable

label_country = LabelEncoder()
X['Geography'] = label_country.fit_transform(X['Geography'])

label_gender = LabelEncoder()
X['Gender'] = label_gender.fit_transform(X['Gender'])

#creating Dumies for geographic location
X = pd.get_dummies(X, prefix='_', columns=['Geography'])
#removing unwanted dumy column
X.drop ('__2',axis = 1,inplace =True)

scalar = StandardScaler()
X = pd.DataFrame(scalar.fit_transform(X),columns=X.columns)

#------ Train test split
X_train, X_test, y_train, y_test = train_test_split(X, df['Exited'], test_size=0.15, random_state=42)

X_train, X_cv, y_train, y_cv = train_test_split(X_train, y_train, test_size=0.1, random_state=42)


#------------------------------TRaining a Model



hist = model.fit(X_train,y_train,batch_size= batch_Size,epochs=epochs,callbacks=[reduceLR],
          validation_data=(X_cv,y_cv),
          #steps_per_epoch=X_train.shape[1]//batch_Size,
          validation_steps=X_cv.shape[1]//batch_Size)

plt.plot(hist.epoch,hist.history['loss'],label='Training Loss')
plt.plot(hist.epoch,hist.history['val_loss'],'r',label='validation_loss')
plt.legend()
plt.show()

plt.plot(hist.epoch,hist.history['acc'],label='Training Acc')
plt.plot(hist.epoch,hist.history['val_acc'],'r',label='validation_Acc')
plt.legend()
plt.show()
#----------------------------------------------------------

#data analysis 
df.columns

['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
       'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary', 'Exited'],
      dtype='object')

def boxPlot(x,y='Exited',hue= 'Exited',ht=8,wd=6):
        
    sns.set_style('darkgrid' )
    plt.figure(figsize=(ht,wd))
    sns.boxplot(x = x,y = y,data=df,hue=hue)
    plt.show()


boxPlot('Exited','Balance','Exited',10,8)


























