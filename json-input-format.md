## Общая схема json.
Предлагается такая схема:
``` json
{
  "model_id": "1",
  "user_id": "1",
  "layers": [{
      "type": "Dense",
      "params": {
   "параметры для слоя"
   "конкретно будет расписано ниже"
      }
    },
    {
      "type": "Activation",
      "params": {
        
      }
    },
    {
      "type": "Dropout",
      "params": {
        
      }
    }
  ]
}
```
# 1. Core Layers

## 1. Dense (regular densely-connected NN layer)

**Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)**

where:
***units***: Positive integer, dimensionality of the output space.
***activation***: Activation function to use (see activations). If you don't specify anything, no activation is applied (ie. "linear" activation: a(x) = x).
***use_bias***: Boolean, whether the layer uses a bias vector.
***kernel_initializer***: Initializer for the kernel weights matrix (see initializers).
***bias_initializer***: Initializer for the bias vector (see initializers).
***kernel_regularizer***: Regularizer function applied to the kernel weights matrix (see regularizer).
***bias_regularizer***: Regularizer function applied to the bias vector (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***kernel_constraint***: Constraint function applied to the kernel weights matrix (see constraints).
***bias_constraint***: Constraint function applied to the bias vector (see constraints).
``` json
{
      "type": "Dense",
      "params": {
        "units": "integer",
        "activation": "activations",
        "use_bias": "boolean",
        "kernel_initializer": "initializers",
        "bias_initializer": "initializers",
        "kernel_regularizer": "regularizer",
        "bias_regularizer": "regularizer",
        "activity_regularizer": "regularizer",
        "kernel_constraint": "constraints",
        "bias_constraint": "contsraints"
      }
    }
```
## 2. Activation

**Activation(activation),**

where:
***activation***: name of activation function to use (see: activations), or alternatively, a Theano or TensorFlow operation.
``` json
    {
      "type": "Activation",
      "params": {
        "activation": "activations"
      }
    }
```
## 3. Dropout

**Dropout(rate, noise_shape=None, seed=None),**
where:
***rate***: float between 0 and 1. Fraction of the input units to drop.
***noise_shape***: 1D integer tensor representing the shape of the binary dropout mask that will be multiplied with the input. For instance, if your inputs have shape (batch_size, timesteps, features) and you want the dropout mask to be the same for all timesteps, you can use noise_shape=(batch_size, 1, features).
***seed***: A Python integer to use as random seed.

``` json
     {
      "type": "Dropout",
      "params": {
        "rate": "float",
        "noise_shape": "integer",
        "seed": "integer"
      }
    }
 ```

# Convolutional Layers

## 1. Conv1D (1D convolution layer)
**keras.layers.Conv1D(filters, kernel_size, strides=1, padding='valid', data_format='channels_last', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)**

Arguments
***filters***: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
***kernel_size***: An integer or tuple/list of a single integer, specifying the length of the 1D convolution window.
***strides***: An integer or tuple/list of a single integer, specifying the stride length of the convolution. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.
***padding***: One of "valid", "causal" or "same" (case-insensitive). "valid" means "no padding". "same" results in padding the input such that the output has the same length as the original input. "causal" results in causal (dilated) convolutions, e.g. output[t] does not depend on input[t + 1:]. A zero padding is used such that the output has the same length as the original input. Useful when modeling temporal data where the model should not violate the temporal order. See WaveNet: A Generative Model for Raw Audio, section 2.1.
***data_format***: A string, one of "channels_last" (default) or "channels_first". The ordering of the dimensions in the inputs. "channels_last" corresponds to inputs with shape (batch, steps, channels) (default format for temporal data in Keras) while "channels_first" corresponds to inputs with shape (batch, channels, steps).
***dilation_rate***: an integer or tuple/list of a single integer, specifying the dilation rate to use for dilated convolution. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any strides value != 1.
***activation***: Activation function to use (see activations). If you don't specify anything, no activation is applied (ie. "linear" activation: a(x) = x).
***use_bias***: Boolean, whether the layer uses a bias vector.
***kernel_initializer***: Initializer for the kernel weights matrix (see initializers).
***bias_initializer***: Initializer for the bias vector (see initializers).
***kernel_regularizer***: Regularizer function applied to the kernel weights matrix (see regularizer).
***bias_regularizer***: Regularizer function applied to the bias vector (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***kernel_constraint***: Constraint function applied to the kernel matrix (see constraints).
***bias_constraint***: Constraint function applied to the bias vector (see constraints).
***Input shape***: 3D tensor with shape: (batch, steps, channels)
***Output shape***: 3D tensor with shape: (batch, new_steps, filters) steps value might have changed due to padding or strides.
https://missinglink.ai/guides/keras/keras-conv1d-working-1d-convolutional-neural-networks-keras/

``` json
    {
    "type": "Conv1D",
    "params": {
      "filters": "integer",
      "kernel_size": "integer",
      "strides": "integer",
      "padding": "integer",
      "data_format": "string",
      "dilation_rate": "integer",
      "activation": "activations",
      "use_bias": "boolean",
      "kernel_initializer": "initializer",
      "bias_initializer": "initializer",
      "kernel_regularizer": "regularizer",
      "bias_regularizer": "regularizer",
      "activity_regulizer": "regulizer",
      "kernel_constraint": "constraints",
      "bias_constraint": "constraints"
    }

  }
```
## 2. Conv2D (2D convolution layer)
**keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)**

Arguments
***filters***: Integer, the dimensionality of the output space (i.e. the number of output filters in the convolution).
***kernel_size***: An integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window. Can be a single integer to specify the same value for all spatial dimensions.
***strides***: An integer or tuple/list of 2 integers, specifying the strides of the convolution along the height and width. Can be a single integer to specify the same value for all spatial dimensions. Specifying any stride value != 1 is incompatible with specifying any dilation_rate value != 1.
***padding***: one of "valid" or "same" (case-insensitive). Note that "same" is slightly inconsistent across backends with strides != 1, as described here
***data_format***: A string, one of "channels_last" or "channels_first". The ordering of the dimensions in the inputs. "channels_last" corresponds to inputs with shape (batch, height, width, channels) while "channels_first" corresponds to inputs with shape (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".
***dilation_rate***: an integer or tuple/list of 2 integers, specifying the dilation rate to use for dilated convolution. Can be a single integer to specify the same value for all spatial dimensions. Currently, specifying any dilation_rate value != 1 is incompatible with specifying any stride value != 1.
***activation***: Activation function to use (see activations). If you don't specify anything, no activation is applied (ie. "linear" activation: a(x) = x).
use_bias: Boolean, whether the layer uses a bias vector.
***kernel_initializer***: Initializer for the kernel weights matrix (see initializers).
***bias_initializer***: Initializer for the bias vector (see initializers).
***kernel_regularizer***: Regularizer function applied to the kernel weights matrix (see regularizer).
***bias_regularizer***: Regularizer function applied to the bias vector (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***kernel_constraint***: Constraint function applied to the kernel matrix (see constraints).
bias_constraint: Constraint function applied to the bias vector (see constraints).

Input shape
4D tensor with shape: (batch, channels, rows, cols) if data_format is "channels_first" or 4D tensor with shape: (batch, rows, cols, channels) if data_format is "channels_last".
Output shape
4D tensor with shape: (batch, filters, new_rows, new_cols) if data_format is "channels_first" or 4D tensor with shape: (batch, new_rows, new_cols, filters) if data_format is "channels_last". rows and cols values might have changed due to padding.
``` json
    {
    "type": "Conv2D",
    "params": {
      "filters": "integer",
      "kernel_size": "integer",
      "strides": "integer",
      "padding": "integer",
      "data_format": "string",
      "dilation_rate": "integer",
      "activation": "activations",
      "use_bias": "boolean",
      "kernel_initializer": "initializer",
      "bias_initializer": "initializer",
      "kernel_regularizer": "regularizer",
      "bias_regularizer": "regularizer",
      "activity_regulizer": "regulizer",
      "kernel_constraint": "constraints",
      "bias_constraint": "constraints"
    }

  }
```
# 3. Pooling Layers

## 1.MaxPooling1D
**keras.layers.MaxPooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last')**

Arguments
***pool_size***: Integer, size of the max pooling windows.
***strides***: Integer, or None. Factor by which to downscale. E.g. 2 will halve the input. If None, it will default to pool_size.
***padding***: One of "valid" or "same" (case-insensitive).
***data_format***: A string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch, steps, features) while channels_first corresponds to inputs with shape (batch, features, steps)

``` json
    {
    "type": "MaxPooling1D",
    "params": {
      "pool_size": "integer",
      "strides": "integer",
      "padding": "valid/same",
      "data_format": "string"
    }
 ```
## 2. MaxPooling2D
**keras.layers.MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None)**

Arguments
***pool_size***: integer or tuple of 2 integers, factors by which to downscale (vertical, horizontal). (2, 2) will halve the input in both spatial dimension. If only one integer is specified, the same window length will be used for both dimensions.
***strides***: Integer, tuple of 2 integers, or None. Strides values. If None, it will default to pool_size.
***padding***: One of "valid" or "same" (case-insensitive).
***data_format***: A string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch, height, width, channels) while channels_first corresponds to inputs with shape (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".
``` json
    {
    "type": "MaxPooling2D",
    "params": {
      "pool_size": "integer",
      "strides": "integer",
      "padding": "valid/same",
      "data_format": "string"
    }
 ```
## 3. AveragePooling1D
**keras.layers.AveragePooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last')**

Arguments
***pool_size***: Integer, size of the average pooling windows.
***strides***: Integer, or None. Factor by which to downscale. E.g. 2 will halve the input. If None, it will default to pool_size.
***padding***: One of "valid" or "same" (case-insensitive).
***data_format***: A string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch, steps, features) while channels_first corresponds to inputs with shape (batch, features, steps).

