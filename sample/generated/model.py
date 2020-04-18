import keras

model = Sequential()
model.add(Dense(units=64, activation="relu",))
model.add(Dropout())
model.add(Dense(units=64, activation="relu",))
