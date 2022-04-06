---
title: "Transformer based ensemble for emotion detection"
collection: publications
permalink: /publication/2022-04-05-transformers-ensemble
excerpt: 'Emotion detection using innovative data sampling techniques and ensemble of transformers.'
date: 2022-04-05
venue: 'ACL WASSA Workshop'
paperurl: 'https://arxiv.org/pdf/2203.11899.pdf'
citation: 'Kane, A., Patankar, S., Khose, S. and Kirtane, N., 2022. Transformer based ensemble for emotion detection. arXiv preprint arXiv:2203.11899.'
---
Detecting emotions in languages is important to accomplish a complete interaction between humans and machines. This paper describes our contribution to the WASSA 2022 shared task which handles this crucial task of emotion detection. We have to identify the following emotions: sadness, surprise, neutral, anger, fear, disgust, joy based on a given essay text. We are using an ensemble of ELECTRA and BERT models to tackle this problem achieving an F1 score of 62.76%. Our codebase ([this https URL](https://github.com/AdityaKane2001/ACL_WASSA)) and our WandB project ([this https URL](https://wandb.ai/acl_wassa_pictxmanipal/acl_wassa)) is available.

[Download paper here](https://arxiv.org/pdf/2203.11899.pdf)

If you find our paper useful in your research, please consider citing:
```
@misc{https://doi.org/10.48550/arxiv.2203.11899,
  doi = {10.48550/ARXIV.2203.11899},
  url = {https://arxiv.org/abs/2203.11899},
  author = {Kane, Aditya and Patankar, Shantanu and Khose, Sahil and Kirtane, Neeraja},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Transformer based ensemble for emotion detection},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```