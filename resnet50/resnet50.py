import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


# class BatchNorm(layers.BatchNormalization):
#     """Extends the Keras BatchNormalization class to allow a central place
#     to make changes if needed.
#     Batch normalization has a negative effect on training if batches are small
#     so this layer is often frozen (via setting in Config class) and functions
#     as linear layer.
#     """
#     def call(self, inputs, training=None):
#         """
#         Note about training values:
#             None: Train BN layers. This is the normal mode
#             False: Freeze BN layers. Good when batch size is small
#             True: (don't use). Set layer in training mode even when making inferences
#         """
        
#         return super(self.__class__, self).call(inputs, training=training)

class BatchNorm(layers.BatchNormalization):
    """
    Replace BatchNormalization layers with this new layer.
    This layer has fixed momentum 0.9.
    """
    def __init__(self, momentum=0.9, name=None, **kwargs):
        super(BatchNorm, self).__init__(momentum=0.9, name=name, **kwargs)

    def call(self, inputs, training=None):
        return super().call(inputs=inputs, training=training)

    def get_config(self):
        config = super(BatchNorm, self).get_config()
        return config




############################################################
#  Resnet Graph
############################################################

# Code adopted from:
# https://github.com/fchollet/deep-learning-models/blob/master/resnet50.py

def identity_block(input_tensor, kernel_size, filters, stage, block,
                   use_bias=True, train_bn=True):
    """The identity_block is the block that has no conv layer at shortcut
    # Arguments
        input_tensor: input tensor
        kernel_size: default 3, the kernel size of middle conv layer at main path
        filters: list of integers, the nb_filters of 3 conv layer at main path
        stage: integer, current stage label, used for generating layer names
        block: 'a','b'..., current block label, used for generating layer names
        use_bias: Boolean. To use or not use a bias in conv layers.
        train_bn: Boolean. Train or freeze Batch Norm layers
    """
    nb_filter1, nb_filter2, nb_filter3 = filters
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    x = layers.Conv2D(nb_filter1, (1, 1), name=conv_name_base + '2a',
                  use_bias=use_bias)(input_tensor)
    x = BatchNorm(name=bn_name_base + '2a')(x, training=train_bn)
    x = layers.Activation('relu')(x)

    x = layers.Conv2D(nb_filter2, (kernel_size, kernel_size), padding='same',
                  name=conv_name_base + '2b', use_bias=use_bias)(x)
    x = BatchNorm(name=bn_name_base + '2b')(x, training=train_bn)
    x = layers.Activation('relu')(x)

    x = layers.Conv2D(nb_filter3, (1, 1), name=conv_name_base + '2c',
                  use_bias=use_bias)(x)
    x = BatchNorm(name=bn_name_base + '2c')(x, training=train_bn)

    x = layers.Add()([x, input_tensor])
    x = layers.Activation('relu', name='res' + str(stage) + block + '_out')(x)
    return x


def conv_block(input_tensor, kernel_size, filters, stage, block,
               strides=(2, 2), use_bias=True, train_bn=True):
    """conv_block is the block that has a conv layer at shortcut
    # Arguments
        input_tensor: input tensor
        kernel_size: default 3, the kernel size of middle conv layer at main path
        filters: list of integers, the nb_filters of 3 conv layer at main path
        stage: integer, current stage label, used for generating layer names
        block: 'a','b'..., current block label, used for generating layer names
        use_bias: Boolean. To use or not use a bias in conv layers.
        train_bn: Boolean. Train or freeze Batch Norm layers
    Note that from stage 3, the first conv layer at main path is with subsample=(2,2)
    And the shortcut should have subsample=(2,2) as well
    """
    nb_filter1, nb_filter2, nb_filter3 = filters
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    x = layers.Conv2D(nb_filter1, (1, 1), strides=strides,
                  name=conv_name_base + '2a', use_bias=use_bias)(input_tensor)
    x = BatchNorm(name=bn_name_base + '2a')(x, training=train_bn)
    x = layers.Activation('relu')(x)

    x = layers.Conv2D(nb_filter2, (kernel_size, kernel_size), padding='same',
                  name=conv_name_base + '2b', use_bias=use_bias)(x)
    x = BatchNorm(name=bn_name_base + '2b')(x, training=train_bn)
    x = layers.Activation('relu')(x)

    x = layers.Conv2D(nb_filter3, (1, 1), name=conv_name_base +
                  '2c', use_bias=use_bias)(x)
    x = BatchNorm(name=bn_name_base + '2c')(x, training=train_bn)

    shortcut = layers.Conv2D(nb_filter3, (1, 1), strides=strides,
                         name=conv_name_base + '1', use_bias=use_bias)(input_tensor)
    shortcut = BatchNorm(name=bn_name_base + '1')(shortcut, training=train_bn)

    x = layers.Add()([x, shortcut])
    x = layers.Activation('relu', name='res' + str(stage) + block + '_out')(x)
    return x


