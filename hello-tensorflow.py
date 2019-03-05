
# Hello world code in tensorflow

#import tensorflow
import tensorflow as tf

#Create a tensorflow constant string
hello = tf.constant("Hello, Tensorflow")
#create a session
sess = tf.Session()
#print the result
print(sess.run(hello))

