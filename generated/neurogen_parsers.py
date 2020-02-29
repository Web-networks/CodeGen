class Id(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = obj


class Model(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Model()
        self.model_id = Id(obj["model_id"])
        self.user_id = Id(obj["user_id"])
        self.layers = []
        for item in obj["layers"]:
            parsed_item = Layer(item)
            self.layers.append(parsed_item)


class Layer(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Layer()
        self.type = obj["type"]
        self.params = obj["params"]


class Activation(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Activation()
        self.type = obj["type"]
        self.params = obj["params"]


class Initializer(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Initializer()
        self.type = obj["type"]
        self.params = obj["params"]


class Constraint(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Constraint()
        self.type = obj["type"]
        self.params = obj["params"]


class Regularizer(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Regularizer()
        self.l1 = obj["l1"]
        self.l2 = obj["l2"]


class DenseParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = DenseParams()
        self.units = obj["units"]
        self.activation = Activation(obj["activation"])
        self.use_bias = obj["use_bias"]
        self.kernel_initializer = Initializer(obj["kernel_initializer"])
        self.bias_initializer = Initializer(obj["bias_initializer"])
        self.kernel_regularizer = Regularizer(obj["kernel_regularizer"])
        self.bias_regularizer = Regularizer(obj["bias_regularizer"])
        self.activity_regularizer = Regularizer(obj["activity_regularizer"])
        self.kernel_constraint = Constraint(obj["kernel_constraint"])
        self.bias_constraint = Constraint(obj["bias_constraint"])


class ActivationParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = ActivationParams()
        self.activation = Activation(obj["activation"])


class DropoutParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = DropoutParams()
        self.rate = obj["rate"]
        self.noise_shape = obj["noise_shape"]
        self.seed = obj["seed"]


class Conv1DParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Conv1DParams()
        self.filters = obj["filters"]
        self.kernel_size = obj["kernel_size"]
        self.strides = obj["strides"]
        self.padding = obj["padding"]
        self.data_format = obj["data_format"]
        self.dilation_rate = obj["dilation_rate"]
        self.activation = Activation(obj["activation"])
        self.use_bias = obj["use_bias"]
        self.kernel_initializer = Initializer(obj["kernel_initializer"])
        self.bias_initializer = Initializer(obj["bias_initializer"])
        self.kernel_regularizer = Regularizer(obj["kernel_regularizer"])
        self.bias_regularizer = Regularizer(obj["bias_regularizer"])
        self.activity_regularizer = Regularizer(obj["activity_regularizer"])
        self.kernel_constraint = Constraint(obj["kernel_constraint"])
        self.bias_constraint = Constraint(obj["bias_constraint"])


class Conv2DParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Conv2DParams()
        self.filters = obj["filters"]
        self.kernel_size = obj["kernel_size"]
        self.strides = []
        for item in obj["strides"]:
            parsed_item = item
            self.strides.append(parsed_item)

        self.padding = obj["padding"]
        self.data_format = obj["data_format"]
        self.dilation_rate = []
        for item in obj["dilation_rate"]:
            parsed_item = item
            self.dilation_rate.append(parsed_item)

        self.activation = Activation(obj["activation"])
        self.use_bias = obj["use_bias"]
        self.kernel_initializer = Initializer(obj["kernel_initializer"])
        self.bias_initializer = Initializer(obj["bias_initializer"])
        self.kernel_regularizer = Regularizer(obj["kernel_regularizer"])
        self.bias_regularizer = Regularizer(obj["bias_regularizer"])
        self.activity_regulizer = Regularizer(obj["activity_regulizer"])
        self.kernel_constraint = Constraint(obj["kernel_constraint"])
        self.bias_constraint = Constraint(obj["bias_constraint"])


class Pooling1DParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Pooling1DParams()
        self.pool_size = obj["pool_size"]
        self.strides = obj["strides"]
        self.padding = obj["padding"]
        self.data_format = obj["data_format"]


class Pooling2DParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = Pooling2DParams()
        self.pool_size = []
        for item in obj["pool_size"]:
            parsed_item = item
            self.pool_size.append(parsed_item)

        self.strides = []
        for item in obj["strides"]:
            parsed_item = item
            self.strides.append(parsed_item)

        self.padding = obj["padding"]
        self.data_format = obj["data_format"]


class SimpleRNNParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = SimpleRNNParams()
        self.units = obj["units"]
        self.activation = Activation(obj["activation"])
        self.use_bias = obj["use_bias"]
        self.kernel_initializer = Initializer(obj["kernel_initializer"])
        self.recurrent_initializer = Initializer(obj["recurrent_initializer"])
        self.bias_initializer = Initializer(obj["bias_initializer"])
        self.kernel_regularizer = Regularizer(obj["kernel_regularizer"])
        self.recurrent_regularizer = Regularizer(obj["recurrent_regularizer"])
        self.bias_regularizer = Regularizer(obj["bias_regularizer"])
        self.activity_regularizer = Regularizer(obj["activity_regularizer"])
        self.kernel_constraint = Constraint(obj["kernel_constraint"])
        self.recurrent_constraint = Constraint(obj["recurrent_constraint"])
        self.bias_constraint = Constraint(obj["bias_constraint"])
        self.dropout = obj["dropout"]
        self.recurrent_dropout = obj["recurrent_dropout"]
        self.return_sequences = obj["return_sequences"]
        self.return_state = obj["return_state"]
        self.go_backwards = obj["go_backwards"]
        self.stateful = obj["stateful"]
        self.unroll = obj["unroll"]


class LSTMParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = LSTMParams()
        self.units = obj["units"]
        self.activation = Activation(obj["activation"])
        self.recurrent_activation = Activation(obj["recurrent_activation"])
        self.use_bias = obj["use_bias"]
        self.kernel_initializer = Initializer(obj["kernel_initializer"])
        self.recurrent_initializer = Initializer(obj["recurrent_initializer"])
        self.bias_initializer = Initializer(obj["bias_initializer"])
        self.unit_forget_bias = obj["unit_forget_bias"]
        self.kernel_regularizer = Regularizer(obj["kernel_regularizer"])
        self.recurrent_regularizer = Regularizer(obj["recurrent_regularizer"])
        self.bias_regularizer = Regularizer(obj["bias_regularizer"])
        self.activity_regularizer = Regularizer(obj["activity_regularizer"])
        self.kernel_constraint = Constraint(obj["kernel_constraint"])
        self.recurrent_constraint = Constraint(obj["recurrent_constraint"])
        self.bias_constraint = Constraint(obj["bias_constraint"])
        self.dropout = obj["dropout"]
        self.recurrent_dropout = obj["recurrent_dropout"]
        self.implementation = obj["implementation"]
        self.return_sequences = obj["return_sequences"]
        self.return_state = obj["return_state"]
        self.go_backwards = obj["go_backwards"]
        self.stateful = obj["stateful"]
        self.unroll = obj["unroll"]


class EmbeddingParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = EmbeddingParams()
        self.input_dim = obj["input_dim"]
        self.output_dim = obj["output_dim"]
        self.embeddings_initializer = Initializer(obj["embeddings_initializer"])
        self.embeddings_regularizer = Regularizer(obj["embeddings_regularizer"])
        self.activity_regularizer = Regularizer(obj["activity_regularizer"])
        self.embeddings_constraint = Constraint(obj["embeddings_constraint"])
        self.mask_zero = obj["mask_zero"]
        self.input_length = obj["input_length"]


class BatchNormalizationParams(neurogen.GeneratedClassBase):
    def __init__(self, obj):
        self = BatchNormalizationParams()
        self.axis = obj["axis"]
        self.momentum = obj["momentum"]
        self.epsilion = obj["epsilion"]
        self.center = obj["center"]
        self.scale = obj["scale"]
        self.beta_initializer = Initializer(obj["beta_initializer"])
        self.gamma_initializer = Initializer(obj["gamma_initializer"])
        self.moving_mean_initializer = Initializer(obj["moving_mean_initializer"])
        self.moving_variance_initializer = Initializer(
            obj["moving_variance_initializer"]
        )
        self.beta_regularizer = Regularizer(obj["beta_regularizer"])
        self.gamma_regularizer = Regularizer(obj["gamma_regularizer"])
        self.beta_constraint = Constraint(obj["beta_constraint"])
        self.gamma_constraint = Constraint(obj["gamma_constraint"])
