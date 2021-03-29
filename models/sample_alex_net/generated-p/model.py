from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dropout

def init_model():
    model = Sequential()
    model.add(Conv2D(input_shape=[32, 32, 3],filters=96,kernel_size=[11, 11],padding="same",strides=[4, 4],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(MaxPooling2D(pool_size=[2, 2],strides=[2, 2],padding="same",))
    model.add(Conv2D(filters=256,kernel_size=[5, 5],padding="same",strides=[1, 1],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(MaxPooling2D(pool_size=[2, 2],strides=[2, 2],padding="same",))
    model.add(Conv2D(filters=384,kernel_size=[3, 3],padding="same",strides=[1, 1],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(Conv2D(filters=384,kernel_size=[3, 3],padding="same",strides=[1, 1],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(Conv2D(filters=256,kernel_size=[3, 3],padding="same",strides=[1, 1],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(MaxPooling2D(pool_size=[2, 2],strides=[2, 2],padding="same",))
    model.add(Flatten())
    model.add(Dense(units=4096,input_shape=[32, 32, 3],))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(Dropout(rate=0.4,))
    model.add(Dense(units=4096,))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(Dropout(rate=0.4,))
    model.add(Dense(units=1000,))
    model.add(BatchNormalization())
    model.add(Activation(activation="relu",))
    model.add(Dropout(rate=0.4,))
    model.add(Dense(units=10,))
    model.add(BatchNormalization())
    model.add(Activation(activation="softmax",))
    return model