def resnet_graph(input_image, architecture, stage5=False, train_bn=True):
    """Build a ResNet graph.
        architecture: Can be resnet50 or resnet101
        stage5: Boolean. If False, stage5 of the network is not created
        train_bn: Boolean. Train or freeze Batch Norm layers
    """
    assert architecture in ["resnet50", "resnet101"]
    # Stage 1
    x = layers.ZeroPadding2D((3, 3))(input_image)
    x = layers.Conv2D(64, (7, 7), strides=(2, 2), name='conv1', use_bias=True)(x)
    x = BatchNorm(name='bn_conv1')(x, training=train_bn)
    x = layers.Activation('relu')(x)
    C1 = x = layers.MaxPooling2D((3, 3), strides=(2, 2), padding="same")(x)
    # Stage 2
    x = conv_block(x, 3, [64, 64, 256], stage=2, block='a', strides=(1, 1), train_bn=train_bn)
    x = identity_block(x, 3, [64, 64, 256], stage=2, block='b', train_bn=train_bn)
    C2 = x = identity_block(x, 3, [64, 64, 256], stage=2, block='c', train_bn=train_bn)
    # Stage 3
    x = conv_block(x, 3, [128, 128, 512], stage=3, block='a', train_bn=train_bn)
    x = identity_block(x, 3, [128, 128, 512], stage=3, block='b', train_bn=train_bn)
    x = identity_block(x, 3, [128, 128, 512], stage=3, block='c', train_bn=train_bn)
    C3 = x = identity_block(x, 3, [128, 128, 512], stage=3, block='d', train_bn=train_bn)
    # Stage 4
    x = conv_block(x, 3, [256, 256, 1024], stage=4, block='a', train_bn=train_bn)
    block_count = {"resnet50": 5, "resnet101": 22}[architecture]
    for i in range(block_count):
        x = identity_block(x, 3, [256, 256, 1024], stage=4, block=chr(98 + i), train_bn=train_bn)
    C4 = x
    # Stage 5
    if stage5:
        x = conv_block(x, 3, [512, 512, 2048], stage=5, block='a', train_bn=train_bn)
        x = identity_block(x, 3, [512, 512, 2048], stage=5, block='b', train_bn=train_bn)
        C5 = x = identity_block(x, 3, [512, 512, 2048], stage=5, block='c', train_bn=train_bn)
    else:
        C5 = None
    return [C1, C2, C3, C4, C5]


def get_imagenet_weights():
  """Downloads ImageNet trained weights from Keras.
  Returns path to weights file.
  """
  from keras.utils.data_utils import get_file
  TF_WEIGHTS_PATH_NO_TOP = 'https://github.com/fchollet/deep-learning-models/'\
                            'releases/download/v0.2/'\
                            'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'
  weights_path = get_file('resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                          TF_WEIGHTS_PATH_NO_TOP,
                          cache_subdir='models',
                          md5_hash='a268eb855778b3df3c7506639542a6af')
  return weights_path


def get_resnet50(input_shape,train_bn=False):
  x_input=layers.Input(shape=input_shape)
  outputs=resnet_graph(input_image=x_input, architecture='resnet50', stage5=True, train_bn=train_bn)
  custom_model=Model(x_input,outputs=outputs[-1],name='custom_resnet55')
  custom_model.load_weights(get_imagenet_weights())
  return custom_model

if __name__=="__main__":
    custom_model=get_resnet50((None,None,3),train_bn=False)
    custom_model.summary()