import keras


def init_model():
    model = Sequential()
    model.add(Dense(units=64, activation="relu",))
    model.add(Dropout())
    model.add(Dense(units=64, activation="relu",))
    return model
