---
title: "Spread Love Not Hate: Undermining the Importance of Hateful Pre-training for Hate Speech Detection"
collection: publications
permalink: /publication/2022-12-10-spread-love-not-hate
excerpt: 'Investigating impact of domain specific pretraining on downstream performance in Marathi.'
date: 2022-12-10
venue: 'NeurIPS 2022 I Can't Belive It's Not Better workshop'
paperurl: 'https://openreview.net/pdf?id=AEtndraI8jr5'
---
Pre-training large neural language models, such as BERT, has led to impressive gains on many natural language processing (NLP) tasks. Although this method has proven to be effective for many domains, it might not always provide desirable benefits. In this paper, we study the effects of hateful pre-training on low-resource hate speech classification tasks. While previous studies on the English language have emphasized its importance, we aim to augment their observations with some non-obvious insights. We evaluate different variations of tweet-based BERT models pre-trained on hateful, non-hateful, and mixed subsets of a 40M tweet dataset. This evaluation is carried out for the Indian languages Hindi and Marathi. This paper is empirical evidence that hateful pre-training is not the best pre-training option for hate speech detection. We show that pre-training on non-hateful text from the target domain provides similar or better results. Further, we introduce HindTweetBERT and MahaTweetBERT, the first publicly available BERT models pre-trained on Hindi and Marathi tweets, respectively. We show that they provide state-of-the-art performance on hate speech classification tasks. We also release hateful BERT for the two languages and a gold hate speech evaluation benchmark HateEval-Hi and HateEval-Mr consisting of manually labeled 2000 tweets each. The models and data are available at [this https URL](https://github.com/l3cube-pune/MarathiNLP).

[Download paper here](https://arxiv.org/abs/2210.04267)
