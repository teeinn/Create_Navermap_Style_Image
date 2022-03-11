import tensorflow as tf

@tf.function
def get_mse(y_true, y_pred):
    diff = tf.pow(y_true - y_pred, 2)
    return  tf.reduce_mean(diff)

y_true = tf.random.uniform([5], maxval=10, dtype=tf.int32)
y_pred = tf.random.uniform([5], maxval=10, dtype=tf.int32)
print(get_mse(y_true, y_pred))
# tf.Tensor(13, shape=(), dtype=int32)
