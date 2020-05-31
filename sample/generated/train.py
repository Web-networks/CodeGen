from model import init_model
from keras.callbacks import ModelCheckpoint
import os


class TrainController:
    def __init__(self):
        self.model = init_model()

    def do_epoch(self):
        pass

    def get_vars(self):
        return ["epochs"]

    def do_compile(self):
        self.model.compile(
            loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]
        )

    def do_train(self, X_train, y_train, X_test, y_test, weights_filename):
        if not os.path.exists("weights"):
            os.makedirs("weights")

        weights_file = "weights/" + weights_filename + ".h5"
        callback = ModelCheckpoint(
            weights_file, monitor="acc", mode="max", save_best_only=True
        )
        result_train = self.model.fit(
            X_train,
            y_train,
            validation_data=(X_test, y_test),
            epochs=5,
            batch_size=32,
            callbacks=[callback],
        )
        return result_train
