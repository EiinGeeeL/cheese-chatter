import tensorflow as tf
from tensorflow.keras import layers

def prepare_tfds(params: dict):
  path = params["img_src"]
  img_height = params["img_size"]
  img_width = params["img_size"]
  label_mode = params["label_mode"] # NOTE: "binary" (e.g. for binary_crossentropy), "categorical" or "int" (e.g. for categorical_crossentropy loss)
  batch_size = params["batch_size"]
  validation_split = params["validation_split"]
  seed = params["tfds_seed"]

  # Use image_dataset_from_directory on the temporary directory structure
  train_ds = tf.keras.utils.image_dataset_from_directory(
    path,
    validation_split=validation_split,
    subset="training",
    seed=seed,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode=label_mode,
    shuffle=True, 
  )
  
  val_ds = tf.keras.utils.image_dataset_from_directory(
    path,
    validation_split=validation_split,
    subset="validation",
    seed=seed,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode=label_mode,
    shuffle=True,
  )
  
  return train_ds, val_ds


def resize_and_rescale(params: dict) -> tf.keras.Sequential:
  resize_and_rescale = tf.keras.Sequential([
    layers.Resizing(params["img_size"], params["img_size"]), # NOTE: To resize cause tf.Keras.Input is None, None
    layers.Rescaling(1./255)
  ],
  name="resize_and_rescale",
  )

  return resize_and_rescale


def data_augmentation(params: dict) -> tf.keras.Sequential:
  data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"), # It is difficult to take a foto vertical
    layers.RandomRotation(factor=params["factor_augmentation"]),
    layers.RandomZoom(height_factor=params["factor_augmentation"], width_factor=params["factor_augmentation"]),
    layers.RandomBrightness(factor=params["factor_augmentation"]),
    layers.RandomContrast(factor=params["factor_augmentation"]),
  ],    
  name="data_augmentation",
  )

  return data_augmentation


def build_cnn_v01(cnn: tf.keras.Sequential, params: dict) -> tf.keras.Sequential:
  cnn.add(tf.keras.Input(shape=(None, None, 3)))
  cnn.add(data_augmentation(params=params))
  cnn.add(resize_and_rescale(params=params))
  cnn.add(layers.Normalization())
  cnn.add(layers.Conv2D(16, 3, padding='same', activation='relu'))
  cnn.add(layers.MaxPooling2D())
  cnn.add(layers.Conv2D(32, 3, padding='same', activation='relu'))
  cnn.add(layers.MaxPooling2D())
  cnn.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
  cnn.add(layers.MaxPooling2D())
  cnn.add(layers.Dropout(0.2))
  cnn.add(layers.Flatten())
  cnn.add(layers.Dense(128, activation='relu'))
  cnn.add(layers.Dense(params["dense_units_output"], activation=params["activation_output"], name="outputs")) # NOTE: If no activation output aplied: 'linear'
  
  return cnn

# def build_cnn_v02(cnn: tf.keras.Sequential, params: dict) -> tf.keras.Sequential:
#   cnn.add(tf.keras.Input(shape=(None, None, 3)))
#   cnn.add(data_augmentation(params=params))
#   cnn.add(resize_and_rescale(params=params))
#   cnn.add(layers.Normalization())
#   cnn.add(layers.Conv2D(16, 3, padding='same', activation='relu'))
#   cnn.add(layers.MaxPooling2D())
#   cnn.add(layers.Conv2D(32, 3, padding='same', activation='relu'))
#   cnn.add(layers.MaxPooling2D())
#   cnn.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
#   cnn.add(layers.MaxPooling2D())
#   cnn.add(layers.Conv2D(128, 3, padding='same', activation='relu'))
#   cnn.add(layers.MaxPooling2D())
#   cnn.add(layers.Dropout(0.2))
#   cnn.add(layers.Flatten())
#   cnn.add(layers.Dense(256, activation='relu'))
#   cnn.add(layers.Dense(params["dense_units_output"], activation=params["activation_output"], name="outputs")) # NOTE: If no activation output aplied: 'linear'
  
#   return cnn

# def build_cnn_v03(cnn: tf.keras.Sequential, params: dict) -> tf.keras.Sequential:
#     cnn.add(tf.keras.Input(shape=(None, None, 3)))
#     cnn.add(data_augmentation(params=params))
#     cnn.add(resize_and_rescale(params=params))
#     cnn.add(layers.Normalization())

#     # Reduced complexity with fewer layers and filters
#     cnn.add(layers.Conv2D(16, 3, padding='same', activation='relu'))
#     cnn.add(layers.MaxPooling2D())
    
#     cnn.add(layers.Conv2D(32, 3, padding='same', activation='relu'))
#     cnn.add(layers.MaxPooling2D())
    
#     cnn.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
#     cnn.add(layers.MaxPooling2D())
    
#     # Global Average Pooling to reduce parameters and combat overfitting
#     cnn.add(layers.GlobalAveragePooling2D())
    
#     cnn.add(layers.Dropout(0.3))  # Moderate dropout for regularization
#     cnn.add(layers.Dense(128, activation='relu'))
#     cnn.add(layers.Dropout(0.5))  # Additional dropout to prevent overfitting
    
#     # Output layer
#     cnn.add(layers.Dense(params["dense_units_output"], activation=params["activation_output"], name="outputs"))

#     return cnn

cnn_architectures = {
  'cnn_champion': build_cnn_v01,
  # 'cnn_v02': build_cnn_v02,
  # 'cnn_v03': build_cnn_v03,
}