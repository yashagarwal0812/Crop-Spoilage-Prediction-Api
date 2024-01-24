from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
model = load_model('model.h5')

d = [0, 17.45, 6.66, 0, 2, 0.95]

input_data = np.array([d])
e = tf.reshape(input_data, shape=(tf.shape(input_data)[0], -1))
f = model.predict(e)
print(f[0][0])