class TrainController:
    def __init__(self, model_json, model):
        self.model_json = model_json
        self.model = model

    def do_epoch(self):
        pass

    def get_vars(self):
        return ["epochs"]

    def do_train(self, X_train, y_train):
        pass
