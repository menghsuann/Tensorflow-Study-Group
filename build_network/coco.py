import tensorflow as tf

t_range = [val/10.0 for val in list(range(-10, 11, 1))]
y_range = ([0] *10) + [0.5] + ([1]*10)

with tf.name_scope('sigmoid') as scope:
    t = tf.placeholder(tf.float32, name="t")
    y = tf.placeholder(tf.float32, name="y")
    a = tf.Variable([.01], tf.float32, name="a")



    sigmoid = 1/(1+tf.exp(-t*a))

    delta = sigmoid - y
    square_delta = tf.square(delta)

    loss = tf.reduce_sum(square_delta)



optimizer = tf.train.GradientDescentOptimizer(11)
trainer = optimizer.minimize(loss)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)



y_range.reverse()

for i in range(1000):
    sess.run(trainer, {y: y_range, t: t_range})
    print (sess.run(loss, {y: y_range, t: t_range}))
    print (sess.run([a]))

file_writer = tf.summary.FileWriter('./summary', sess.graph)
