---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
---

<!-- <style>
section::after {
    content: attr(data-marpit-pagination) '/24';
}
</style> -->

<!-- _paginate: false -->
<!-- _class: title-slide -->

![bg](../themes/aibs-backgrounds/title.png)

<!-- ![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg) -->

<!-- <h1 style="margin-top: 200px;">
Connectivity properties in light of proofreading
</h1> -->

<!-- <br> -->

# Quantifying proofreading effects on connectivity

<div class="columns">
<div>

Ben Pedigo
(he/him)
Scientist I
Allen Institute for Brain Science

<div style='' >

![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [ben.pedigo@alleninstitute.org](mailto:ben.pedigo@alleninstitute.org)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>

</div>
<div>

</div>
</div>

---

# Measurement design in connectomics

<br>

<div class="columns">
<div>

![h:250 center](../berlin-2024/images/optimizing-title.png)

</div>
<div>

> Would you rather have many noisy connectivity measurements, or a few high-quality ones?

> There exists cases where you'd actually prefer the "sloppy" version

</div>
</div>

<br>

### Given finite resources, worth reflecting on how to proofread with specific scientific goals in mind

<!-- _footer: Priebe et al. *Communications in Statistics* (2013) -->

---

# Measurements in modern connectomics

### Automated segmentation + proofreading

<!-- ![bg](../themes/aibs-backgrounds/Slide4.png) -->

<div class="columns-br">
<div>

![](../berlin-2024/imagesimages/editing.png)

<div class="p" style="font-size: 0.55em; text-align: center;">

CAVE: Connectome Annotation Versioning Engine
Dorkenwald, Schneider-Mizell et al. _bioRxiv_ (2023)

</div>

</div>
<div>

![h:500 center](../berlin-2024/images/all_edits_by_time-target_id=271886.gif)

</div>
</div>

<!-- ### How do these edits affect downstream conclusions? -->

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Schneider-Mizell et al. *bioRxiv* (2023) -->

---

# Inhibition in mouse visual cortex

![h:160 center](../berlin-2024/images/inhibition-census-wide.png)

![center h:300](../berlin-2024/images/casey-heatmap.png)

<div style="position: absolute; bottom: 30px; right: 140px;">

![h:60](../berlin-2024/images/casey-legend.png)

</div>

<!-- _footer: Schneider-Mizell et al. *bioRxiv* (2023) -->

<!-- ---

# Inhibition in mouse visual cortex

<div class="columns">
<div>

![](images/inhibitory-gallery.png)

</div>
<div>

- 163 inhibitory neurons were heavily proofread
- Characterized how inhibitory neurons distribute their outputs:

{diagram of proportion of outputs metric}

</div>
</div>

<!--
# CAVE allows us to extract the complete edit history

![h:500 center](./images/all_edits_by_time-root_id=864691135213953920.gif)

_footer: Dorkenwald, Schneider-Mizell et al. *bioRxiv* (2023) -->

---

<!-- # Connectivity during proofreading -->

![bg center fit](../berlin-2024/images/all_edits_by_time_with_plots-target_id=271886.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](../berlin-2024/images/cell-type-legend.png)

</div>

<div style="position: absolute; bottom: 20px; right: 60px;">

![h:280](../berlin-2024/images/white.png)

</div>

---

<!-- # Connectivity during proofreading -->

<!-- _backgroundImage: None -->

![bg blur:5px opacity:40%](../berlin-2024/images/paused.png)

<!-- <div style="position: absolute; bottom: 20px; right: 60px;">

![h:280](images/white.png)

</div> -->

![center h:600](../berlin-2024/images/distance-transparent.png)

---

![bg center fit](../berlin-2024/images/all_edits_by_time_with_plots-target_id=271886-copy.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](../berlin-2024/images/cell-type-legend.png)

</div>

---

# Cell-type specific connectivity converged quickly

![h:500 center](../berlin-2024/images/distance-lines-animation.gif)

---

# Counterfactual proofreading

Replay specific edits and not others, reconstruct what the network would look like

<div class="columns">
<div>

### What if I'd proofread each neuron to 50% extension?

![](../berlin-2024/images/clustering-target_p=0.5.png)

</div>
<div>

### Full proofreading

<br>

![](../berlin-2024/images/clustering-target_p=1.png)

</div>
</div>

<span style="text-align: center;">

NMI(50% proofreading, full proofreading) = 0.82

</span>

<!-- - So far, have looked at how neurons changed over the course of proofreading in actuality, but this is a somewhat arbitrary historical ordering
- Can replay edits (or not) according to alternative schemes
- E.g. what if we only had half the proofreading resources - how should we allocate them? -->

---

# Summary

<!-- - Worth understanding whether most neurons look like they have converged -->

- NOT saying we need less proofreading...
- Monitoring proofreading with specific analyses/metrics in mind could help us decide how much proofreading is needed for a specific question
- Counterfactual replay of edits can help understand how alternative proofreading strategies would affect downstream analyses

# Ongoing work

- Prediction of edit impact with respect to a feature of interest
<!-- - Prediction of whether a neuron is proofread enough for a specific analysis -->

<!-- - Counterfactual replay of various edit schemes can help understand how alternative proofreading strategies might affect downstream analyses -->
<!-- - Analyses could be applied to other datasets or even to analyze how design of automated proofreading systems affects conclusions -->

---

# Can we find heuristics for deciding how "done" neurons are?

![center](images/doneness.jpg)

---

# Setup

- We have 163 sequences of neuron-states for neurons which were proofread in the column for Casey's paper.
- Retrospectively, for each neuron, we can compute how far a given feature is from the final state. So each state has an associated scalar distance.
  - Here the connectivity feature is proportion of outputs onto each M-type.
- I create labels for each neuron state as "good enough" or "not good enough", where "good enough" just means the distance to final state is < 0.2 Euclidean distance from final
  - This threshold is a parameter, of course. Could also not threshold at all and just do regression.

---

# Setup (cont.)

- Now, we associate each neuron-state with some simple features:
  - Number of output synapses
  - Number of input synapses
  - Number of level2 nodes (proxy for size)
  - Path length (proxy for size)
  - Number of edits (only using "filtered" edits)
- Using the proofreading history, the Goal is to use these features to predict the label described on the last slide, is a cell "good enough" in its current state?

---

# Features for our heuristic/classifier

<div class="columns">
<div>

![center h:250](images/distance-transparent-cut.png)

![center h:100](images/legend-euc-dist.png)

<br>

\*stuff is on a log scale here $\rightarrow$

</div>
<div>

![center h:500](./images/state_prediction_heuristics/proofreading_feature_pairplot.png)

</div>
</div>

---

# LDA on proofreading features

- Log-transformed features
- Ran linear discriminant analysis (LDA)
- One version fit separately for each cell type (ITC, PTC, STC, DTC)
- One version fit for all cell types, pooled
- The pooled version did just as well, so sticking with that for now since it's simpler (see supplementd)

---

# LDA posterior ratios

<div class="columns">
<div>

$$log \left( \frac{P[y=1 | x]}{P[y=0 | x]} \right)$$

Higher number = more likely to be "good enough"

</div>
<div>

![center h:500](./images/state_prediction_heuristics/lda_decision_function.png)

</div>
</div>

---

# Precision-recall

<div class="columns">
<div>

![center h:470](./images/state_prediction_heuristics/precision_recall_curve.png)

</div>
<div>

![center h:470](./images/state_prediction_heuristics/precision_recall_overlay.png)

</div>
</div>

\*classification metrics here use a sample weight so that all neurons are equally weighted

---

# Now, I computed the same features and ran this classifier for all neurons with putative inhibitory labels

---

# Rating all inhibitory cells

Posterior ratio for ~8,000 putative inhibitory cells (`aibs_metamodel_mtypes_v661_v2`)

![center h:480](./images/state_prediction_heuristics/new_log_posterior_ratio.png)

---

# Posteriors by class

<div class="columns">
<div>

Count

![h:450 center](./images/state_prediction_heuristics/log_posterior_ratio_count_by_mtype.png)

</div>
<div>

Density

![h:450 center](./images/state_prediction_heuristics/log_posterior_ratio_density_by_mtype.png)

</div>
</div>

---

# Posterior for proofread cells

Cells with putative inhibitory label and entry in `proofreading_status_public_release`

![center h:480](./images/state_prediction_heuristics/proofread_log_posterior_ratio.png)

---

# Ratings are well spread out

![center h:500](./images/spatial-locs.png)

---

# How many cells do we have?

...for varying thresholds for the classifier.

Note that precision-recall here are obviously just estimates since they came from the column training set

![h:500 bg right](./images/state_prediction_heuristics/log_posterior_ratio_survival_precision_recall.png)

---

<div class="columns">
<div>

![](./images/state_prediction_heuristics/log_posterior_ratio_survival.png)

</div>
<div>

![](./images/state_prediction_heuristics/posterior_ratio_quantile_survival.png)

</div>
</div>

---

# Example cells

The (putative) good:
https://ngl.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4953793234993152

The (putative) bad:
https://ngl.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5885470224416768

---

# For various thresholds on the posterior...

- Select the neurons that pass that threshold
- Cluster on neuron output proportions
- Using k=40
  - Likely an oversplitting, but I found this easier to look at for trying to map onto Casey's clustering
- Just using Ward's for clustering

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=0-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=1-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=2-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=3-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=4-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=5-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=6-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=7-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=8-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=9-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_w_tree-threshold=10-k=40-metric=euclidean-method=ward.png)

