import tensorflow as tf

sess = tf.Session()
E = tf.constant([2.7182818284590452353602874], tf.float32)
a = tf.Variable([1.0], tf.float32)
t = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
t_range = [val/10.0 for val in list(range(-10, 11, 1))]
y_range = ([0] *10) + [0.5] + ([1]*10)

sigmoid = 1 / (1 + E**(-a*t))

delta = tf.square(sigmoid-y)

loss = tf.reduce_sum(delta)

optimizer = tf.train.GradientDescentOptimizer(1)
trainer = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    sess.run(trainer, {t: t_range, y: y_range})
    print (sess.run([a]))
