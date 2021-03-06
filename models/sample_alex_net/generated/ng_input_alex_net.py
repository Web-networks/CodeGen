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
            from keras.datasets import cifar10

            (self.X_train, self.y_train), (
                self.X_test,
                self.y_test,
            ) = cifar10.load_data()
            from sklearn.model_selection import train_test_split

            self.X_train, self.x_val, self.y_train, self.y_val = train_test_split(
                self.X_train, self.y_train, test_size=0.3
            )
            from sklearn.utils.multiclass import unique_labels
            from keras.utils import to_categorical

            self.y_train = to_categorical(self.y_train)
            self.y_val = to_categorical(self.y_val)
            self.y_test = to_categorical(self.y_test)
        else:
            raise Exception("invalid mode: " + self.ng_bus.mode)

    def get_train_xy(self):

        return self.X_train, self.y_train

    def get_test_xy(self):

        return self.X_test, self.y_test
