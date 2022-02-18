# SSAH_CVPR2018
This is the code for "Self-Supervised Adversarial Hashing Networks for Cross-Modal Retrieval".

The official code can be get from https://github.com/lelan-li/SSAH. 

The original code is built for tensorflow1 and python2. I modified it so that it can run on python3 and tensorflow2. Also I add some implementation details of this work, like how to get the dataset.

### Environment
Python 3.7.11

Tensorflow 2.3.1

### Dataset
The Flickr-25K dataset can be downloaded from https://github.com/jiangqy/DCMH-CVPR2017/tree/master/DCMH_tensorflow/DCMH_tensorflow.

Once get the Flickr-25K data files, unzip them and put them in the './data' directory. Then run 'data_process.m' to get the input data file 'FLICKR-25K.mat'. 
