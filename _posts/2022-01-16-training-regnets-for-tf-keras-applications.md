---
title: 'Training RegNets for tf.keras.applications'
date: 2022-01-16
permalink: /blogs/training_regnets-for_tf_keras_applications/
tags:
  - keras
  - tensorflow
  - machine learning
---

This blog post is about sharing our experience of training 24 RegNet models for tf.keras.applications.  

## Prologue
tf.keras.applications is a set of built-in models in TensorFlow-Keras. They are pretrained on ImageNet-1k, and are just one function call away. This makes life easier for the ML folks as they have ready-to-go models at their disposal. [RegNets](https://arxiv.org/abs/2003.13678) are highly efficient and scalable models proposed by Facebook AI Research (FAIR). They are used in works like [SEER](https://arxiv.org/abs/2103.01988) which need models that can scale to billions and billions of parameters. In submitting a [PR to Keras](https://github.com/keras-team/keras/pull/15702), I implement and train 24 RegNet models of varying complexity to tf.keras.applications. 

Even though I was responsible for the primary development work on the PR as well as training the models, I received great help from the community which makes it truly collaborative.

I performed several experiments with these models, because the reported accuracies could not be reproduced using the hyperparameters provided in the paper. This blog post is a record of these experiments I tried and how they panned out. 


## Acknowledgements:
I sincerely thank the Keras team for allowing me to add these models. Huge thanks to the [TPU Research Group (TRC)](https://sites.research.google/trc/about/) for providing TPUs for the entire duration of this project, without which the project would have been impossible. Google supported this work by providing Google Cloud credit. Thanks a lot to [Francois Chollet](https://github.com/fchollet) and [Matt Watson](https://github.com/mattdangerw) from the Keras team for their reviews. Thanks to [Qianli Scott Zhu](https://github.com/qlzh727) for his guidance in building Keras from source on TPU VMs. Special thanks to [Lukas Geiger] (https://github.com/lgeiger) for his contributions to the code. Thanks a ton to [Sayak Paul](https://github.com/sayakpaul) for his continuous guidance and encouragement.

## The Basics
### About the paper
The paper ["Designing Network Design Spaces"](https://arxiv.org/abs/2003.13678) aims to systematically deduce the best model population starting from a model space that has no constraints. The paper also aims to find a best model population, as opposed to finding a singular best model as in works like [NASNet](https://arxiv.org/abs/1707.07012).
The outcome of this experiment is a family of networks which comprises models with various computational costs. The user can choose a particular architecture based upon the need.
### About the models
Every model of the RegNet family consists of four Stages. Each Stage consists of numerous Blocks. The architecture of this Block is fixed, and three major variants of this Block are available: X Block, Y Block, Z Block. Other variants can be seen in the paper, and the authors state that the model deduction method is robust and RegNets generalize well to these block types.
The number of Blocks and their channel width in each Stage is determined by a simple quantization rule put forth in the paper. More on that in [this blog](https://medium.com/visionwizard/simple-powerful-and-fast-regnet-architecture-from-facebook-ai-research-6bbc8818fb44). RegNets have been the network of choice for self supervised methods like SEER due to their remarkable scaling abilities.

## The Pull Request:
Before opening a pull request which requires large amounts of work, it is advisable to consult the team first so that there is no conflict of interest. After getting a solid confirmation from the Keras team, I started working on the code. You can check out our discussion [here](https://github.com/keras-team/keras/issues/15240). Below is a small snippet from our conversation:

François Chollet and the Keras team were super supportive and made merging the PR a smooth process. I express my heartfelt gratitude to the team for their help.
Even though I had 24 models to implement, the basic code was fairly straightforward. Thus, I was able to create a PR with the code and get reviews from the team quickly. Check out the PR [here](https://github.com/keras-team/keras/pull/15702).

## Training the models:

### General Setup

I mainly used the TPUv3-8 Node for training. It has a 96-core VM with around 335 GB RAM, which handles heavy preprocessing with ease. After  preprocessing raw images were resized to 224x224 as mentioned in the paper. I used multiple TPU Nodes simultaneously to allow running many experiments in parallel. This reduced the experimentation time considerably.

The code used for training is available [here](https://github.com/AdityaKane2001/regnets_trainer).

In this section, I simply jot down the takeaways and methods I used for achieving this performance. 
Input pipeline
I trained these models on the powerful TPU-v3 (thanks to TRC). This meant that I had to employ a lightning-fast input pipeline. Also, the input pipeline must be static, which means I cannot have abrupt changes in the preprocessing graph at runtime (since the preprocessing functions are optimized using AutoGraph). As per the requirements of TPUs, I stored the ImageNet-1k TFRecords on a GCS bucket and employed an interleaved dataset read. 

Learning point: It is important to implement augmentations in the most efficient and stable way possible and minimize slow and redundant ops in the process. 

Here is an example of how one must avoid dynamic changes in the execution graph. In the following example, I create a couple of functions for inception-style cropping, which was popularized by the [original inception paper](https://arxiv.org/pdf/1409.4842.pdf). The point of interest is that `break` statements are not allowed in graph execution because they change the graph on the fly.

```python
this is a test
```

We can see that some chunks of the code are repeated, but this guarantees that the function remains pure. Here being pure simply means absence of break statements, which would otherwise cause the graph to change arbitrarily. One can also see, for example, the variable `w_crop` is cast to `tf.int32` exactly once in the entire function call. It is important to do such optimizations, because we are working with a single image at a time and not a batch of images.   

Apart from inception style cropping, the implementation of the remaining input pipeline was fairly simple. I used inception cropping, channel-wise PCA jitter, horizontal flip and mixup.

PCA jitter: https://github.com/AdityaKane2001/regnets_trainer/blob/63bf8fb00e83fe92ae8a6f2ce2307bc9274d43e0/dataset.py#L211-L236
Mixup: https://github.com/AdityaKane2001/regnets_trainer/blob/63bf8fb00e83fe92ae8a6f2ce2307bc9274d43e0/dataset.py#L353-L382

Random horizontal flip: https://github.com/AdityaKane2001/regnets_trainer/blob/63bf8fb00e83fe92ae8a6f2ce2307bc9274d43e0/dataset.py#L238-L252
 
–
PCA jitter and random horizontal flip were suggested in the paper, whereas addition of mixup was inspired by the papers [Revisited ResNets](https://arxiv.org/abs/2103.07579). 


Effect of weight decay on training
Weight decay is a regularization technique where we penalize the weights for being too large. Weight decay is a battle-tested method and is often used when training deep neural networks. A small note, I used decoupled weight decay and not the conventional implementation of weight decay.  
I saw increasing the weight decay too much made it difficult for the model to converge. However, small weight decay caused the model to have near-constant accuracy during the final epochs. These observations suggest the weight decay is a strong regularizer, especially for smaller models. Inspired by the paper [“Revisiting ResNets: Improved Training and Scaling Strategies”](https://arxiv.org/abs/2103.07579), I kept the weight decay same for large models, since mixup was increased simultaneously. 

  Learning point: Weight decay is a strong regularizer. It is advisable to reduce weight decay or keep it the same for large models, where other augmentations or regularizers are being used simultaneously.   

Finally, I used a constant weight decay of 5e-5 for all models, which was suggested in the original paper. 

Regularization as a function of model size
It is empirically known that increasing augmentation of regularization results in better performance. Conforming to this, I gradually increased the strength of mixup augmentation as the model size increased. I saw good results using this simple technique.

  Learning point: Increase augmentations and regularization when increasing model size.

Smaller models are difficult to train
I had to train 12 variants of RegNetX and RegNetY each. This included small models which don’t have as many parameters as the larger ones. It is speculated that these models simply do not have enough capacity to hold the given information in them. They tend to underfit and the solution is seldom as simple as adding augmentation. The best starting point in most cases was low regularization and medium augmentation. I could tune the rest of the hyperparameters from there. These models took a lot of time to fine-tune and train, whereas the larger models had more flexibility. Smaller models are sensitive to small changes in regularization or augmentation.

 Learning point: Do a hyperparameter search for small models. Repeat the search as the size of models increases.

Noteworthy learnings: 
Use multiple copies of the data if possible 
It was observed the training would stop abruptly and would be stuck at 
the end of an epoch. I use the `tf.data.Dataset.interleave`   method which reads data from multiple TFRecords simultaneously. During this read operation, the TFRecords are unavailable to other processes. I used to train multiple models in parallel, and thus they constantly needed to read data from the same bucket. Thus, to counter this, I created multiple copies of the TFRecords and saved them in different buckets. This reduced collisions and the problem reduced substantially. 
Dump logs at a single location
While training a number of models, maintaining the logs may get out of hand. The best way, in my opinion, is to dump all the raw logs at one location. In our case, I organized the logs and checkpoints of the models using the time and date of training. This made it easier to locate and use the checkpoints where needed. Following is a snap of the same:

Use automation to reduce cognitive load
Managing many experiments simultaneously quickly becomes a difficult task. Automating the things which you need to do repeatedly is an extremely useful thing to do from the beginning.  For example, one can use Weights and Biases (W&B) to automatically track all experiments. It is useful to log the hyperparameters along with the runs in W&B rather than feeding them manually. These seemingly small things reduce a ton of cognitive load, so you can actually focus on what’s important - running experiments. Following is a snapshot of our runs:


Gain intuitions of how the model might react to certain changes to hyperparameters 
After working on a single architecture for days or months, you may notice patterns in the performance of models. This helps in building intuitions of how the model might react to different changes in hyperparameters. Using this newfound intuition, you might be able to come up with ideas which might help in increasing performance. For example, using a slightly higher weight decay for RegNetY004 leads to sudden increase followed by a decrease of accuracy at the end of the run, but using a lower weight decay flattens this out. This implies that usage of a more aggressive augmentation policy along with lower weight decay may help in training, in this case. In similar fashion, one can spot changes in hyperparameters which lead to significant improvements.


Finally, here are the results. In the following tables, I compare our results with the paper. The last column has the hyperparameters which are different from the original implementation.
