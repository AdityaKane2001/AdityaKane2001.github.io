---
title: "Continual VQA for Disaster Response Systems"
collection: publications
permalink: /publication/2022-10-31-continualvqa
excerpt: 'We study the VQA problem for the Floodnet dataset in continual and zero shot setting.'
date: 2022-10-31
venue: NeurIPS 2022 Tackling Climate Change with Machine Learning workshop'
paperurl: 'https://arxiv.org/abs/2209.10320'
---

Visual Question Answering (VQA) is a multi-modal task that involves answering questions from an input image, semantically understanding the contents of the image and answering it in natural language. Using VQA for disaster management is an important line of research due to the scope of problems that are answered by the VQA system. However, the main challenge is the delay caused by the generation of labels in the assessment of the affected areas. To tackle this, we deployed pre-trained CLIP model, which is trained on visual-image pairs. however, we empirically see that the model has poor zero-shot performance. Thus, we instead use pre-trained embeddings of text and image from this model for our supervised training and surpass previous state-of-the-art results on the FloodNet dataset. We expand this to a continual setting, which is a more real-life scenario. We tackle the problem of catastrophic forgetting using various experience replay methods. Our training runs are available at: this https URL. Our code is available at this https URL.

[Download paper here](https://arxiv.org/pdf/2209.10320.pdf)