---

# Same data, now attempted to sort by depth

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=0-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=1-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=2-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=3-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=4-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=5-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=6-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=7-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=8-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=9-k=40-metric=euclidean-method=ward.png)

---

![](./images/state_prediction_heuristics/excitatory_inhibitory_clustermap_sorted-threshold=10-k=40-metric=euclidean-method=ward.png)

---

# Looking at clusters

[Link to neuroglancer view with clustering at all levels as tags](<https://ngl.cave-explorer.org/#!%7B%22showSlices%22:false,%22layout%22:%22xy-3d%22,%22crossSectionScale%22:1e-08,%22projectionScale%22:0.001,%22layers%22:%5B%7B%22type%22:%22image%22,%22source%22:%5B%7B%22url%22:%22precomputed://https://bossdb-open-data.s3.amazonaws.com/iarpa_microns/minnie/minnie65/em%22%7D%5D,%22name%22:%22img%22%7D,%7B%22type%22:%22segmentation%22,%22source%22:%5B%7B%22url%22:%22graphene://middleauth+https://minnie.microns-daf.com/segmentation/table/minnie3_v1%22%7D,%7B%22url%22:%22precomputed://middleauth+https://global.daf-apis.com/nglstate/api/v1/property/6038514572460032%22%7D,%7B%22url%22:%22precomputed://middleauth+https://minnie.microns-daf.com/skeletoncache/api/v1/minnie65_phase3_v1/precomputed/skeleton%22%7D%5D,%22skeletonRendering%22:%7B%22shader%22:%22void%20main()%20%7B%5Cn%20%20emitDefault();%5Cn%7D%5Cn%22%7D,%22selectedAlpha%22:0.3,%22objectAlpha%22:1.0,%22notSelectedAlpha%22:0.0,%22name%22:%22seg%22%7D%5D%7D>)

---

# Acknowledgements

<style scoped>
p {
    font-size: 11px;
}
</style>

<div class="columns">
<div>

**Network Anatomy**
Clay Reid
Agnes Bodor
Adam Bleckert
JoAnn Buchanan
Casey M. Schneider-Mizell
Dan Bumbarger
Derrick Brittain
Forrest Collman
Steven Cook
Nuno da Costa
Bethanny Danskin
Sven Dorkenwald
Leila Elabbady
Emily Joyce
Dan Kapner
Sam Kinn
Cheryl Lea
Gayathri Mahalingam
Ben Pedigo
Sharmi Seshamani
Jenna Schardt
Marc Takeno
Russel Torres
Wenjing Yin
Chi Zhang

</div>
<div>

**PM**
Lynne Becker
Florence D'Orazi
Sarah Naylor
Shelby Suckow
David Vumbaco
Susan Sunkin

**Morphology and 3D Reconstruction**
Rachel Dalley
Clare Gamlin
Staci Sorensen
Grace Williams

**Modeling & Simulation**
Ani Nandi
Tom Chartrand
Anatoly Buchin
Yina Wei
Soo Yeun Lee
Costas Anastassiou

**Technology**
Tim Fliss
Rob Young
And others

**IT**
Brian Youngstrom
Stuart Kendrick
Scott Harrison
Nathaniel Middleton
And others

</div>
<div>

**MPE**
Jay Borseth
Collin Farrell
And others

**MindScope**
Reza Abbasi-Asi
Anton Arkhipov
Michael Buice
Daniel Denman
Brian Hu
Josh Larkin
Stefan Mihalas
Daniel Millmann
Gabe Ocker
Naveen Ouellette
Kevin Takasaki
Saskia de Vries
Jun Zhuang

**Alen Institute for Brain Sciences**
Tanya Daigle
Shenqin Yao
Nikolas Jorstad
Trygve Bakken
Rebecca Hodge
Nathan Gouwens
Bosiljka Tasic
Ed Lein
Hongkui Zeng
And many others

</div>
<div>

**Princeton**
Sven Dorkenwald
Tommy Macrina
Sebastian Seung
Nick Turner
And team

**Baylor**
Jake Riemer
Andreas Tolias
And team

**Harvard Medical School**
Brett Graham
Wei-Chung Lee
And team

**Janelia**
Khaled Khairy
Stephan Saalfeld
Carolyn Ott
Jennifer Lippincott-Schwartz
And others

**JHU**
Jenna Glatzer
Dwight Bergles

**APL**
Brock Wester
And team

</div>
<div>

**Neuro Surgery and Behavior**
**Lab Animal Services**
**Transgenic Colony Management**
**Finance**
**Legal**

**Computing Resources**
BBP5 Supercomputing Resources
National Energy Research Computing Center
AI HPC
Google Cloud

**Funding**
IARPA - MICRONS
NSF - NeuroNex
NIH – BICCN

</div>
</div>

<!-- ---

# How would clustering change with different proofreading schemes?

![center ](images/ari-vs-merges.png)

--- -->
<!--
# Impactful edits are more often near the soma

![center](images/distance_vs_impact.png)

--- -->
<!--
# Space of simple edit allocation schemes

![center](images/iso-edit-contours.png) -->

<!-- # (1) "sloppy" proofreading?

![](images/half_edit_heatmaps.png) -->

<!-- ---

# (2) what if I omit individual edits? (importance)

![h:500 center](images/edit_dropout_importance_root_id=864691135213953920.png) -->

<!-- ---

# (3) which neurons are "good enough"?

![h:500 center](images/closeness-by-n_outputs.png) -->

<!-- # Estimating reciprocal ratios

![center](images/reciprocal-ratio.png) -->

---

# Supplement

---

# Cell-type specific pooled LDA performed the same

<div class="columns">
<div>

![center h:450](images/pooled-vs-split-f1.png)

</div>
<div>

![center h:450](images/pooled-vs-split-acc.png)

</div>
</div>

\*Interpreting precision/recall/accuracy is a bit tough here; computed over neuron-states

<!-- ---

# Split by cell type

```
By cell type accuracy:
DTC: 0.9596586501163693
ITC: 0.9136459062281316
PTC: 0.9762838957188944
STC: 0.9459313327926466
```

```
By cell type scores:
              precision    recall  f1-score   support

       False       0.95      0.84      0.89      8518
        True       0.96      0.99      0.97     29263

    accuracy                           0.95     37781
   macro avg       0.95      0.91      0.93     37781
weighted avg       0.95      0.95      0.95     37781
```

---

# Pooled

```
Pooled scores:
              precision    recall  f1-score   support

       False       0.94      0.83      0.88      8518
        True       0.95      0.99      0.97     29263

    accuracy                           0.95     37781
   macro avg       0.95      0.91      0.93     37781
weighted avg       0.95      0.95      0.95     37781
``` -->

---

# Feature sets comparison

![center h:500](./images/feature_set_f1_scores.png)
