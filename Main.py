import os
import tensorflow as tf
from setting import *
from SSAH import SSAH

os.environ['CUDA_VISIBLE_DEVICES'] = select_gpu
gpuconfig = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=per_process_gpu_memory_fraction))

if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)
if not os.path.exists(Savecode):
    os.makedirs(Savecode)

with tf.compat.v1.Session(config=gpuconfig) as sess:
    model = SSAH(sess)
    model.train() if phase == 'train' else model.test('test')
