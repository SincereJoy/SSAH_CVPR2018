# SSAH_CVPR2018
This is the code for "Self-Supervised Adversarial Hashing Networks for Cross-Modal Retrieval".

The official code can be get from https://github.com/lelan-li/SSAH. 

The original code is built for tensorflow1 and python2. I modified it so that it can run on python3 and tensorflow2. Also I add some implementation details of this work, like how to get the dataset.

## Environment
**Python** 3.7.11

**Tensorflow** 2.3.1

## Dataset
Original MIRFLICKR 25000 dataset：https://press.liacs.nl/mirflickr/mirdownload.html
The processed Flickr-25K dataset can be downloaded from https://github.com/jiangqy/DCMH-CVPR2017/tree/master/DCMH_tensorflow/DCMH_tensorflow.

Once get the Flickr-25K data files, unzip them and put them in the _'./data/'_ directory. Then run _'./data/data_process.m'_ to get the input data file _'FLICKR-25K.mat'_. 

## Pre-trained model
Download the pre-trained imagenet model _'imagenet-vgg-f.mat'_ from https://www.vlfeat.org/matconvnet/pretrained/ and put it in the _'./data/'_ directory.

## Train
Run _'Main.py'_.

I get the best result with one epoch:

```
...test map: map(i->t): 0.790, map(t->i): 0.799
...test map: map(t->t): 0.767, map(i->i): 0.825
```
