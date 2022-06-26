## This repository provides the supplementary data for the paper: Insect pest image recognition

### Matching networks
Matching networks is referred to [oscarknagg's code](https://github.com/oscarknagg/few-shot).

### Prototypical networks
Prototypical networks is referred to [cnielly
's code](https://github.com/cnielly/prototypical-networks-omniglot)

### Pairwise similarity with Bregman Divergences

- Euclidean;
- Mahalanobis;
- Kullback–Leibler (KL-divergence);
- Itakura–Saito (IS-divergence).

### Dataset:
Data set will be uploaded

### An adult maturity stage insect classification task:

![Episode](/Figures/task_example_adult.jpg)

### An early maturity stage insect classification task:

![Episode](/Figures/task_example_adult.jpg)

## Experiment results:

// Node.js
let MarkdownIt = require('markdown-it'),
    MarkdownItMergeCells = require('markdown-it-merge-cells'),
    md = new MarkdownIt();
md.use(MarkdownItMergeCells);

// Browser (use dist/bundle.min.js)
let md = new window.markdownit();
md.use(window.markdownitMergeCells);

let result = md.render(`
|1|1|3|4|5|
|-|-|-|-|-|
|1|1|2|2|6|
|1|1|2|2|7|
|1|4|3|5|5|
`)