``` json
    {
    "type": "AveragePooling1D",
    "params": {
      "pool_size": "integer",
      "strides": "integer",
      "padding": "valid/same",
      "data_format": "string"
    }
 ```
## 4. AveragePooling2D
**keras.layers.AveragePooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None)**

Arguments
***pool_size***: integer or tuple of 2 integers, factors by which to downscale (vertical, horizontal). (2, 2) will halve the input in both spatial dimension. If only one integer is specified, the same window length will be used for both dimensions.
***strides***: Integer, tuple of 2 integers, or None. Strides values. If None, it will default to pool_size.
***padding***: One of "valid" or "same" (case-insensitive).
***data_format***: A string, one of channels_last (default) or channels_first. The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch, height, width, channels) while channels_first corresponds to inputs with shape (batch, channels, height, width). It defaults to the image_data_format value found in your Keras config file at ~/.keras/keras.json. If you never set it, then it will be "channels_last".

``` json
    {
    "type": "AveragePooling2D",
    "params": {
      "pool_size": "integer",
      "strides": "integer",
      "padding": "valid/same",
      "data_format": "string"
    }
 ```
# 4. Recurrent Layers

## 1. SimpleRNN (Fully-connected RNN where the output is to be fed back to input)
**keras.layers.SimpleRNN(units, activation='tanh', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False)**

