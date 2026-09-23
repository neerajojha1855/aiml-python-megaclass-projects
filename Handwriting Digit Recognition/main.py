import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from matplotlib import pyplot as plt

mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train, X_test = X_train / 255.0, X_test / 255.0

X_train_reshaped = X_train.reshape(-1, 28, 28, 1)
X_test_reshaped = X_test.reshape(-1, 28, 28, 1)

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mnist_model.keras")

if os.path.exists(MODEL_PATH):
    print("Loading saved model...")
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    print("Training new model...")
    model = Sequential([
        Input(shape=(28, 28, 1)),
        Conv2D(32, (3,3), activation="relu"),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation="relu"),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(X_train_reshaped, y_train, epochs=5, validation_data=(X_test_reshaped, y_test))
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

test_loss, test_accuracy = model.evaluate(X_test_reshaped, y_test)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

idx = 0
test_image = X_test[idx].reshape(1, 28, 28, 1)

prediction = np.argmax(model.predict(test_image))
plt.imshow(X_test[idx], cmap="gray")
plt.title(f"Predicted Digit: {prediction}")
plt.show()