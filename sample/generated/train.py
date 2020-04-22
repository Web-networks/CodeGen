from model import init_model


class TrainController:
    def __init__(self, model_json, model):
        self.model_json = model_json
        self.model = init_model()

    def do_epoch(self):
        pass

    def get_vars(self):
        return ["epochs"]

    def do_compile(self):
        self.model.compile(
            loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]
        )

    def do_train(self, X_train, y_train, X_test, y_test):
        result_train = self.model.fit(
            X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=32
        )
        return result_train
