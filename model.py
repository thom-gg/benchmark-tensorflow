import tensorflow as tf 
from objects import Configuration, Layer
import time


mnist = tf.keras.datasets.mnist



(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_and_evaluate_model(config: Configuration, epochs: int):
    layers = [tf.keras.layers.Flatten(input_shape=(28, 28))]
    for l in config.layers_list:
        layers.append(tf.keras.layers.Dense(l.nb_neurons, activation='relu'))
    layers.append(tf.keras.layers.Dense(10)) # output layer

    model = tf.keras.models.Sequential(layers)
    predictions = model(x_train[:1]).numpy()
    predictions
    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn(y_train[:1], predictions).numpy()

    model.compile(optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy'])

    start_time = time.time()
    model.fit(x_train, y_train, epochs=epochs)
    end_time = time.time() 

    duration = end_time - start_time # in seconds

    [loss, accuracy] = model.evaluate(x_test,  y_test, verbose=2)
    return (accuracy, duration)


