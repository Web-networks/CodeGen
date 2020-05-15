from keras.models import Sequential
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import MaxPool2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import MaxPool2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import MaxPool2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import MaxPool2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import Conv2D
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers.core import Dense
from keras.layers.core import Dense


def init_model():
    model = Sequential()
    model.add(
        Conv2D(
            input_shape=[28, 28, 1],
            filters=64,
            kernel_size=[3, 3],
            padding="same",
            activation="relu",
        )
    )
    model.add(
        Conv2D(filters=64, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(MaxPool2D(pool_size=[2, 2], strides=[2, 2],))
    model.add(
        Conv2D(filters=128, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=128, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(MaxPool2D(pool_size=[2, 2], strides=[2, 2],))
    model.add(
        Conv2D(filters=256, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=256, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=256, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(MaxPool2D(pool_size=[2, 2], strides=[2, 2],))
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(MaxPool2D(pool_size=[2, 2], strides=[2, 2],))
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(
        Conv2D(filters=512, kernel_size=[3, 3], padding="same", activation="relu",)
    )
    model.add(Flatten())
    model.add(Dense(units=4096, activation="relu",))
    model.add(Dense(units=4096, activation="relu",))
    model.add(Dense(units=1, activation="softmax",))
    return model
