---
marp: true
theme: slides
size: 16:9
paginate: true
math: true
---

<style>
section::after {
    content: attr(data-marpit-pagination) '/15';
}
</style>

<!-- _paginate: false -->

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

<style scoped>
p {
    font-size: 24px;
}
</style>

# On proofreading and connectome inference

<div class="columns">
<div>

<br>

##### Ben Pedigo

(he/him)
Scientist I
Allen Institute for Brain Science

![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [ben.pedigo@alleninstute.org](mailto:ben.pedigo@alleninstitute.org)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>
<div>

<!-- Nodes on slide one -->

</div>
</div>

---

# Background

<!-- - EM connectomics is done by automated segmentation, followed by human proofreading
- This process is labor intensive, takes a while, and costly -->

<div class="columns-bl">
<div>

![](images/em-pipeline.png)

</div>
<div>

</div>
</div>

<!-- _footer: MICrONS Consortium et al. (2023) -->

---

# Background

<!-- - EM connectomics is done by automated segmentation, followed by human proofreading
- This process is labor intensive, takes a while, and costly -->

<div class="columns-bl">
<div>

![](images/em-pipeline-focus.png)

</div>
<div>

![center](images/editing.png)

- Labor-intensive
- Costly
- Takes time

</div>
</div>

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Dorkenwald et al. *bioRxiv* (2023) -->

---

<!-- TODO: better title -->

# Proofreading edits

- We have a record of many edits now, across several datasets
  - **>800K in Minnie, ~2.5 million in V1dd**
    ![h:300](./images/cumulative_edits.svg)
- How much do they matter for downstream conclusions?
- Can we predict which edits are most impactful?

---

# Aims

- Aim 1 (paper): develop a quantitative understanding of how proofreading affects connectivity
  - Characterize which connectivity measures are stable/unstable
  - Characterize which edits are impactful
- Aim 2 (system/paper): develop a system for deploying predictions of _impactful_ edits to prioritize for human or automated proofreading

---

# Aim 1: sensitivity to proofreading

- Understand how connectivity features change with proofreading, e.g.:
  - Probability cell $i$ connects to cell $j$
  - Proportion of cell $i$'s outputs onto cell type $k$
  - Proportion of cell $i$'s outputs onto cell type $k$ in compartment $c$
  <!-- TODO: these were clunkier -->

## Why do it?

- Know when we should trust connectivity analyses
  - How much proofreading to identify a cell's connectivity type?
  - How much proofreading to find long-range vs. short-range connections?
- Know how much proofreading is needed to answer a question

<!-- ## Why do it?

- Understand what quantitative claims we can make based on this variance
- Motivate extending analyses to volumes which include unproofread or less proofread cells -->

---

# Approach

![center h:400](./images/approach-partial.png)

---

# Approach

![center h:400](./images/approach-full.png)

#### Allows us to examine connectivity for various "what if" proofreading scenarios

<!-- ---

# Approach

<!-- make these examples more concrete/less mathy -->
<!-- maybe use this more specific language earlier -->

<!-- - Apply a set of edits to a neuron

  - E.g., 50% of edits at random, all edges within $d$ distance to soma, etc.

- For proofread neurons/volume, examine how connectivity features change w/ proofreading
  <!-- - Likely need a "proofreading model" for replaying edits in a plausible way -->

<!-- - Choose connectivity estimands,
  - e.g. $P(\text{type } i \rightarrow \text{type } j)$
  - $P(\text{type } i \rightarrow \text{type } j) \circledast \text{compartment}$, etc. -->

<!-- TODO: create diagram for this -->

---

# Examples: stable neuron

<!-- Replaying some proportion of merges onto a neuron, evaluating connectivity -->

<!-- ![h:400 center](images/exc_group_connectivity_root=864691135865971164.png)
 -->

<div class="columns">
<div>

![center h:400](images/exc_group_connectivity_root_n=864691135865971164.png)

</div>
<div>

![center h:400](images/exc_group_connectivity_root_p=864691135865971164.png)

</div>
</div>

![h:100 center](images/cell-type-legend.png)

<!-- _footer: Neurons from Schneider-Mizell et al *bioRxiv* (2023) -->

---

# Examples: unstable neuron

<div class="columns">
<div>

![center h:400](images/exc_group_connectivity_root_n=864691135992790209.png)

</div>
<div>

![center h:400](images/exc_group_connectivity_root_p=864691135992790209.png)

</div>
</div>

![h:100 center](images/cell-type-legend.png)

<!-- _footer: Neurons from Schneider-Mizell et al *bioRxiv* (2023) -->

---

# Differential edit importance

Distal edits and synapses depend on more proximal merges

<div class="columns">
<div>

![bg right:68%](images/neuron_tree_root=864691135865971164.png)

<!-- **Dependency graph of merges** -->

<!-- ![h:400](images/merge_dependency_tree_root=864691135865971164.png) -->

<!-- ![h:450](images/neuron_tree_root=864691135992790209.png) -->

---

# Comparing edit dependencies

<div class="columns">
<div>

## Stable neuron

![h:300 center](images/n_dependencies_hist-root=864691135865971164.png)

</div>
<div>

## Unstable neuron

![h:300 center](images/n_dependencies_hist-root=864691135992790209.png)

<!-- ![h:450](images/neuron_tree_root=864691135992790209.png) -->

</div>
</div>

<!-- **Proximal edits with many dependents are more important** -->

---

# Aim 2

<div class="columns">
<div>

- Develop a system for predicting edit _impact_ to prioritize for proofreading
  - May be specific to the question at hand

## Why do it?

- Maximize utility of future proofreading efforts given limited resources

</div>
<div>

![center](./images/dependency_hist=864691135992790209.png)

</div>
</div>

---

# Approach

- Use Aim 1 to quantify impact of edits
- Relate morphological features to this impact score

![h:300 center](images/neurd-features.png)

- Test by deploying high-priority edits to proofreaders

<!-- _footer: Celii et al. bioRxiv 2023 -->

---

<!-- try to think i could give it uninterrupted in 12-13 mins -->

# Questions/comments?

---

# Appendix

---

# Prior work on quality-quantity tradeoff

## Would you rather have bit of highly-curated data, or lots of messy data?

![h:150 center](images/quantity-quality-tradeoff.png)

Depends on the question, but there exist theoretical cases where you want the latter

## Would you rather have a bit of highly-curated data or lots of ~~messy~~ _unproofread, biased_ data?

---

# Analogy to "prediction powered inference"

![center h:500](images/prediction-powered-summary.png)

<!-- _footer: Angelopoulos et al. arXiv (2023) -->

---

# Analogy from "prediction powered inference"

![center h:500](images/prediction-powered-examples.png)

<!-- _footer: Angelopoulos et al. arXiv (2023) -->

---

# Resampling skeletons

- Understand {whether, how} skeleton features are affected by proofreading
- Develop classifiers/clustering methods which are robust to such differences
  - E.g. train classifiers on many "messy" neurons

---

# Example frankeneurons

<iframe height=500 frameborder=0 src="images/skeleton_samples_root_id=864691135915450982_use_cc=True.html">
</iframe>

---

# Frankeneuron </br> features

![bg right:65% center h:600](images/feature_samples_root_id=864691135915450982_use_cc=True.png)

---

# Challenges

<!--
- Does not require running much classification code that hasn't already been run, since just operating on the unproofread bulk of Minnie, say -->

- Information already accessible in CAVE, have code for mapping synapses onto their dependant edits
  - May need some new API features to make it scalable
- More specific the question, the smaller our sample size for this kind of approach
- Need to assume some kind of homogeneity across the volume for this to work
  - May not be palatable to the community
- Feature set for a model on how proofreading errors affect connectivity?
- Results are likely question-specific; unclear to what extent any lessons will generalize

---

<!-- Null space of the idea above -->

# Machine-guided or hypothesis-driven proofreading

Now that we have these connectome volumes, how should we spend our time?

- Algorithm that eats a neuron and predicts completeness
- Algorithm that eats a segmentation and predicts sites for edits
  - Better version: eats a segmentation and a _statistic_, predicts _impactful_ edits
    - Find neurons where we need information to assign C-type
    - Find edits likely to attach many synapses

---

# Approach

- Develop feature set, ideally reusing relevant tested models (PSS, SegCLR, ...)
  - Features could involve anything in power set of {image, segmentation, skeleton, skeleton attributes}
- Train {NN, RFC, ...} using training set of available edits to predict {edit locations, completeness level, ...}
- Validate on held out neurons or subvolume
- Deployment is a tricker question
  - V$0$ Could run predictions on a fixed materialization prior to bout of proofreading
- More elaborate version: predict (edit location, importance)
  - E.g. find me edits likely to add many synapses

---

# Challenges

- Little proof-of-concept for feasibility (as far as I know)
  - For a random neuron, can we predict where its primary axon might be?
  - What if you know something about its cell type, say from PSS features?
  - Ditto for predicting completeness from a cell you know nothing else about
- Dynamics: to be useful, would this be running on neurons all the time as they are edited, like the L2cache?
- How would a proofreader interact with such a system?
- Overlap with other work on auto-proofreading?

---

# Thoughts?

Paper on how proofreading affects connectivity estimand

- Have a specific analysis goal, but message could be a general perspective on how to do analysis in light of noisy proofreading
- Side output: defining specific notions of connectivity estimands we care about super clearly
  - Connection probability: $P(i \rightarrow j | i,j)$
  - What we often plot: how cells distribute outputs over output classes: $P(i \rightarrow j \in K)$, $P(i \rightarrow j \in K | d_{ij})$
- Have something that we do expect to fail if there is little proofreading
- Maybe worth keeping this simple...
- Relationship between segmentation error and neuroanatomy

---

<!-- explain this better, makes sense in context of aim 2 -->
<!-- make a diagram that can describe this post hoc importance idea -->

# Example differential edit importance

Merge dependency graphs for two neurons, size of node = # of dependent synapses

<div class="columns">
<div>

![h:520 center](images/merge_dependency_tree_root=864691135995711402.png)

</div>
<div>

![h:520 center](images/merge_dependency_tree_root=864691135013445270.png)

</div>
</div>
