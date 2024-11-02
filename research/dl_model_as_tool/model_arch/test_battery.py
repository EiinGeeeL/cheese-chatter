import tensorflow as tf
from tensorflow.keras import layers

# Itertools.product() Function

# Defining the dataset
dataset = {
    'path1': 'temp_all_data',
    'path2': 'temp_solo_alcorques',
}

# Defining tf.keras methods
keras_loss = {
    'binary_crossentropy': tf.keras.losses.BinaryCrossentropy(from_logits=False),
    'binary_focal_crossentropy': tf.keras.losses.BinaryFocalCrossentropy(from_logits=False),
    'categorical_crossentropy': tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    'categorical_focal_crossentropy': tf.keras.losses.CategoricalFocalCrossentropy(from_logits=True),
    'sparse_categorical_crossentropy':tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    'generic_loss': tf.keras.Loss(),
    }

# %%
# Main params to tune
params_int_activation_loss_battery = {
    'batch_size': 32,
    'epochs': 15,
    'img_size': 164,
    'validation_split': 0.2,
    'img_src': dataset['path2'],
    'label_mode': 'int',
    'tfds_seed': 123,
    'factor_augmentation': 0.2,
    'dense_units_output': 2, # NOTE: number of classes or 1 if label mode binary and activation_output sigmoid
    'activation_output': ['linear', 'relu', 'sigmoid'],
    'loss': [
        keras_loss['sparse_categorical_crossentropy'], 
        keras_loss['categorical_crossentropy'], 
        keras_loss['categorical_focal_crossentropy'], 
        keras_loss['generic_loss'],
        ],
    'optimizer': 'adam',
    'metrics': ['accuracy'],
}


params_binary_activation_loss_battery = {
    'batch_size': 32,
    'epochs': 15,
    'img_size': 164,
    'validation_split': 0.2,
    'img_src': dataset['path2'],
    'label_mode': 'binary',
    'tfds_seed': 123,
    'factor_augmentation': 0.2,
    'dense_units_output': 1, # NOTE: number of classes or 1 if label mode binary and activation_output sigmoid
    'activation_output': ['linear', 'relu', 'sigmoid'],
    'loss': [
        keras_loss['sparse_categorical_crossentropy'], 
        keras_loss['binary_crossentropy'], 
        keras_loss['binary_focal_crossentropy'], 
        keras_loss['generic_loss'],
        ],
    'optimizer': 'adam',
    'metrics': ['accuracy'],
}


# TODO: TEST DIFFERENTS IMAGE SIZE FACTOR AUGMENTATION AND OPTIMIZER TOO