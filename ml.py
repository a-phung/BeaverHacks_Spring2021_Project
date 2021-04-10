import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.kerasmodels import sequential
from tensorflow.keras.layers Dense, Dropout, LSTM

#load data
company = 'TSLA'
start = dt.datetime(2012,1,1)
end = dt.datetune(2020,1,1)

data = web.DataReader(company, 'yahoo', start, end)

#prepare data
scaler = MinMaxScaler(feature_range = (0,1))
scaled_data = scaler.fit_transform(data['close'].values.reshape(-1,1))
#try adjusted close?

prediction_days = 20

x_train = []
y_train = []

for x in range(prediction_days, len(scaled_data))
    x_train.append(scaled_data[x-prediction_days:x,0])
    y_train.append(scaled_data[x,0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1].1))

#build model (simple tree)
model = sequential()

model.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units = 50, return_sequences = True)
model.add(Dropout(0.2))
model.add(LSTM(units = 50))
model.add(Dropout(0.2))
model.add(Debse(units = 1)) #prediction of next closing day

model.compile(optimizer = 'adam', loss = 'mean_squared_error'

#fitting
model.fit(x_train, y_train, epochs = 25, batch_size = 32)

#model accuracy

test_start = dt.datetime(2020,1,1)
test_end = dt.datetime.now()

test_data = web.DataReader(company, 'yahoo', test_start
actual_prices = test_data['close].values

total_dataset = pd.concat((data['close'], test_data['close'], axis = 0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model.inputs = scaler.transform(model_inputs)

# make predicitons on test data
x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days;x,0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted-prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

#plotting
plt.plot(actual_prices, color = 'black', label= f"Actual {company) Price")
plt.plot(predicted_prices, color = 'red', label= f"Predicted {company) Price")
plt.title(f"{company} Share Price")
plt.xlabel('Time')
plt.ylabel(f'{company} Share Price')
plt.legend()
plt.show()


real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model(inputs+1), 0]]
real_data = np.array(real_data)
real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

prediction = model.preduct(real_data)
prediction = scalar.inverse_transform(prediction)
print('prediction for next day is {prediction}')

