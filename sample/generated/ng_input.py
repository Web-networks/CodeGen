class NeurogenIO:
    def __init__(self, ng_bus):
        self.ng_bus = ng_bus

    # Returns list of CLI vars
    def get_vars(self):
        return ["train_test_ratio"]

    def read_inputs(self):
        if self.ng_bus.mode == "inference":
            # TODO
            pass
        elif self.ng_bus.mode == "train":
            from keras.datasets import mnist

            (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()
        else:
            raise Exception("invalid mode: " + self.ng_bus.mode)

    def get_train_xy(self):
        return self.X_train, self.y_train

    def get_test_xy(self):
        return self.X_test, self.y_test