Arguments
***units***: Positive integer, dimensionality of the output space.
***activation***: Activation function to use (see activations). Default: hyperbolic tangent (tanh). If you pass None, no activation is applied (ie. "linear" activation: a(x) = x).
***use_bias***: Boolean, whether the layer uses a bias vector.
***kernel_initializer***: Initializer for the kernel weights matrix, used for the linear transformation of the inputs (see initializers).
***recurrent_initializer***: Initializer for the recurrent_kernel weights matrix, used for the linear transformation of the recurrent state (see initializers).
***bias_initializer***: Initializer for the bias vector (see initializers).
***kernel_regularizer***: Regularizer function applied to the kernel weights matrix (see regularizer).
***recurrent_regularizer***: Regularizer function applied to the recurrent_kernel weights matrix (see regularizer).
***bias_regularizer***: Regularizer function applied to the bias vector (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***kernel_constraint***: Constraint function applied to the kernel weights matrix (see constraints).
***recurrent_constraint***: Constraint function applied to the recurrent_kernel weights matrix (see constraints).
***bias_constraint***: Constraint function applied to the bias vector (see constraints).
***dropout***: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs.
***recurrent_dropout***: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state.
***return_sequences***: Boolean. Whether to return the last output in the output sequence, or the full sequence.
***return_state***: Boolean. Whether to return the last state in addition to the output.
***go_backwards***: Boolean (default False). If True, process the input sequence backwards and return the reversed sequence.
***stateful***: Boolean (default False). If True, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch.
***unroll***: Boolean (default False). If True, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.

``` json
    {
    "type": "SimpleRnn",
    "params": {
      "units": "integer",
      "activation": "activations",
      "use_bias": "boolean",
      "kernel_initializer": "initializers",
      "recurrent_initializer": "initializers",
      "bias_initializer": "initializers",
      "kernel_regularizer": "regularizer",
      "recurrent_regularizer": "regularizer",
      "bias_regularizer": "regularizer",
      "activity_regularizer": "regularizer",
      "kernel_constraint": "constraints",
      "recurrent_constraint": "constraints",
      "bias_constraint": "constraints",
      "dropout": "float",
      "recurrent_dropout": "float",
      "return_sequences": "boolean",
      "return_state": "boolean",
      "go_backwards": "boolean",
      "stateful": "boolean",
      "unroll": "boolean"
    }
  }
```
## 2. LSTM (Long Short-Term Memory layer)
**keras.layers.LSTM(units, activation='tanh', recurrent_activation='sigmoid', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, implementation=2, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False)**

Arguments
***units***: Positive integer, dimensionality of the output space.
***activation***: Activation function to use (see activations). Default: hyperbolic tangent (tanh). If you pass None, no activation is applied (ie. "linear" activation: a(x) = x).
recurrent_activation: Activation function to use for the recurrent step (see activations). Default: hard sigmoid (hard_sigmoid). If you pass None, no activation is applied (ie. "linear" activation: a(x) = x).
***use_bias***: Boolean, whether the layer uses a bias vector.
***kernel_initializer***: Initializer for the kernel weights matrix, used for the linear transformation of the inputs. (see initializers).
***recurrent_initialize***: Initializer for the recurrent_kernel weights matrix, used for the linear transformation of the recurrent state. (see initializers).
***bias_initializer***: Initializer for the bias vector (see initializers).
***unit_forget_bias***: Boolean. If True, add 1 to the bias of the forget gate at initialization. Setting it to true will also force bias_initializer="zeros". This is recommended in Jozefowicz et al. (2015).
***kernel_regularizer***: Regularizer function applied to the kernel weights matrix (see regularizer).
***recurrent_regularizer***: Regularizer function applied to the recurrent_kernel weights matrix (see regularizer).
***bias_regularizer***: Regularizer function applied to the bias vector (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***kernel_constraint***: Constraint function applied to the kernel weights matrix (see constraints).
***recurrent_constraint***: Constraint function applied to the recurrent_kernel weights matrix (see constraints).
***bias_constraint***: Constraint function applied to the bias vector (see constraints).
***dropout***: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs.
***recurrent_dropout***: Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state.
***implementation***: Implementation mode, either 1 or 2. Mode 1 will structure its operations as a larger number of smaller dot products and additions, whereas mode 2 will batch them into fewer, larger operations. These modes will have different performance profiles on different hardware and for different applications.
***return_sequences***: Boolean. Whether to return the last output in the output sequence, or the full sequence.
***return_state***: Boolean. Whether to return the last state in addition to the output. The returned elements of the states list are the hidden state and the cell state, respectively.
***go_backwards***: Boolean (default False). If True, process the input sequence backwards and return the reversed sequence.
***stateful***: Boolean (default False). If True, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch.
***unroll***: Boolean (default False). If True, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences.
``` json
{
    "type": "LSTM",
    "params": {
      "units": "integer",
      "activation": "activations",
      "recurrent_activation": "activations",
      "use_bias": "boolean",
      "kernel_initializer": "initializers",
      "recurrent_initializer": "initializers",
      "bias_initializer": "initializers",
      "unit_forget_bias": "boolean",
      "kernel_regularizer": "regularizer",
      "recurrent_regularizer": "regularizer",
      "bias_regularizer": "regularizer",
      "activity_regularizer": "regularizer",
      "kernel_constraint": "constraints",
      "recurrent_constraint": "constraints",
      "bias_constraint": "constraints",
      "dropout": "float",
      "recurrent_dropout": "float",
      "implementation": "1/2",
      "return_sequences": "boolean",
      "return_state": "boolean",
      "go_backwards": "boolean",
      "stateful": "boolean",
      "unroll": "boolean"
      }
  }
```
# 5. Embedding Layers

**keras.layers.Embedding(input_dim, output_dim, embeddings_initializer='uniform', embeddings_regularizer=None, activity_regularizer=None, embeddings_constraint=None, mask_zero=False, input_length=None)**
Arguments
***input_dim***: int > 0. Size of the vocabulary, i.e. maximum integer index + 1.
***output_dim***: int >= 0. Dimension of the dense embedding.
***embeddings_initializer***: Initializer for the embeddings matrix (see initializers).
***embeddings_regularizer***: Regularizer function applied to the embeddings matrix (see regularizer).
***activity_regularizer***: Regularizer function applied to the output of the layer (its "activation"). (see regularizer).
***embeddings_constraint***: Constraint function applied to the embeddings matrix (see constraints).
***mask_zero***: Whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is True then all subsequent layers in the model need to support masking or an exception will be raised. If mask_zero is set to True, as a consequence, index 0 cannot be used in the vocabulary (input_dim should equal size of vocabulary + 1).
***input_length***: Length of input sequences, when it is constant. This argument is required if you are going to connect Flatten then Dense layers upstream (without it, the shape of the dense outputs cannot be computed).

This layer can only be used as the first layer in a model.
``` json
{
    "type": "Embedding",
    "params": {
      "input_dim": "integer",
      "output_dim": "integer",
      "embeddings_initializer": "initializer",
      "embeddings_regularizer": "regularizer",
      "activity_regularizer": "regularizer",
      "embeddings_constraint": "constraints",
      "mask_zero": "boolean",
      "input_length": "integer"
    }

  }
```

# 6. Normalization Layers
**keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)**

Normalize the activations of the previous layer at each batch, i.e. applies a transformation that maintains the mean activation close to 0 and the activation standard deviation close to 1.

Arguments
***axis***: Integer, the axis that should be normalized (typically the features axis). For instance, after a Conv2D layer with data_format="channels_first", set axis=1 in BatchNormalization.
***momentum***: Momentum for the moving mean and the moving variance.
***epsilon***: Small float added to variance to avoid dividing by zero.
***center***: If True, add offset of beta to normalized tensor. If False, beta is ignored.
***scale***: If True, multiply by gamma. If False, gamma is not used. When the next layer is linear (also e.g. nn.relu), this can be disabled since the scaling will be done by the next layer.
***beta_initializer***: Initializer for the beta weight.
***gamma_initializer***: Initializer for the gamma weight.
***moving_mean_initializer***: Initializer for the moving mean.
***moving_variance_initializer***: Initializer for the moving variance.
***beta_regularizer***: Optional regularizer for the beta weight.
***gamma_regularizer***: Optional regularizer for the gamma weight.
***beta_constraint***: Optional constraint for the beta weight.
***gamma_constraint***: Optional constraint for the gamma weight.
``` json
{
    "type": "BatchNormalization",
    "params": {
      "axis": "integer",
      "momentum": "float",
      "epsilion": "float",
      "center": "boolean",
      "scale": "boolean",
      "beta_initializer": "initializer",
      "gamma_initializer": "initializer",
      "moving_mean_initializer": "initializer",
      "moving_variance_initializer": "initializer",
      "beta_regularizer": "regularizer",
      "gamma_regularizer": "regularizer",
      "beta_constraint": "constraint",
      "gamma_constraint": "constraint"
    }
  }
```


