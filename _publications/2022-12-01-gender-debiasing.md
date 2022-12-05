---
title: "Efficient Gender Debiasing of Pre-trained Indic Language Models"
collection: publications
permalink: /publication/2022-12-01
excerpt: 'A state-of-the-art baseline for VQA on the FloodNet dataset. Won the Second Best Paper award in NewInML Workshop 2022.'
date: 2022-12-01
venue: 'AAAI 2023 Deployable AI workshop'
paperurl: 'https://arxiv.org/abs/2209.03661'
citation: 'Kirtane, N., Manushree, V. and Kane, A., 2022. Efficient Gender Debiasing of Pre-trained Indic Language Models. arXiv preprint arXiv:2209.03661.'
---
The gender bias present in the data on which language models are pre-trained gets reflected in the systems that use these models. The model's intrinsic gender bias shows an outdated and unequal view of women in our culture and encourages discrimination. Therefore, in order to establish more equitable systems and increase fairness, it is crucial to identify and mitigate the bias existing in these models. While there is a significant amount of work in this area in English, there is a dearth of research being done in other gendered and low resources languages, particularly the Indian languages. English is a non-gendered language, where it has genderless nouns. The methodologies for bias detection in English cannot be directly deployed in other gendered languages, where the syntax and semantics vary. In our paper, we measure gender bias associated with occupations in Hindi language models. Our major contributions in this paper are the construction of a novel corpus to evaluate occupational gender bias in Hindi, quantify this existing bias in these systems using a well-defined metric, and mitigate it by efficiently fine-tuning our model. Our results reflect that the bias is reduced post-introduction of our proposed mitigation techniques. Our codebase is available publicly.


[Download paper here](https://arxiv.org/pdf/2209.03661.pdf)

If you find our paper useful in your research, please consider citing:
```
@article{kirtane2022efficient,
  title={Efficient Gender Debiasing of Pre-trained Indic Language Models},
  author={Kirtane, Neeraja and Manushree, V and Kane, Aditya},
  journal={arXiv preprint arXiv:2209.03661},
  year={2022}
}
```