---
permalink: /opensource/gsoc2022report
title: "GSoC 2022 at TensorFlow : Final Report"
collection: opensource
author_profile: true
---

## **Contribute to KerasCV and KerasNLP**


## Objectives
The main objective was to contribute valuable components to KerasCV(https://keras.io/keras_cv/) that would help developers create computer vision solutions quickly and effectively. Concretely, the tasks were as follows:
- To port over models from [keras.applications](https://keras.io/api/applications/) to keras_cv. 
- To incorporate preprocessing and model building layers into keras_cv.
<br>


## Acknowledgement

I thank [Google Summer of Code](https://summerofcode.withgoogle.com/) and [TensorFlow](https://www.tensorflow.org) for this opportunity. I am grateful to my mentors [Sayak Paul](https://sayak.dev/) and [Luke Wood](https://lukewood.xyz/about) for their continuous guidance and encouragement. Without them this project would not have been possible. Lastly, I would like to thank members of the Keras team who helped me during the process. 
<br>

## Overview

[KerasCV](https://keras.io/keras_cv/) is a new library in the Keras ecosystem. It is targeted towards computer vision engineers who can use it to create efficient pipelines quickly. During GSoC 2022, I incorporated useful model blocks and preprocessing layers which would help developers build models and pipelines quickly. I also ported over some models from Keras to KerasCV. Addition of EfficientNets, ResNets and RandomResizedCrop layer were my most significant contributions.
<br>

## Important milestones

### Model Blocks

KerasCV, being a new library, had many requests for additions of various model blocks. Considering those, we added a few model blocks: [StochasticDepth](https://github.com/keras-team/keras-cv/pull/474), [DropPath](https://github.com/keras-team/keras-cv/pull/480) and [SqueezeAndExcite](https://github.com/keras-team/keras-cv/pull/505) block. The main takeaway from these implementations was that these implementations need to be flexible enough to cater to the needs of users. Hence it was important not to fixate on the implementation in their original papers, as the blocks may have many varied downstream applications.
<br>

### Preprocessing layers

Augmentations and image preprocessing are integral operations of computer vision. My contributions in this regard were mostly related to bug fixes. We fixed some bugs as well as added a foolproof testing module such that any new additions would not need special conditions for testing. Apart from that, we added [RandomResizedCrop](https://github.com/keras-team/keras-cv/pull/738) (RRC) to KerasCV.
<br>

### Porting over models from Keras:

The target of KerasCV is to be a horizontal extension of Keras. This meant that the computer vision model architectures in Keras should be housed in KerasCV. We ported over some models from Keras: [EfficientNets](https://github.com/keras-team/keras-cv/pull/740), [RegNets](https://github.com/keras-team/keras-cv/pull/739) and [ResNets](https://github.com/keras-team/keras-cv/pull/558). The main challenge was to make the new implementations future-proof. For this purpose, the team has decided to retrain all models ported over to KerasCV. This is something that is ongoing and I will try to contribute to this in the future as well.
<br>   

## Parting thoughts

The last three months have been phenomenal. During GSoC ‘22, I got a chance to work on one of the most acclaimed frameworks for deep learning. It gave me the opportunity to work with the best developers in computer vision. I learnt a lot about TensorFlow, Keras and deep learning in general. I look forward to continuing to contribute to KerasCV in the future. 
<br>

## Important links
1. [KerasCV](https://github.com/keras-team/keras-cv/)
2. [My merged PRs](https://github.com/keras-team/keras-cv/search?o=desc&p=1&q=is%3Apr+author%3AAdityaKane2001&s=committer-date&type=commits)
3. [Google Summer of Code project page](https://summerofcode.withgoogle.com/programs/2022/projects/hkRbtWVD)
