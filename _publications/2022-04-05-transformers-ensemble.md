---
title: "Transformer based ensemble for emotion detection"
collection: publications
permalink: /publication/2022-04-05-transformers-ensemble
excerpt: 'Emotion detection using innovative data sampling techniques and ensemble of transformers.'
date: 2022-04-05
venue: 'ACL WASSA Workshop'
paperurl: 'https://aclanthology.org/2022.wassa-1.25/'
citation: 'Aditya Kane, Shantanu Patankar, Sahil Khose, and Neeraja Kirtane. 2022. Transformer based ensemble for emotion detection. In Proceedings of the 12th Workshop on Computational Approaches to Subjectivity, Sentiment & Social Media Analysis, pages 250–254, Dublin, Ireland. Association for Computational Linguistics.'
---
Detecting emotions in languages is important to accomplish a complete interaction between humans and machines. This paper describes our contribution to the WASSA 2022 shared task which handles this crucial task of emotion detection. We have to identify the following emotions: sadness, surprise, neutral, anger, fear, disgust, joy based on a given essay text. We are using an ensemble of ELECTRA and BERT models to tackle this problem achieving an F1 score of 62.76%. Our codebase ([this https URL](https://github.com/AdityaKane2001/ACL_WASSA)) and our WandB project ([this https URL](https://wandb.ai/acl_wassa_pictxmanipal/acl_wassa)) is available.

[Download paper here](https://aclanthology.org/2022.wassa-1.25/)

If you find our paper useful in your research, please consider citing:
```
@inproceedings{kane-etal-2022-transformer,
    title = "Transformer based ensemble for emotion detection",
    author = "Kane, Aditya  and
      Patankar, Shantanu  and
      Khose, Sahil  and
      Kirtane, Neeraja",
    booktitle = "Proceedings of the 12th Workshop on Computational Approaches to Subjectivity, Sentiment {\&} Social Media Analysis",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wassa-1.25",
    doi = "10.18653/v1/2022.wassa-1.25",
    pages = "250--254",
    abstract = "Detecting emotions in languages is important to accomplish a complete interaction between humans and machines. This paper describes our contribution to the WASSA 2022 shared task which handles this crucial task of emotion detection. We have to identify the following emotions: sadness, surprise, neutral, anger, fear, disgust, joy based on a given essay text. We are using an ensemble of ELECTRA and BERT models to tackle this problem achieving an F1 score of 62.76{\%}. Our codebase (https://bit.ly/WASSA{\_}shared{\_}task) and our WandB project (https://wandb.ai/acl{\_}wassa{\_}pictxmanipal/acl{\_}wassa) is publicly available.",
}
```