This repository provides the supplementary data for the paper: Insect pest image recognition: **A few-shot machine learning approach including maturity stages classification**

### Code references
Matching networks is referred to [oscarknagg's code](https://github.com/oscarknagg/few-shot).

Prototypical networks is referred to [cnielly's code](https://github.com/cnielly/prototypical-networks-omniglot).

### Pairwise similarity with Bregman Divergences
The file **[Bregman_divergences](/Bregman_divergences.py)** provides the script for the divergences used as similarity functions. For use, replace the similarity functions in the chosen Few-shot Learning algorithm.

- Euclidean;
- Mahalanobis;
- Kullback–Leibler (KL-divergence);
- Itakura–Saito (IS-divergence).

### Dataset:
Data set will be uploaded https://drive.google.com/file/d/12iguabGCTC2aVpkP8zTDhOeP6HgndeQ5/view?usp=sharing


### Adult maturity stage insect classification task:

<!-- ![Episode](/Figures/task_example_adult.jpg) -->
<img src="/Figures/task_example_adult.jpg" alt="drawing" width="600"/>

#### Experiment results:
<!-- ![Adult_results](/Figures/adult_results.png) -->
<img src="/Figures/adult_results.png" alt="drawing" width="500"/>

### Early maturity stage insect classification task:

<!-- ![Episode](/Figures/task_example_adult.jpg) -->
<img src="/Figures/task_example_early.jpg" alt="drawing" width="600"/>

#### Experiment results:
<!-- ![Early_results](/Figures/early_results.png) -->
<img src="/Figures/early_results.png" alt="drawing" width="500"/>


