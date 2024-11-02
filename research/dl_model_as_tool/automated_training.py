# %%
import mlflow
import tensorflow as tf
from tensorflow.keras import layers

from itertools import product
from model_arch.sequential_cnn import prepare_tfds, cnn_architectures
from model_arch.test_battery import params_int_activation_loss_battery, params_binary_activation_loss_battery

# %%
# Selecting the model arch and the dataset
build_model = cnn_architectures['cnn_champion']

# %%
# Creating the product of activation_output and loss
combinations = product(params_int_activation_loss_battery['activation_output'], params_int_activation_loss_battery['loss'])

# Iterate through combinations
for activation, loss in combinations:
    try:
        # Create a new params dictionary for each combination
        params = params_int_activation_loss_battery.copy()
        params['activation_output'] = activation
        params['loss'] = loss

        # Obtain the tensorflow datasets
        train_ds, val_ds = prepare_tfds(params)

        # Build and compile the model
        cnn = build_model(tf.keras.Sequential(), params)
        cnn.summary()

        cnn.compile(
            optimizer=params['optimizer'],
            loss=params['loss'],
            metrics=params['metrics'],
        )

        # Fit the model
        history = cnn.fit(
            train_ds,
            validation_data=val_ds,
            epochs=params['epochs'],
            batch_size=params["batch_size"]
        )

        # Evaluation
        loss, accuracy = cnn.evaluate(val_ds)

        # Register the evaluation
        mlflow.set_experiment("TOOL ZONAS VERDES CNN")
        
        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics({
                'accuracy': accuracy,
                'loss': loss,
            })
            mlflow.set_tag("arch info", build_model.__name__)
            # mlflow.tensorflow.log_model(cnn, model_name)

    except Exception as e:
        print(f"An error occurred for activation: {activation}, loss: {loss}. Error: {e}")
        continue  # Continue with the next combination