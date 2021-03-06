from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Flatten
from tensorflow.keras.models import Dense
from tensorflow.keras.models import Conv2D

def init_model():
    model = Sequential()
    model.add(Conv2D(input_shape=[28, 28, 1],filters=64,kernel_size=[3, 3],padding="same",activation="relu",)
    model.add(Flatten())
    model.add(Dense(units=64,activation="relu",)
    model.add(Dense(units=32,activation="relu",)
    model.add(Dense(units=10,activation="softmax",)
    return model