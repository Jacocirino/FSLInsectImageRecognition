This repository provides the supplementary data for the paper: **Insect pest image recognition: A few-shot machine learning approach including maturity stages classification**

### Code references
Matching networks is referred to [oscarknagg's code](https://github.com/oscarknagg/few-shot).

Prototypical networks is referred to [cnielly's code](https://github.com/cnielly/prototypical-networks-omniglot).

### Pairwise similarity with Bregman Divergences
The file **[Bregman_divergences](/Bregman_divergences.py)** provides the script for the divergences used as similarity functions. For use, replace the similarity functions in the chosen Few-shot Learning algorithm.

- Euclidean;
- Mahalanobis;
- Kullback–Leibler (KL-divergence);
- Itakura–Saito (IS-divergence).

### IP-FSL data set:
The IP-FSL data set, based on curated images from [IP102](https://openaccess.thecvf.com/content_CVPR_2019/html/Wu_IP102_A_Large-Scale_Benchmark_Dataset_for_Insect_Pest_Recognition_CVPR_2019_paper.html), is composed 97 classes of adult insect pest images, and 45 classes of early stages, totalling 6,817 images.
IP-FSL can be downloaded here: https://drive.google.com/file/d/12iguabGCTC2aVpkP8zTDhOeP6HgndeQ5/view?usp=sharing.

<img src="/Figures/data_config.jpg" alt="drawing" width="300"/>

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


