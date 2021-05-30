import tensorflow.compat.v1 as tf

with tf.compat.v1.Session() as sess:    
    saver = tf.train.import_meta_graph('my-tiny-yolo-6780.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./'))
    print(sess.run('w1:0'))
##Model has been restored. Above statement will print the saved value of w1.
