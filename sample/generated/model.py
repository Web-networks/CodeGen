from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.layers.core import Dense


def init_model():
    model = Sequential()
    model.add(Dense(units=64, activation="relu",))
    model.add(Dropout())
    model.add(Dense(units=64, activation="relu",))
    return model
