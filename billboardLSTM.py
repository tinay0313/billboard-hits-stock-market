import pandas as pd
import re 
from datetime import datetime, timedelta, date
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.regularizers import L1L2
from keras.utils.np_utils import to_categorical
from numpy import array
import numpy as np

from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.model_selection import train_test_split

dfX = pd.read_csv("billboard_input1.csv")

dfY = pd.read_csv("yLabel.csv")

dfX = dfX.drop(['Name', 'Week'],axis =1)

dfX = dfX.drop(dfX.index[-1])
dfX = dfX.drop(dfX.index[-1])
dfX = dfX.drop(dfX.index[-1])


dfY= dfY.drop(['Week'], axis = 1)
dfY = dfY.drop(dfY.index[-1])
dfY = dfY.drop(dfY.index[-1])
dfY = dfY.drop(dfY.index[-1])

dfXArr = dfX.to_numpy()
dfYArr = dfY.to_numpy()

ts_data = []
regl1_data = []
regl2_data = []
dropout_data = []
neurons_data = []
loss_data = []
acc_data = []

x_train, x_test, y_train, y_test = train_test_split(dfXArr, dfYArr, test_size = 0.3, random_state = 123, shuffle = False)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

n_timesteps = [4,6,8,10,12]

for ts in n_timesteps:
    train_generator = TimeseriesGenerator(x_train, y_train, length = ts, sampling_rate = 1, batch_size = 32 )
    test_generator = TimeseriesGenerator(x_test, y_test, length = ts, sampling_rate = 1, batch_size = 32 )

    n_features = 15
    n_outputs = 2
        
    dropout = [0.0,0.2,0.4,0.6]

    for dp in dropout: 
        model = Sequential()
        model.add(LSTM(128, return_sequences=True,input_shape=(ts,n_features)) )
        model.add(Dropout(dp))

        model.add(LSTM(128, return_sequences=True))
        model.add(Dropout(dp))

        model.add(LSTM(128))
        model.add(Dropout(dp))

        neurons = [30,50,80,100,120]

        for nr in neurons:
            model.add(Dense(nr, activation='relu'))
            model.add(Dense(n_outputs, activation='sigmoid'))
            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

            # fit network
            model.fit(train_generator, epochs=10, shuffle = False, verbose=0)

            # evaluate model
            accuracy = model.evaluate(test_generator, verbose=0)

            ts_data.append(ts)
            dropout_data.append(dp)
            neurons_data.append(nr)
            loss_data.append('{:.4f}'.format(accuracy[0]))
            acc_data.append('{:.4f}'.format(accuracy[1]))

        #print("n_timesteps= %d: %s=%.4f, %s=%.4f" % (ts, model.metrics_names[0], accuracy[0],model.metrics_names[1], accuracy[1]))
    
    
    #print("\n")

df = pd.DataFrame(list(zip(ts_data,dropout_data,neurons_data,loss_data,acc_data)),columns =['time step','dropout', 'neurons','loss','accuracy'])
#print(df.to_latex(index=False))
print(df)
print(df[df['accuracy'] == df['accuracy'].max()])